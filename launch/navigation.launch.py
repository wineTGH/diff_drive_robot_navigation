import os
from launch import LaunchDescription
from ament_index_python.packages import get_package_share_directory
from launch.substitutions import LaunchConfiguration
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.actions import IncludeLaunchDescription, DeclareLaunchArgument
def generate_launch_description():

    # Package name
    package_name='diff_drive_robot_navigation'
    nav2_params_file = os.path.join(get_package_share_directory(package_name),'config','nav2_params.yaml')

    # Launch configurations
    use_sim_time = LaunchConfiguration('use_sim_time')

    # Declare launch arguments
    declare_use_sim_time = DeclareLaunchArgument(
            'use_sim_time', default_value='false',
            description='Use sim time if true')

    # Launch Nav2 nodes
    nav2 = IncludeLaunchDescription(
                PythonLaunchDescriptionSource([os.path.join(
                    get_package_share_directory('nav2_bringup'),'launch','navigation_launch.py'
                )]), launch_arguments={'use_sim_time': use_sim_time, 'params_file': nav2_params_file}.items()
    )
    # Launch them all!
    return LaunchDescription([
        # Declare launch arguments
        declare_use_sim_time,

        # Launch the nodes
        nav2,
    ])