# 🚙 Vision-Based Autonomous Rover Navigation and Path Planning using Deep Learning

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![YOLOv8/11](https://img.shields.io/badge/YOLO-Segmentation-orange)
![ResNet18](https://img.shields.io/badge/ResNet-18-yellow)
![CLRNet](https://img.shields.io/badge/CLRNet-Lane_Detection-red)
![OpenCV](https://img.shields.io/badge/OpenCV-Vision-green)

## 📌 Project Overview
This project focuses on developing a robust, vision-based autonomous navigation system for a rover capable of real-time path perception and navigation. The primary objective is to create a perception pipeline that accurately identifies drivable boundaries and navigates complex, unstructured environments by processing monocular camera feeds[cite: 2].


## 🚀 Technical Journey & Implementation Phases

My approach to solving this autonomous navigation challenge evolved through multiple phases, transitioning from traditional computer vision to state-of-the-art deep learning segmentation:

### Phase 1: Foundations in Traditional Computer Vision (OpenCV)
*   **Approach:** Implemented traditional image processing techniques using OpenCV[cite: 2].
*   **Techniques:** Developed a pipeline including perspective transformation (bird's-eye view mapping) and sliding-window-based lane detection[cite: 2]. Applied histogram-based pixel identification and fitted second-order polynomials to lane boundaries[cite: 2].
*   **Outcome & Limitations:** Achieved a fundamental understanding of spatial mapping, but the methods lacked robustness against occlusions, dynamic road textures, and varying lighting conditions[cite: 2].

### Phase 2: Transitioning to Deep Learning (ResNet-18)
*   **Approach:** Transitioned to a ResNet-18-based architecture for semantic segmentation to overcome hand-crafted feature limitations[cite: 2].
*   **Outcome & Limitations:** Significantly improved boundary classification by learning complex feature representations directly from data[cite: 2]. However, challenges persisted with high-curvature paths and temporal stability in high-latency video feeds[cite: 2].

### Phase 3: High-Fidelity Lane Detection (CLRNet)
*   **Approach:** Explored the Cross-Layer Refinement Network (CLRNet) utilizing multi-scale feature interaction to address complex curves[cite: 2].
*   **Outcome & Limitations:** Proved highly accurate for structured environments with explicit painted lines (e.g., highways)[cite: 2]. Realized that semi-structured or unstructured environments (like campus paths) required a shift from strict "lane detection" to full "drivable area segmentation"[cite: 2].

### Phase 4: Drivable Area Segmentation & Control Integration (Current Focus)
*   **Approach:** Implementing state-of-the-art YOLO-based segmentation models (YOLOv8/YOLO11-seg)[cite: 2]. 
*   **Implementation:** Fine-tuning the model on custom-annotated datasets to predict pixel-accurate binary masks of the entire drivable path[cite: 2].
*   **Control Integration:** The pipeline processes these binary masks to extract a dynamic centerline in real-time, effectively translating visual perception into actionable steering parameters for the rover's path-following controller[cite: 2].

---


## 📁 Repository Structure 
*(Note: Code modules are currently being added and structured based on the further progress)*

```text
├── notebooks/
│   ├── 01_traditional_cv_opencv.ipynb     # Phase 1: Sliding window & perspective transform
│   ├── 02_resnet18_segmentation.ipynb     # Phase 2: Semantic segmentation experiments
│   └── 03_clrnet_lane_detection.ipynb     # Phase 3: High-fidelity lane detection on structured roads
├── src/
│   ├── model.py                           # YOLO segmentation initialization
│   ├── centerline.py                      # Real-time dynamic centerline extraction logic
│   └── utils.py                           # Helper functions for mask processing
└── README.md
