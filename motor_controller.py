import time

class Motor:
    def __init__(self, name):
        self.name = name
        self.speed = 0

    def setSpeed(self, speed):
        self.speed = speed
        print(f"Motor {self.name} => {speed}")

class MotorController:
    def __init__(self):
        self.left = Motor("left")
        self.right = Motor("right")

    def forward(self, speed=200):
        self.left.setSpeed(speed)
        self.right.setSpeed(speed)

    def stop(self):
        self.left.setSpeed(0)
        self.right.setSpeed(0)

    def turn_left(self, speed=150):
        self.left.setSpeed(-speed)
        self.right.setSpeed(speed)

    def turn_right(self, speed=150):
        self.left.setSpeed(speed)
        self.right.setSpeed(-speed)
