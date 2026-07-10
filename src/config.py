import os

# Directory Paths
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODELS_DIR = os.path.join(BASE_DIR, "models")
ASSETS_DIR = os.path.join(BASE_DIR, "assets")

# File Paths
MODEL_PATH = os.path.join(MODELS_DIR, "best.pt")
INPUT_VIDEO_PATH = os.path.join(ASSETS_DIR, "lane_input_final.avi")
OUTPUT_VIDEO_PATH = os.path.join(ASSETS_DIR, "lane_output_with_centerline.mp4")

# Model Parameters
CONFIDENCE_THRESHOLD = 0.5
CENTERLINE_STEP_SIZE = 15

# Visualization Settings
CENTERLINE_COLOR = (0, 255, 0)  # Green color (BGR format)
CENTERLINE_THICKNESS = 3
MASK_OVERLAY_OPACITY = 0.4