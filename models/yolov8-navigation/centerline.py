import cv2
import numpy as np

class CenterlineExtractor:
    def __init__(self, step_size=15, line_color=(0, 255, 0), line_thickness=3):
        """
        Initializes the CenterlineExtractor with configurable parameters.
        """
        self.step_size = step_size
        self.line_color = line_color
        self.line_thickness = line_thickness

    def extract(self, frame, mask):
        """
        Takes the original frame and the segmentation mask, calculates the centerline,
        and draws it on the frame.
        """
        height, width = frame.shape[:2]

        # Resize the mask to match the original frame dimensions
        mask_resized = cv2.resize(mask, (width, height))
        
        center_points = []
        
        # Scan the mask horizontally based on the defined step size
        for y in range(0, height, self.step_size):
            row = mask_resized[y, :]
            road_pixels = np.where(row > 0.5)[0]
            
            if len(road_pixels) > 0:
                left_edge = road_pixels[0]
                right_edge = road_pixels[-1]
                
                # Calculate the midpoint to establish the center of the drivable path
                center_x = int((left_edge + right_edge) / 2)
                center_points.append((center_x, y))
        
        # Draw the extracted centerline directly onto the original frame
        for i in range(len(center_points) - 1):
            pt1 = center_points[i]
            pt2 = center_points[i + 1]
            cv2.line(frame, pt1, pt2, self.line_color, thickness=self.line_thickness)
            
        return frame