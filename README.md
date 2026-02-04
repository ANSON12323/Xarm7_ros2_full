Xarm7_ros2_full-A Complete standalone package of Xarm7 for ROS2 Jazzy

Consists of the following packages
1.Xarm7-Which is basically the description package, contains the urdf, meshes, launch files
2.xarm7_bringup: Launch files and configurations to easily start up the robot drivers and simulation environments.
3.xarm7_moveit: Full MoveIt 2 configuration for motion planning, collision checking, and trajectory execution.
4.xarm7_commander_cpp: C++ interface and examples for sending commands and controlling the manipulator programmatically.
5.xarm7_interfaces: Custom ROS 2 messages and service definitions required for communication.


How to run the simulation!
For running the simulation use the following steps

1.Downlaod/Clone all the packages inside the workspace/src folder
2.Build using Colcon build
3.Source the bash file
4.open 3 terminals
5.1st terminal
  ros2 launch xarm7_bringup display.launch.xml
6.2nd terminal
  ros2 run xarm7_commander_cpp commander_cpp
7.3rd terminal
  We can use 3 topics to send the commmands to the robot
  1.Joint Command
  2.Joint Trajectory
  3.Pose Command

  
  1.Joint Command
  ros2 topic pub -1 /joint_command example_interfaces/msg/Float64MultiArray "{data: [0.0, 0.0, 0.0, 1.5, 0.0, 0.0, 0.0]}"

  2.joint trajectory
  ros2 topic pub -1 /arm_controller/joint_trajectory trajectory_msgs/msg/JointTrajectory "{
    joint_names: ['joint1','joint2','joint3','joint4','joint5','joint6','joint7'],
    points: [
      {
        positions: [0.5, -0.3, 0.2, 0.0, 0.0, 0.0, 0.0],
        time_from_start: {sec: 2}
      }
    ]
    }"

  3.pose command
  ros2 topic pub -1 /pose_command xarm7_interfaces/msg/PoseCommand "{x: 0.2, y: 0.0, z: 0.6, roll: 3.14, pitch: 0.0, yaw: 0.0, cartesian_path: false}"


  Debugging commands
  1.ros2 topic list
  2.ros2 topic info /<topic_name>
  3.ros2 controller list_controllers

