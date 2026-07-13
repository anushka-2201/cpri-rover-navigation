# CPRI Rover Navigation

Perception stack for autonomous rover navigation: lane detection (three approaches, compared) and YOLOv8-based navigation/obstacle detection.

## Modules

| Module | What it does | Folder | Status |
|--------|--------------|--------|--------|
| Lane detection — OpenCV | Classical CV pipeline (camera calibration, thresholding, sliding window) | [`models/opencv-lane-detection`](models/opencv-lane-detection) | ✅ Working |
| Lane detection — ResNet-18 | Ultra-Fast-Lane-Detection, pretrained on TuSimple | [`models/resnet18-ultrafast-lane`](models/resnet18-ultrafast-lane) | ✅ Working |
| Lane detection — CLRNet | Transformer-informed lane detector | [`models/clrnet`](models/clrnet) | 🚧 Environment set up, inference not yet run |
| YOLOv8 navigation | Custom-trained YOLOv8 for path/obstacle detection | [`models/yolov8-navigation`](models/yolov8-navigation) | ✅ Working — README still needs a real description, see below |

> Update this table's status column as CLRNet progresses and once the yolov8-navigation description is filled in.

## Repo structure

```
cpri-rover-navigation/
├── models/
│   ├── opencv-lane-detection/     # Classical CV lane detection
│   ├── resnet18-ultrafast-lane/   # ResNet-18 lane detection (Ultra-Fast-Lane-Detection)
│   ├── clrnet/                    # CLRNet lane detection (in progress)
│   └── yolov8-navigation/         # YOLOv8-based navigation module
├── data/
│   ├── sample_inputs/             # Short input videos/images used to test all modules
│   ├── sample_outputs/            # Generated output videos (gitignored — regenerate locally)
│   └── datasets/                  # Dataset notes + download links for weights/datasets
├── docs/
│   └── images/                    # README screenshots/GIFs
└── scripts/                       # Shared utilities (e.g. make_gif.py)
```

Each `models/<name>/` folder is self-contained: its own README, its own dependencies, its own run script — you can `cd` into any one and run it without the others.

## Why three lane-detection approaches?

This project explores lane detection at increasing levels of complexity: classical CV as a fast, no-training-data-needed baseline; ResNet-18 (Ultra-Fast-Lane-Detection) for more robustness to lighting and curves; and CLRNet as a further accuracy upgrade still being evaluated.

> Replace this paragraph with your own reasoning/observations — e.g. what specific failure cases pushed you from OpenCV to ResNet, and what CLRNet was expected to improve on. This is the part that makes the repo read as a project with a story, not just a folder of scripts.

## Quick start

```bash
# OpenCV lane detection
cd models/opencv-lane-detection
# see README.md in this folder for exact run command

# ResNet-18 lane detection
cd models/resnet18-ultrafast-lane
pip install -r requirements.txt
python run_inference.py --source ../../data/sample_inputs/challenge_video.mp4 \
                         --weights weights/tusimple_18.pth \
                         --output ../../data/sample_outputs/resnet_result.mp4

# YOLOv8 navigation
cd models/yolov8-navigation
# see README.md in this folder for exact run command (still being finalized)
```

## Datasets & weights

Large files (pretrained weights, full-length videos) are not committed directly — see [`data/datasets/README.md`](data/datasets/README.md) for download links and expected file paths.

## License

Add a license (MIT is a common default) — see `LICENSE`.
