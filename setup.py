from setuptools import find_packages, setup

package_name = 'my_robot'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='pranav_s',
    maintainer_email='pranav_s@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            "test_node=my_robot.my_first_node:main",
            "draw_circle=my_robot.draw_circle:main",
            "my_publisher=my_robot.my_publisher:main",
            "my_subscriber=my_robot.my_subscriber:main",
            "fibonacci_action_server=my_robot.fibonacci_action_server:main",
            "fibonacci_action_client=my_robot.fibonacci_action_client:main"
            
        ],
    },
)
