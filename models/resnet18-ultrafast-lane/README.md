# ResNet-18 Lane Detection (Ultra-Fast-Lane-Detection)

CNN-based lane detection using [Ultra-Fast-Lane-Detection](https://github.com/cfzd/Ultra-Fast-Lane-Detection) (ResNet-18 backbone, pretrained on TuSimple), run via the [ibaiGorordo/Ultrafast-Lane-Detection-Inference-Pytorch](https://github.com/ibaiGorordo/Ultrafast-Lane-Detection-Inference-Pytorch) inference wrapper for clean video I/O.

This uses the **pretrained TuSimple checkpoint** — the model was not retrained from scratch, only used for inference on rover-captured video.

## Folder contents

```
resnet18-ultrafast-lane/
├── README.md
├── requirements.txt
├── run_inference.py       # Cleaned CLI script (derived from the original Colab notebook)
├── ultrafastLaneDetector/ # Vendored inference library (from ibaiGorordo's repo — see setup)
└── weights/               # tusimple_18.pth goes here (gitignored — see data/datasets/README.md)
```

## Setup

```bash
pip install -r requirements.txt

# Vendor the inference library (small, no heavy deps of its own)
git clone https://github.com/ibaiGorordo/Ultrafast-Lane-Detection-Inference-Pytorch ultrafastLaneDetector_src
mv ultrafastLaneDetector_src/ultrafastLaneDetector ./ultrafastLaneDetector
rm -rf ultrafastLaneDetector_src
```

Download `tusimple_18.pth` and place it at `weights/tusimple_18.pth` — see [`data/datasets/README.md`](../../data/datasets/README.md) for the link.

> Note: the original vendored library has a known bug where `lanes_points`/`lanes_detected` arrays raise a numpy ragged-array error on newer numpy versions. `run_inference.py` patches this automatically on first run (this replaces the manual `sed`-style fix that was done ad hoc in the notebook).

## Run

```bash
python run_inference.py \
  --video ../../data/videos/input/challenge_video.mp4 \
  --weights weights/tusimple_18.pth \
  --output ../../data/videos/output/resnet18/challenge_video_annotated.mp4 \
  --model-type tusimple
```

## Notes

This folder replaces a Colab notebook (`Resnet_18.ipynb`, kept in `notebooks/` for reference if you want) that cloned two separate GitHub repos, patched a library bug in-place, and used MoviePy to stitch frames back into a video. The logic is the same here, just as a single reusable script instead of sequential Colab cells.
