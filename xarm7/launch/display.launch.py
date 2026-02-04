import os
from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import Command, LaunchConfiguration

from launch_ros.actions import Node
from launch_ros.parameter_descriptions import ParameterValue


def generate_launch_description():
    arduinobot_description_dir = get_package_share_directory("xarm7")

    model_arg = DeclareLaunchArgument(name="model", default_value=os.path.join(
                                        arduinobot_description_dir, "urdf", "xarm7.urdf.xacro"),
                                      description="Absolute path to robot urdf file")
    print(model_arg)
    #we will get this path /home/anson/arduinobot_ws/src/arduinobot_description/urdf/arduinobot.urdf.xacro

    robot_description = ParameterValue(Command(["xacro ", LaunchConfiguration("model")]),
                                       value_type=str)
    #converting xacro model to plain urdf model

    robot_state_publisher_node = Node(
        package="robot_state_publisher",
        executable="robot_state_publisher",
        parameters=[{"robot_description": robot_description}]
    )

    joint_state_publisher_gui_node = Node(
        package="joint_state_publisher_gui",
        executable="joint_state_publisher_gui"
    )

    rviz_node = Node(
        package="rviz2",
        executable="rviz2",
        name="rviz2",
        output="screen",
        arguments=["-d", os.path.join(arduinobot_description_dir, "rviz", "urdf_config.rviz")],
    )

    return LaunchDescription([
        model_arg,
        joint_state_publisher_gui_node,
        robot_state_publisher_node,
        rviz_node
    ])
