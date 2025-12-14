from ultralytics import YOLO
import cv2

class ObstacleDetector:
    def __init__(self):
        self.model = YOLO("yolov8n.pt")

    def detect(self, frame):
        return self.model(frame)

    def is_obstacle(self, frame):
        results = self.detect(frame)
        for box in results[0].boxes:
            return True
        return False
