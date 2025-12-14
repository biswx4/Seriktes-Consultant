import rospy
from open_manipulator_msgs.srv import SetJointPosition
from open_manipulator_msgs.msg import JointPosition

class RobotArm:
    def __init__(self):
        rospy.wait_for_service('/open_manipulator/goal_joint_space_path')
        self.move = rospy.ServiceProxy('/open_manipulator/goal_joint_space_path', SetJointPosition)

    def move_joint(self, positions, time=2.0):
        req = SetJointPosition()
        req.joint_position.joint_name = ["joint1", "joint2", "joint3", "joint4"]
        req.joint_position.position = positions
        req.path_time = time
        self.move(req)

    def open(self):
        self.move_joint([0, 0, 0, -0.8])

    def close(self):
        self.move_joint([0, 0, 0, 0.2])

    def remove_object(self):
        self.close()
        self.move_joint([0.0, -0.6, 0.5, 0.0])
        self.open()
