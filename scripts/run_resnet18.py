import argparse
import sys
import os
import cv2
from moviepy.editor import ImageSequenceClip

# Add the src directory to the system path to allow module imports
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

try:
    # Import the core detection logic (Ensure this file exists in the src/resnet18_segmentation/ directory)
    from resnet18_segmentation.ultrafastLaneDetector import UltrafastLaneDetector, ModelType
except ImportError:
    print("[ERROR] ultrafastLaneDetector module not found. Please check the src/resnet18_segmentation/ directory.")
    sys.exit(1)

def process_video(video_path, model_path, output_path):
    print("[INFO] Loading ResNet-18 Model...")
    # Set use_gpu=True if CUDA/GPU is available, otherwise keep it False
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
        
        # Perform AI-based lane detection
        output_img = lane_detector.detect_lanes(frame)
        
        # Convert BGR to RGB (Required by MoviePy for correct color mapping)
        frames.append(cv2.cvtColor(output_img, cv2.COLOR_BGR2RGB))
        
        frame_count += 1
        if frame_count % 100 == 0:
            print(f"       Processed {frame_count} frames...")

    cap.release()

    print("[INFO] Saving corruption-free video using MoviePy...")
    clip = ImageSequenceClip(frames, fps=fps)
    clip.write_videofile(output_path, codec='libx264', audio=False)
    
    print(f"[SUCCESS] Video successfully saved at: {output_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="ResNet-18 Lane Detection Inference Script")
    parser.add_argument("--source", type=str, required=True, help="Path to the input video file")
    parser.add_argument("--weights", type=str, required=True, help="Path to the ResNet-18 model weights (.pth)")
    parser.add_argument("--output", type=str, default="data/sample_outputs/resnet_result.mp4", help="Path to save the output video")
    
    args = parser.parse_args()
    process_video(args.source, args.weights, args.output)