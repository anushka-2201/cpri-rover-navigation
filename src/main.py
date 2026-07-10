import cv2
from segmentation import TerrainSegmenter
from centerline import CenterlineExtractor

def main():
    """
    Main pipeline to run the CPRI Rover perception system.
    """
    video_path = '../assets/lane_input_final.avi'
    model_path = '../models/best.pt'
    output_path = '../assets/lane_output_with_centerline.mp4'

    print("Initializing perception modules...")
    segmenter = TerrainSegmenter(model_path)
    extractor = CenterlineExtractor(step_size=15)

    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print(f"Error: Could not open video at {video_path}")
        return

    # Setup video writer
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

    print("Processing video frames...")

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        
        # Step 1: Get YOLO predictions for the current frame
        yolo_result = segmenter.predict_frame(frame)
        
        # Step 2: Extract mask data if drivable area is detected
        if yolo_result.masks is not None:
            # Extract the raw mask array from GPU/CPU memory
            mask_data = yolo_result.masks.data[0].cpu().numpy()
            
            # Step 3: Pass frame and mask to extract centerline
            processed_frame = extractor.extract(frame, mask_data)
        else:
            # If no drivable area is detected, use the raw frame
            processed_frame = frame
        
        # Write the processed frame to the output video
        out.write(processed_frame)

    cap.release()
    out.release()
    print(f"Processing complete! Output saved to: {output_path}")

if __name__ == "__main__":
    main()