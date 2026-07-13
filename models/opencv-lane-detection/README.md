# Classical CV Lane Detection (OpenCV)

Baseline lane detection pipeline using classical computer vision — no neural network, no training data required. Originally forked and adapted from [thisisbhavin/Advanced-lane-detection-using-OpenCV](https://github.com/thisisbhavin/Advanced-lane-detection-using-OpenCV).

## Pipeline

1. **Camera calibration** — compute the camera matrix and distortion coefficients from a set of chessboard images (`camera_cal/`).
2. **Distortion correction** — undistort each raw frame.
3. **Thresholding** — combine color transforms (HLS) and gradient (Sobel) thresholds into a binary image that isolates lane-line pixels.
4. **Perspective transform** — warp the binary image to a bird's-eye view.
5. **Lane pixel detection** — sliding-window search on the first frame, then a margin-based search around the previous fit for subsequent frames.
6. **Curve fit** — fit a 2nd-degree polynomial to each lane line; compute radius of curvature and vehicle offset from lane center.
7. **Unwarp + overlay** — project the fitted lane back onto the original frame.

## Folder contents

```
opencv-lane-detection/
├── README.md
├── requirements.txt
├── run_pipeline.py          # CLI entry point — run on an image or a video
├── lane_detection/          # Pipeline code (calibration, thresholding, perspective transform, fitting)
├── camera_cal/              # Chessboard calibration images
└── test_images/             # A few sample frames for quick testing
```

> This is where you move your forked repo's actual code into. Keep the calibration images and any small test images — drop large output videos into `data/videos/output/opencv/` at the repo root instead (see `.gitignore`).

## Setup

```bash
pip install -r requirements.txt
```

`requirements.txt`:
```
opencv-python
numpy
moviepy
matplotlib
```

## Run

```bash
python run_pipeline.py --input ../../data/videos/input/challenge_video.mp4 \
                        --output ../../data/videos/output/opencv/challenge_video_annotated.mp4
```

## Known limitations

Classical thresholding is sensitive to lighting changes, shadows, and road-surface cracks — this is the main motivation for moving to the learned approaches in `models/resnet18-ultrafast-lane` and `models/clrnet`. Note any specific failure cases you observed here.
