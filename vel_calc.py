import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from my_pkg import posn_msg
from geometry_msgs.msg import Twist

target = [10,10,1]
trgtx = float(target[0])
trgty = float(target[1])
trgtyaw = float(target[2])

class velocitycalc(Node):
    def __init__(self):
        super().__init__('velcmd')

        # Create a subscriber for the calc_posn topic
        self.subscriber = self.create_subscription(posn_msg, 'calc_posn',self.timer_callback, 10)  #calc_posn is the topic
        # Log node initialization
        self.get_logger().info('Velocity calculator Node has been started.')
        self.publisher = self.create_publisher(Twist,'velcmd',10)

    def timer_callback(self,msg):
        vel_cmd = Twist()
        global x,y,z,r,p,y
        x = msg.x
        y = msg.y
        z = msg.z
        r = msg.r
        p = msg.p
        y = msg.y
    
        for i in enumerate(msg.name) :   
            error_l = trgtx-x
            vel_cmd.linear.x = error_l

            error_r = trgtyaw-y
            vel_cmd._angular.z = error_r/2
        self.publisher.publish(vel_cmd)
        
def main(args=None):
    # Initialize the rclpy library
    rclpy.init(args=args)

    # Create the VelocityController node
    node = velocitycalc()

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
