#use ros 2 humble  base image
FROM ros:humble

#prevent package prompts from blocking installation
ENV DEBIAN_FRONTEND=noninteractive


#update and install the following: Rviz tool, demo nodes cpp and python, clean up package lists
RUN apt update && apt install -y \
    python3-colcon-common-extensions \
    ros-humble-rviz2 \
    ros-humble-demo-nodes-cpp \
    ros-humble-demo-nodes-py \
    ros-humble-tf2-ros \
    ros-humble-geometry-msgs \
    ros-humble-visualization-msgs \
    && rm -rf /var/lib/apt/lists/*


#create catkin/colcon workspace
RUN mkdir -p /ros2_ws/src

#sets working directory inside container
WORKDIR /ros2_ws

#ensure ros 2 environment is loaded when shell is started
RUN echo "source /opt/ros/humble/setup.bash" >> /root/.bashrc
