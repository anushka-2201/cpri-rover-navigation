"""
Run Ultra-Fast-Lane-Detection (ResNet-18, pretrained on TuSimple) on a video file.

Cleaned, reusable version of the original Colab notebook — same steps, but as a
single script instead of sequential cells:
  1. patch the vendored inference library's known ragged-array numpy bug
  2. load the model + weights
  3. run frame-by-frame inference
  4. write an annotated output video

Usage:
    python run_inference.py --video path/to/input.mp4 \
                             --weights weights/tusimple_18.pth \
                             --output path/to/output.mp4 \
                             --model-type tusimple
"""

import argparse
import os
import sys

import cv2
from tqdm import tqdm

LIB_DIR = os.path.join(os.path.dirname(__file__), "ultrafastLaneDetector")


def patch_ragged_array_bug():
    """
    The vendored library returns `np.array(lanes_points)` / `np.array(lanes_detected)`
    without dtype=object, which raises a ValueError on newer numpy versions when the
    per-lane arrays have inconsistent lengths. Patch it in place, once.
    """
    target_file = os.path.join(LIB_DIR, "ultrafastLaneDetector.py")
    if not os.path.exists(target_file):
        raise FileNotFoundError(
            f"Could not find {target_file}. Did you vendor the library? See README.md setup steps."
        )

    with open(target_file, "r") as f:
        code = f.read()

    old = "return np.array(lanes_points), np.array(lanes_detected)"
    new = "return np.array(lanes_points, dtype=object), np.array(lanes_detected, dtype=object)"

    if old in code:
        code = code.replace(old, new)
        with open(target_file, "w") as f:
            f.write(code)
        print("Patched ragged-array bug in ultrafastLaneDetector.py")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--video", required=True, help="Path to input video")
    parser.add_argument("--weights", required=True, help="Path to tusimple_18.pth")
    parser.add_argument("--output", required=True, help="Path to write annotated output video")
    parser.add_argument(
        "--model-type", default="tusimple", choices=["tusimple", "culane"],
        help="Which pretrained config the weights correspond to",
    )
    args = parser.parse_args()

    patch_ragged_array_bug()

    sys.path.append(os.path.dirname(__file__))
    from ultrafastLaneDetector import UltrafastLaneDetector, ModelType

    model_type = ModelType.TUSIMPLE if args.model_type == "tusimple" else ModelType.CULANE
    print("Loading model...")
    lane_detector = UltrafastLaneDetector(args.weights, model_type)

    cap = cv2.VideoCapture(args.video)
    if not cap.isOpened():
        raise RuntimeError(f"Could not open video: {args.video}")

    fps = cap.get(cv2.CAP_PROP_FPS) or 30
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    os.makedirs(os.path.dirname(args.output), exist_ok=True)
    fourcc = cv2.VideoWriter_fourcc(*"mp4v")
    writer = cv2.VideoWriter(args.output, fourcc, fps, (width, height))

    print(f"Running inference on {args.video} ({total_frames} frames)...")
    with tqdm(total=total_frames) as pbar:
        while True:
            ret, frame = cap.read()
            if not ret:
                break
            output_frame = lane_detector.detect_lanes(frame)
            writer.write(output_frame)
            pbar.update(1)

    cap.release()
    writer.release()
    print(f"Done. Output written to {args.output}")


if __name__ == "__main__":
    main()
