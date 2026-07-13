import cv2
import numpy as np

class PerceptionVisualizer:
    def __init__(self, overlay_opacity=0.4):
        """
        Initializes the visualizer with a customizable mask overlay opacity.
        """
        self.overlay_opacity = overlay_opacity

    def overlay_segmentation_mask(self, frame, mask, color=(255, 0, 0)):
        """
        Overlays a semi-transparent colored mask onto the drivable terrain area.
        """
        height, width = frame.shape[:2]
        mask_resized = cv2.resize(mask, (width, height))
        
        # Create a colored mask layer
        colored_mask = np.zeros_like(frame, dtype=np.uint8)
        colored_mask[mask_resized > 0.5] = color
        
        # Blend the original frame with the colored mask layer
        blended_frame = cv2.addWeighted(frame, 1.0, colored_mask, self.overlay_opacity, 0)
        return blended_frame

    def add_telemetry_data(self, frame, status="Autonomous Navigation", fps=None):
        """
        Adds professional text overlays and system status onto the frame.
        """
        cv2.putText(frame, f"SYSTEM STATUS: {status}", (20, 40), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 255), 2, cv2.LINE_AA)
        if fps is not None:
            cv2.putText(frame, f"FPS: {fps}", (20, 70), 
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 255), 2, cv2.LINE_AA)
        return frame