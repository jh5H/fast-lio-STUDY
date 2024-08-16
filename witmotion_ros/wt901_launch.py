
import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration


def generate_launch_description():
    ld = LaunchDescription()
    logger = LaunchConfiguration("log_level")
    log_level_arg = DeclareLaunchArgument("log_level",
                          default_value=["debug"],
                          description="logging level")


    config = os.path.join(
        get_package_share_directory('witmotion_ros'),
        'config',
        'wt901.yml'
        )
        
    node=Node(
        package = 'witmotion_ros',
        executable = 'witmotion_ros_node',
        parameters = [config],
        arguments = ['--ros-args', '--log-level', logger],
        emulate_tty = True
    )

    ld.add_action(log_level_arg)
    ld.add_action(node)
    return ld