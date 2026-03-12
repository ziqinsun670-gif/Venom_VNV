import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource


def generate_launch_description():
    # Get package directories
    livox_driver_dir = get_package_share_directory('livox_ros_driver2')
    point_lio_dir = get_package_share_directory('point_lio')

    # Include Livox driver launch
    livox_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(livox_driver_dir, 'launch_ROS2', 'msg_MID360_launch.py')
        )
    )

    # Include Point-LIO mapping launch
    point_lio_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(point_lio_dir, 'launch', 'mapping.launch.py')
        )
    )

    return LaunchDescription([
        livox_launch,
        point_lio_launch,
    ])
