---
sidebar_position: 5
---

# URDF Basics for Humanoids: Defining the Robotic Anatomy

## Understanding URDF (Unified Robot Description Format)

URDF serves as the genetic blueprint for robotic systems, defining the physical structure, joints, and properties of a robot. Like DNA defines the structure of biological organisms, URDF describes how the parts of a robot relate to each other in 3D space.

### The Importance of Robot Description

For humanoid robots, which have complex articulated structures similar to humans, URDF becomes especially important:

- **Kinematic chains**: Describes how limbs connect and move relative to each other
- **Physical properties**: Defines mass, inertia, and collision properties
- **Visual representation**: Determines how the robot appears in simulation and visualization
- **Sensor placement**: Specifies where sensors are located on the robot body

## URDF Structure and Components

### Links: The Structural Elements

Links represent rigid bodies in the robot, analogous to bones in the human skeleton:

```xml
<link name="torso">
  <visual>
    <geometry>
      <box size="0.3 0.2 0.5"/>
    </geometry>
    <material name="gray">
      <color rgba="0.5 0.5 0.5 1.0"/>
    </material>
  </visual>
  <collision>
    <geometry>
      <box size="0.3 0.2 0.5"/>
    </geometry>
  </collision>
  <inertial>
    <mass value="5.0"/>
    <inertia ixx="0.1" ixy="0.0" ixz="0.0" iyy="0.1" iyz="0.0" izz="0.1"/>
  </inertial>
</link>
```

**Components of a Link:**
- **Visual**: How the link appears in visualization
- **Collision**: Shape used for collision detection
- **Inertial**: Mass properties for physics simulation

### Joints: The Connections

Joints define how links connect and move relative to each other, like joints in the human body:

```xml
<joint name="torso_to_head" type="revolute">
  <parent link="torso"/>
  <child link="head"/>
  <origin xyz="0.0 0.0 0.3" rpy="0 0 0"/>
  <axis xyz="0 1 0"/>  <!-- Y-axis rotation for head nodding -->
  <limit lower="-0.5" upper="0.5" effort="100" velocity="1.0"/>
</joint>
```

**Joint Types:**
- **Revolute**: Rotational joint (like elbow, knee)
- **Continuous**: Rotational without limits (like shoulder)
- **Prismatic**: Linear sliding joint
- **Fixed**: No movement (welded connection)

### Biological Analogies in Humanoid URDF

Creating a humanoid robot in URDF follows the same hierarchical organization as the human body:

**Spine Structure:**
- Root link: Pelvis (center of mass)
- Series of joints: Spine segments connecting pelvis to torso to neck to head

**Limb Structure:**
- Upper limb: Torso → Shoulder → Arm → Elbow → Forearm → Wrist → Hand
- Lower limb: Pelvis → Hip → Thigh → Knee → Shin → Ankle → Foot

## Essential URDF Tags and Properties

### Materials and Appearance
```xml
<material name="blue">
  <color rgba="0.0 0.0 1.0 1.0"/>
</material>
```

### Transmission Elements
Define how actuators connect to joints for control:
```xml
<transmission name="tran1">
  <type>transmission_interface/SimpleTransmission</type>
  <joint name="shoulder_joint">
    <hardwareInterface>hardware_interface/PositionJointInterface</hardwareInterface>
  </joint>
  <actuator name="motor1">
    <hardwareInterface>hardware_interface/PositionJointInterface</hardwareInterface>
    <mechanicalReduction>1</mechanicalReduction>
  </actuator>
</transmission>
```

### Robot Tag and Naming
The entire description is wrapped in a robot tag:
```xml
<robot name="humanoid_robot">
  <!-- All links and joints go here -->
</robot>
```

## Best Practices for Humanoid URDF Design

### 1. Start with the Root
Always begin with the base or center-of-mass link, typically the pelvis for humanoids.

### 2. Maintain Consistent Units
Use consistent units throughout (typically meters for length, kilograms for mass).

### 3. Realistic Inertial Properties
Calculate or estimate realistic inertial properties for stable simulation.

### 4. Logical Joint Limits
Set joint limits that match human-like ranges of motion for humanoid robots.

### 5. Organized Structure
Group related components and use clear naming conventions.

## Working with URDF in ROS 2

URDF files are typically loaded using robot_state_publisher:

```bash
ros2 run robot_state_publisher robot_state_publisher --ros-args -p robot_description:=$(ros2 pkg prefix your_package)/share/your_package/urdf/robot.urdf
```

This node publishes TF transforms that allow ROS 2 nodes to understand the spatial relationships between different parts of the robot, enabling coordinated movement and sensor fusion.

URDF forms the foundation for all motion planning, control, and simulation in humanoid robotics, serving as the essential bridge between abstract control algorithms and the physical robot structure.