---
sidebar_position: 2
---

# ROS 2 Architecture: The Framework of the Robotic Nervous System

## Understanding ROS 2 Architecture

ROS 2 represents a significant evolution from its predecessor, addressing critical concerns like real-time performance, security, and industrial reliability. Like the central and peripheral nervous systems working together, ROS 2's architecture balances centralized coordination with distributed processing.

### Core Components of ROS 2 Architecture

#### The DDS Middleware

At the heart of ROS 2 lies DDS (Data Distribution Service), which acts as the neural network infrastructure enabling communication between different parts of the robot system. Think of DDS as the spinal cord and peripheral nerves that ensure information reaches the right destination reliably.

#### Nodes: The Processing Centers

Nodes in ROS 2 are computational units that perform specific functions, similar to organs or specialized brain regions:

- **Sensor nodes** collect information from cameras, lidars, IMUs (like sensory organs)
- **Controller nodes** manage robot motion and behavior (like motor cortex)
- **Perception nodes** interpret sensor data (like visual cortex)
- **Planning nodes** determine future actions (like decision-making regions)

### Communication Patterns

ROS 2 supports three primary communication patterns that mirror how information flows in biological systems:

1. **Publish/Subscribe (Topics)**: Continuous, asynchronous communication like the sympathetic nervous system's broadcast signals
2. **Client/Service**: Request-response interaction like sending a specific signal to move a muscle
3. **Action**: Goal-oriented communication with feedback, like controlling a complex movement with continuous adjustment

### Quality of Service (QoS) Settings

Like biological systems that prioritize critical signals (such as pain responses over less urgent sensations), ROS 2 provides QoS settings that control how messages are delivered:

- **Reliability**: Ensuring messages arrive (like critical safety signals)
- **Durability**: Keeping messages for late joiners (like storing important information in memory)
- **History**: How many messages to retain (like short-term vs long-term memory)
- **Deadline**: Timing constraints for message delivery (like reflex actions)

## Architecture Benefits for Humanoid Robotics

Humanoid robots have unique requirements that make ROS 2's architecture particularly suitable:

- **Complexity Management**: Hundreds of sensors and actuators can be managed through organized node structures
- **Real-time Capabilities**: Critical control loops can be isolated and prioritized
- **Safety Features**: Security protocols protect against unauthorized access to robot controls
- **Multi-platform Integration**: Different computing platforms within the robot can interoperate seamlessly