#!/usr/bin/env bash
# Sets up the CLRNet environment and works through the build issues encountered
# during initial setup (captured from the original Colab notebook).
set -e

if [ ! -d "CLRNet" ]; then
  git clone https://github.com/Turoad/CLRNet.git
fi
cd CLRNet

# torch/torchvision from CLRNet's requirements.txt conflict with a modern
# environment's already-installed versions — strip them and install the rest.
sed -i '/torch/d' requirements.txt
sed -i '/torchvision/d' requirements.txt
pip install -r requirements.txt

# requirements.txt references the deprecated PyPI name "sklearn"
sed -i 's/sklearn/scikit-learn/g' requirements.txt
pip install -r requirements.txt

# First build attempt — will likely fail on the custom NMS CUDA op with newer PyTorch.
python setup.py build develop || true

# Fix 1: .type() -> .scalar_type() (removed in newer PyTorch/ATen)
sed -i 's/\.type()/.scalar_type()/g' clrnet/ops/csrc/*.cu
sed -i 's/\.type()/.scalar_type()/g' clrnet/ops/csrc/*.cpp

# Fix 2: AT_CHECK -> TORCH_CHECK (renamed in newer PyTorch)
sed -i 's/AT_CHECK/TORCH_CHECK/g' clrnet/ops/csrc/*.cpp
sed -i 's/AT_CHECK/TORCH_CHECK/g' clrnet/ops/csrc/*.cu

python setup.py build develop

echo "CLRNet environment set up. See README.md 'Next steps' for what's left to do."
