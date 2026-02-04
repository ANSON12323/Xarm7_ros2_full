cmake_minimum_required(VERSION 3.8)
project(xarm7_commander_cpp)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# find dependencies
find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)
find_package(rcl_interfaces REQUIRED)
find_package(moveit_ros_planning_interface REQUIRED)
find_package(example_interfaces REQUIRED)
find_package(std_msgs REQUIRED)
find_package(xarm7_interfaces REQUIRED)

add_executable(test_cpp src/test_moveit.cpp)
ament_target_dependencies(test_cpp rclcpp std_msgs moveit_ros_planning_interface)

add_executable(commander_cpp src/commander_template.cpp)
ament_target_dependencies(commander_cpp rclcpp std_msgs moveit_ros_planning_interface example_interfaces xarm7_interfaces)

install(TARGETS
  test_cpp
  commander_cpp
  DESTINATION lib/${PROJECT_NAME}/
)

ament_package()
