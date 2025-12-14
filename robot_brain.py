from obstacle_detection import ObstacleDetector
from arm_controller import RobotArm
from motor_controller import MotorController
import cv2

class RobotBrain:
    def __init__(self):
        self.detector = ObstacleDetector()
        self.arm = RobotArm()
        self.motors = MotorController()
        self.cam = cv2.VideoCapture(0)

    def run(self):
        while True:
            ret, frame = self.cam.read()
            if not ret:
                continue

            if self.detector.is_obstacle(frame):
                print("Object detected")
                self.motors.stop()
                self.arm.remove_object()
            else:
                self.motors.forward()
