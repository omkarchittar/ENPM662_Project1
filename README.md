# **ENPM Project 1 (CHOMS)**

## **File Tree**

```text
ochittar_Project1
+-Assembly
|
+-Package
|   +-CHOMS
|       +-10 directories
+-Videos
|   +-Project1_circle.mkv
|   +-Project1_Rviz.mkv
|   +-Project1_teleop.mkv
+-README.md
+-Project1_report.pdf
```

## **Installation**

1. Download and extract the files.
2. The folder Package consists of a ROS Package.
3. Copy the package into your workspace and build it using the following command in your terminal

   ```bash
   cd ~/catkin_ws/

   catkin_make
   ```

4. Don't forget to source your files.

   ```bash
   source devel/setup.bash
   ```

   if you are using zsh

   ```bash
   source devel/setup.zsh
   ```

## **Running**

### 1. Teleop

Open a terminal and launch the `template_teleop.launch` file.

```bash
roslaunch CHOMS template_teleop.launch
```

This will launch a gazebo world with the robot in it.

To control the robot using teleop open a new terminal and launch the `teleop_template.py` node.

```bash
rosrun CHOMS teleop_template.py
```

The node will display a message on how to control the robot as shown below.

```bash
Control Your Toy!
---------------------------
Moving around:
   u    i    o
   j    k    l
   m    ,    .
q/z : increase/decrease max speeds by 10%
w/x : increase/decrease only linear speed by 10%
e/c : increase/decrease only angular speed by 10%
space key, k : force stop
anything else : stop smoothly
CTRL-C to quit
```


### 2. Circle

Open a terminal and launch the `circle.launch` file.

```bash
roslaunch CHOMS circle.launch
```

This will launch an empty gazebo world and spawn the robot in its center.

Open another terminal and launch the `circle.py` node.

```bash
rosrun CHOMS circle.py
```

This node will publish commands to the robot to move in a circular loop. It also publishes the values to the terminal.

In a new terminal run the `sub.py` node.

```bash
rosrun CHOMS sub.py
```

This node subscribes to the robot commands that are being published and displays them on the terminal.


### Credits

This project was made by

- Omkar Chittar (ochittar@umd.edu / omkar.chittar@gmail.com)
- Kshitij Karnawat (kshitij@umd.edu / kshitijkarnawat009@gmail.com)

