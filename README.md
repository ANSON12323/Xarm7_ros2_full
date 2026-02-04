<h1 align="center">🤖 XArm7 ROS 2 Full</h1>

<p align="center">
  <b>A Complete Standalone Package for ROS 2 Jazzy</b>
  <br><br>
  <img src="https://img.shields.io/badge/ROS_2-Jazzy-blue?logo=ros&logoColor=white" alt="ROS 2 Jazzy" />
  <img src="https://img.shields.io/badge/Build-Colcon-orange" alt="Build Status" />
  <img src="https://img.shields.io/badge/License-MIT-green" alt="License" />
  <br><br>
  XArm7 ROS 2 Full provides description files, MoveIt 2 configurations, and C++ interfaces to simulate and control the XArm7 manipulator.
</p>

---

## 📦 Package Overview

| Package | Description |
| :--- | :--- |
| **`xarm7`** | Contains URDFs, meshes, and basic launch files. |
| **`xarm7_bringup`** | Launch files to start robot drivers and simulation environments. |
| **`xarm7_moveit`** | **MoveIt 2** configuration for motion planning and collision checking. |
| **`xarm7_commander_cpp`** | C++ interface for controlling the manipulator programmatically. |
| **`xarm7_interfaces`** | Custom ROS 2 messages and services. |

---

### 📂 File Tree
```text
Xarm7_ros2_full/
├── xarm7/
│   ├── urdf/          # Robot model files
│   ├── meshes/        # Visualization assets
│   └── launch/        # Base launch files
├── xarm7_bringup/
│   ├── launch/        # Gazebo/Driver configs
│   └── config/        # Controller YAMLs
├── xarm7_moveit/
│   ├── config/        # Planning configs
│   └── launch/        # MoveIt runtime
└── xarm7_commander_cpp/
    ├── src/           # Source code
    └── include/       # Headers

---

### 🛠️ BUild Package
**🚀 How to Run the Simulation**
1️⃣ Installation & Build
First, ensure your environment is set up. This project is optimized for ROS 2 Jazzy.

Bash
# Navigate to your workspace
cd ~/ros2_ws

# Clone repository
git clone <YOUR_REPO_LINK> src/xarm7_ros2_full

# Install dependencies
rosdep install -i --from-path src --rosdistro jazzy -y

# Build the workspace
colcon build --symlink-install
source install/setup.bash

```
### Execution (3 Terminals)

**Terminal 1: Launch Simulation**

```bash
ros2 launch xarm7_bringup display.launch.xml

```

**Terminal 2: Run Commander**

```bash
ros2 run xarm7_commander_cpp commander_cpp

```

**Terminal 3: Robot Commands**
*Use the commands below to control the robot.*

### Option 1: Joint Command

*Send an array of 7 float values to 7 joints.*

```bash
ros2 topic pub -1 /joint_command example_interfaces/msg/Float64MultiArray "{data: [0.0, 0.0, 0.0, 1.5, 0.0, 0.0, 0.0]}"

```

### Option 2: Joint Trajectory

*Send a trajectory with Trajectory Controller.*

```bash
ros2 topic pub -1 /arm_controller/joint_trajectory trajectory_msgs/msg/JointTrajectory "{
  joint_names: ['joint1','joint2','joint3','joint4','joint5','joint6','joint7'],
  points: [
    {
      positions: [0.5, -0.3, 0.2, 0.0, 0.0, 0.0, 0.0],
      time_from_start: {sec: 2}
    }
  ]
}"

```

### Option 3: Pose Command

*Send a Cartesian target (x, y, z, roll, pitch, yaw).*

```bash
ros2 topic pub -1 /pose_command xarm7_interfaces/msg/PoseCommand "{x: 0.2, y: 0.0, z: 0.6, roll: 3.14, pitch: 0.0, yaw: 0.0, cartesian_path: false}"

```

---

## 🛠 Debugging

```bash
# List all active topics
ros2 topic list

# Get info on a specific topic
ros2 topic info /<topic_name>

# Check active controllers
ros2 control list_controllers

```

```
Have fun playing with Xarm7!
