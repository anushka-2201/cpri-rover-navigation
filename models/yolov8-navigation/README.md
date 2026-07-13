# YOLOv8 Navigation

Object/path detection module for rover navigation using a custom-trained YOLOv8 model (`weights/best.pt`).

> **Draft — please correct.** This description was inferred from filenames only (`main.py`, `segmentation.py`, `centerline.py`, `visualizer.py`, `model.py`, `config.py`, `utils.py`). Replace this paragraph with an accurate description of what the module actually does — e.g. does it detect the drivable path/road segment, obstacles, or both? Does `centerline.py` compute a navigation line for the rover to follow from the segmentation output? Is this used together with the lane-detection models, or independently?

## Folder contents

```
yolov8-navigation/
├── main.py           # Entry point
├── config.py         # Configuration / parameters
├── model.py           # Model loading / architecture wrapper
├── segmentation.py    # Segmentation logic
├── centerline.py       # Centerline / path extraction
├── visualizer.py       # Output visualization
├── utils.py             # Shared helpers
└── weights/
    └── best.pt          # Trained YOLOv8 weights (gitignored — see data/datasets/README.md)
```

## Setup

```bash
pip install ultralytics opencv-python numpy
```
> Replace with the actual dependency list — check what `main.py` and `model.py` import.

## Run

```bash
python main.py --weights weights/best.pt --source ../../data/sample_inputs/<your_video>.mp4
```
> Replace with the actual CLI arguments `main.py` expects — check its `argparse` section.

## Training

> If `best.pt` was trained on a custom dataset (not a stock YOLOv8 checkpoint), document here: dataset size/source, classes, training config, and a link to the dataset (see `data/datasets/README.md`).
