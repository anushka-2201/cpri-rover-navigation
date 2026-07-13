# CPRI Rover Navigation — Lane Detection

Lane detection pipeline for autonomous rover navigation, built and compared across three approaches of increasing complexity: classical computer vision (OpenCV), a CNN-based detector (ResNet-18 backbone / Ultra-Fast-Lane-Detection), and a transformer-style detector (CLRNet).

This repo documents the full progression — what was tried, how each one was run, and how they compare — with input/output video samples for each method.

## Approaches

| # | Method | Folder | Status |
|---|--------|--------|--------|
| 1 | Classical CV (OpenCV) | [`models/opencv-lane-detection`](models/opencv-lane-detection) | ✅ Working |
| 2 | ResNet-18 (Ultra-Fast-Lane-Detection, pretrained on TuSimple) | [`models/resnet18-ultrafast-lane`](models/resnet18-ultrafast-lane) | ✅ Working |
| 3 | CLRNet | [`models/clrnet`](models/clrnet) | 🚧 Environment set up, inference in progress |

> Update the status column as each method matures — this table is the first thing anyone reviewing the repo will read.

## Repo structure

```
cpri-rover-navigation/
├── models/
│   ├── opencv-lane-detection/     # Classical CV pipeline (camera calibration, thresholding, sliding window)
│   ├── resnet18-ultrafast-lane/   # Ultra-Fast-Lane-Detection, ResNet-18 backbone
│   └── clrnet/                    # CLRNet setup + inference
├── data/
│   ├── videos/
│   │   ├── input/                 # Raw source videos used to test all three methods
│   │   └── output/                # Annotated output videos, one subfolder per method
│   └── datasets/                  # Dataset notes / download links (TuSimple, etc.)
├── docs/
│   └── images/                    # Sample frames, diagrams, README screenshots
└── scripts/                       # Small shared utilities (e.g. frame extraction, video conversion)
```

Each `models/<method>/` folder is self-contained: its own README, its own `requirements.txt`, its own run script. You should be able to `cd` into any one of them and run it without needing the other two.

## Sample results

| Input | OpenCV | ResNet-18 | CLRNet |
|-------|--------|-----------|--------|
| ![input](docs/images/input_sample.gif) | ![opencv](docs/images/opencv_sample.gif) | ![resnet](docs/images/resnet_sample.gif) | *coming soon* |

> Replace these with actual GIFs/frames extracted from your output videos (see `scripts/make_gif.py` below). Short GIFs (a few seconds, <5MB) work far better in a README than linking full videos — GitHub renders them inline.

## Quick start

Each method is independent. Pick one:

```bash
# Classical CV
cd models/opencv-lane-detection
pip install -r requirements.txt
python run_pipeline.py --input ../../data/videos/input/challenge_video.mp4

# ResNet-18 / Ultra-Fast-Lane-Detection
cd models/resnet18-ultrafast-lane
pip install -r requirements.txt
python run_inference.py --video ../../data/videos/input/challenge_video.mp4 --weights weights/tusimple_18.pth

# CLRNet
cd models/clrnet
bash setup_environment.sh
```

See each subfolder's README for full details, including where to get model weights (not checked into git — see below).

## Datasets & weights

Large files (pretrained weights, full-length videos, training datasets) are **not** committed to this repo. See [`data/datasets/README.md`](data/datasets/README.md) for download links and expected paths. Small representative clips (a few seconds) are kept in `data/videos/` for quick testing.

## Why three approaches?

A short paragraph here explaining your reasoning — e.g. started with classical CV as a baseline (fast, no training data needed, but brittle to lighting/curves), moved to ResNet-18-based detection for more robustness, then explored CLRNet for further accuracy gains. This context is what makes the repo read as a project rather than a folder of scripts — write 3-4 sentences here.

## License

Add a license (MIT is a common default for this kind of project) — see `LICENSE`.
