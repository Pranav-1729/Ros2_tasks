from launch import LaunchDescription
from launch_ros.actions import Node

#launch this file to print tf info

def generate_launch_description():
    return LaunchDescription([
        Node(
            package = 'tf2_ros',
            executable = 'static_transform_publisher',
            arguments = ['0', '0', '1', '0', '0', '0', 'world', 'link1'],
        ),
#publishes a static transform between the world frame and link1 frame, first 3 args are translational
#next 3 are rotnl then parent frame then child frame
#used for fixed relationships
#the tf2_ros pkg is idk where

        Node(
            package = 'my_pkg',
            executable = 'frame_tf2_broadcaster',
            parameters = [
                {
                    'parent_frame_name': 'link1',
                    'child_frame_name': 'link2',
                }
            ]
        ),

# Launches a custom dynamic transform broadcaster from your package my_pkg. just starts a node, that broadcasts

        Node(
            package = 'my_pkg',
            executable = 'tf2_listener',
            parameters = [
                {
                    'from_frame': 'world',
                    'to_frame': 'link2',
                }
            ],
        ),
    ])
