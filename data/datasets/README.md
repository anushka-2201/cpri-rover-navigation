# Datasets & pretrained weights

Large files are not committed to this repo (GitHub blocks files over 100MB, and repo bloat makes cloning slow). This file is the single source of truth for where to get everything.

## Pretrained weights

| File | Used by | Source |
|------|---------|--------|
| `tusimple_18.pth` | `models/resnet18-ultrafast-lane` | [Ultra-Fast-Lane-Detection releases](https://github.com/cfzd/Ultra-Fast-Lane-Detection) — see repo README for the Google Drive / OneDrive link |
| CLRNet checkpoint | `models/clrnet` | TBD — add once you've picked one from [CLRNet's model zoo](https://github.com/Turoad/CLRNet) |

Place each at the path referenced in its model folder's README (e.g. `models/resnet18-ultrafast-lane/weights/tusimple_18.pth`).

## Datasets

Both pretrained models were trained on **TuSimple** — this project uses the pretrained checkpoints for inference only; no retraining was done. If you later fine-tune on your own rover footage, document that dataset here: size, source, split, and a download link (Google Drive / a GitHub Release, not committed directly to git).

## Camera calibration images

`models/opencv-lane-detection/camera_cal/` — chessboard images used for OpenCV camera calibration. These are small (a few KB each) and fine to commit directly.

Full videos are hosted externally https://drive.google.com/drive/folders/1GxR3JKEmpcuys9-uKjbMnamZU6IxpULF?usp=sharing and only short representative clips (a few seconds, <10MB) are committed under `data/sample_inputs/` and `data/sample_outputs/` for quick testing and for the README GIFs.
