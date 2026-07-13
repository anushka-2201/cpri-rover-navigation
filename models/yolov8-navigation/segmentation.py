from ultralytics import YOLO

class TerrainSegmenter:
    def __init__(self, model_path):
    
        self.model = YOLO(model_path)

    def predict_frame(self, frame):
        
        results = self.model.predict(source=frame, show_labels=False, verbose=False)
        return results[0]