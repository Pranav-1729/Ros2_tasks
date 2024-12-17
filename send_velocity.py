#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
# import sys
# import termios
# import tty
# import time
# only rz is to be used for rotation, +ve fr left and _ve for right, and only vx is needed

# def read_data(file_name):
#     float_data = []
#     try:
#         with open(file_name, 'r') as file:
#             for line in file:
#                 line = line.strip()  # Remove leading/trailing whitespace
#                 if line:  # Check if the line is not empty
#                     try:
#                         float_data.append(float(line))
#                     except ValueError:
#                         raise ValueError(f"Non-float data found: '{line}' in file {file_name}")
#     except FileNotFoundError:
#         raise FileNotFoundError(f"File '{file_name}' not found.")
#     return float_data  #returns a list

class VelocityController(Node):
    def __init__(self):
        super().__init__('send_velocity')

        # Create a publisher for the /cmd_vel topic
        self.publisher = self.create_publisher(Twist, '/cmd_vel', 10)
        # Set the publishing rate (1 Hz)
        self.timer = self.create_timer(1.0, self.timer_callback)
        # Log node initialization
        self.get_logger().info('Velocity Controller Node has been started.')
        self.subscriber = self.create_subscription(Twist, 'velcmd',self.timer_callback1, 10)

    def timer_callback1(self,msg):
        global x
        x=msg.linear.x
        global rz
        rz=msg.angular.z
        # Create a Twist message
        # velocity_msg = Twist()
        # Set linear and angular velocities
        # vel_data =read_data("vel_input.txt")
        # vx = float(vel_data[0])
        # rz = float(vel_data[1])
        # velocity_msg.linear.x = vx  # Forward velocity in m/s
        # velocity_msg.angular.z = rz  # Angular velocity in rad/s

    def timer_callback(self):
        velfinal = Twist()
        velfinal.linear.x =x
        velfinal.angular.z = rz
        self.publisher.publish(velfinal)

def main(args=None):
    # Initialize the rclpy library
    rclpy.init(args=args)

    # Create the VelocityController node
    node = VelocityController()

    # Spin the node (keep it running)
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass

    # Shutdown the node
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()




# class CustomTeleopTwist(Node):

#     def __init__(self):
#         super()._init_('custom_teleop_twist')
#         self.publisher_ = self.create_publisher(Twist, 'cmd_vel', 10)
#         self.twist = Twist()
#         self.twist.linear.x = 0.0
#         self.twist.linear.y = 0.0
#         self.twist.linear.z = 0.0
#         self.twist.angular.x = 0.0
#         self.twist.angular.y = 0.0
#         self.twist.angular.z = 0.0

#     def run(self):
#         settings = termios.tcgetattr(sys.stdin)
#         try:
#             while True:
#                 key = self.get_key(settings)
#                 if key == 'w':
#                     self.twist.linear.x += 1
#                     # time.sleep(1)
#                     # self.twist.linear.x=0
                
#                 elif key == 's':
#                     self.twist.linear.x -= 1
#                 elif key == 'a':
#                     self.twist.angular.z = 1
#                 elif key == 'd':
#                     self.twist.angular.z -= 1
#                 elif key == '\x03':  # Ctrl+C
                
#                     break
#                 print(self.twist)
#                 self.publisher_.publish(self.twist)
#         finally:
#             termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)

#     def get_key(self, settings):
#         tty.setraw(sys.stdin.fileno())
#         key = sys.stdin.read(1)
#         termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
#         return key

# def main(args=None):
#     rclpy.init(args=args)
#     node = CustomTeleopTwist()
#     node.run()
#     node.destroy_node()
#     rclpy.shutdown()

# if __name__ == '_main_':
#     main()