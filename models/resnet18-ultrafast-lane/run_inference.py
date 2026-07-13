import argparse
import sys
import os
import cv2
from moviepy import ImageSequenceClip

# The ultrafastLaneDetector library now lives right next to this script
sys.path.append(os.path.dirname(os.path.abspath(__file__)))


def patch_ragged_array_bug():
    """
    Newer numpy versions raise an error when this library builds an array from
    lane-point lists of uneven length. Patch it once, in place, if needed.
    """
    target_file = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        "ultrafastLaneDetector", "ultrafastLaneDetector.py",
    )
    with open(target_file, "r") as f:
        code = f.read()
    old = "return np.array(lanes_points), np.array(lanes_detected)"
    new = "return np.array(lanes_points, dtype=object), np.array(lanes_detected, dtype=object)"
    if old in code:
        code = code.replace(old, new)
        with open(target_file, "w") as f:
            f.write(code)
        print("[INFO] Patched ragged-array bug in ultrafastLaneDetector.py")


try:
    from ultrafastLaneDetector import UltrafastLaneDetector, ModelType
except ImportError:
    print("[ERROR] ultrafastLaneDetector module not found. Check models/resnet18-ultrafast-lane/ultrafastLaneDetector/")
    sys.exit(1)


def process_video(video_path, model_path, output_path):
    patch_ragged_array_bug()

    print("[INFO] Loading ResNet-18 Model...")
    lane_detector = UltrafastLaneDetector(model_path, ModelType.TUSIMPLE, use_gpu=False)

    print(f"[INFO] Opening video file: {video_path}")
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print("[ERROR] Could not open the video file.")
        return

    fps = int(cap.get(cv2.CAP_PROP_FPS))
    frames = []
    frame_count = 0

    print("[INFO] Starting frame processing...")
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        output_img = lane_detector.detect_lanes(frame)
        frames.append(cv2.cvtColor(output_img, cv2.COLOR_BGR2RGB))
        frame_count += 1
        if frame_count % 100 == 0:
            print(f"       Processed {frame_count} frames...")
    cap.release()

    os.makedirs(os.path.dirname(output_path) or ".", exist_ok=True)
    print("[INFO] Saving corruption-free video using MoviePy...")
    clip = ImageSequenceClip(frames, fps=fps)
    clip.write_videofile(output_path, codec="libx264", audio=False)
    print(f"[SUCCESS] Video successfully saved at: {output_path}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="ResNet-18 Lane Detection Inference Script")
    parser.add_argument("--source", type=str, required=True, help="Path to the input video file")
    parser.add_argument("--weights", type=str, required=True, help="Path to the ResNet-18 model weights (.pth)")
    parser.add_argument("--output", type=str, default="data/sample_outputs/resnet_result.mp4", help="Path to save the output video")
    args = parser.parse_args()
    process_video(args.source, args.weights, args.output)