# CLRNet Lane Detection

Third approach explored — [CLRNet](https://github.com/Turoad/CLRNet), a transformer-informed lane detector, evaluated as a potential accuracy upgrade over the ResNet-18 baseline.

**Status: environment set up and build issues resolved; inference on rover video not yet run/committed.** Being upfront about this in the README is better than implying it's finished — fill in the "Run" section once you have a working inference script.

## What's in this folder

```
clrnet/
├── README.md
├── setup_environment.sh    # Reproduces the environment setup + build fixes from the original notebook
└── CLRNet/                 # (gitignored) cloned CLRNet source lives here after running setup
```

## Setup

```bash
bash setup_environment.sh
```

This script clones CLRNet and works through the build issues that came up (torch/torchvision version conflicts in `requirements.txt`, `sklearn` → `scikit-learn` rename, and two C++/CUDA source fixes needed for the custom NMS op to compile against a newer PyTorch: `.type()` → `.scalar_type()` and `AT_CHECK` → `TORCH_CHECK`).

## Next steps

- [ ] Confirm `python setup.py build develop` completes cleanly end-to-end
- [ ] Download a CLRNet checkpoint (pretrained on TuSimple or CULane) and add the path to `data/datasets/README.md`
- [ ] Write `run_inference.py` (mirror the structure of `models/resnet18-ultrafast-lane/run_inference.py`) using CLRNet's `demo`/`tools/detect.py` entry point
- [ ] Run on `data/videos/input/` and save results to `data/videos/output/clrnet/`
- [ ] Update the status line above and the comparison table in the top-level README
