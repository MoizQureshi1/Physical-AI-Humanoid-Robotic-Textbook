---
sidebar_position: 3
---

# Nodes, Topics, Services, and Actions: The Neural Network of Communication

## Nodes: The Functional Units of the Robot Body

In the ROS 2 ecosystem, nodes function as specialized organs or systems within the robot, each responsible for specific tasks. Just as different organs in the human body have specialized functions, robot nodes perform dedicated operations:

- **Sensor nodes** collect information from the environment (eyes, ears, skin)
- **Processing nodes** interpret sensor data and make decisions (brain regions)
- **Control nodes** manage actuators and motors (motor cortex and spinal cord)
- **Interface nodes** connect to external systems or users (sensory gateways)

### Characteristics of Nodes
- Each node typically performs one primary function
- Nodes can be written in different programming languages (C++, Python, Rust)
- Nodes can run on different machines or processors within the robot
- Multiple nodes can be packaged into a single executable for efficiency

## Topics: The Information Superhighway

Topics represent the communication channels between nodes, analogous to nerve bundles carrying signals throughout the body. Information travels continuously from publishers (sensors, decision-making nodes) to subscribers (actuators, monitoring nodes).

### How Topics Work
- Publishers send data to a topic (e.g., camera images, sensor readings)
- Subscribers receive data from a topic (e.g., image processing, logging)
- Multiple publishers can send to the same topic
- Multiple subscribers can receive from the same topic
- Communication is fire-and-forget (asynchronous)

### Biological Analogy
Consider how the optic nerve carries visual information: light sensors (camera) send continuous streams of data through the optic nerve (topic) to the visual cortex (subscriber) which processes the information. Multiple areas of the brain may simultaneously process different aspects of the same visual stream.

## Services: On-Demand Requests

Services handle request-response communication, similar to how the brain sends specific commands that require immediate feedback. When you decide to reach for an object, your brain sends a specific command and expects confirmation that the action is complete.

### Service Characteristics
- Client sends a request and waits for a response
- Synchronous communication
- Typically used for operations that have a clear start and end
- Examples: saving a map, calibrating a sensor, executing a specific action

## Actions: Complex, Monitored Operations

Actions combine features of topics and services for complex operations that require ongoing feedback and can be canceled. Like complex motor activities that require continuous adjustment and monitoring (walking, speaking, reaching).

### Action Components
- **Goal**: What the action should accomplish
- **Feedback**: Continuous status updates during execution
- **Result**: Final outcome when the action completes

### Real-World Example
Moving a robot arm to pick up an object involves:
1. Sending a goal (move arm to grasp position)
2. Receiving feedback (current joint angles, distance to target)
3. Returning a result (success or failure to reach)

## Practical Applications in Humanoid Robotics

In humanoid robots, these communication patterns enable complex coordinated behavior:

- **Walking**: Controller nodes publish joint commands (topics) while receiving sensor feedback
- **Object recognition**: Camera nodes publish images to perception nodes
- **Speech interaction**: Service calls handle speech recognition and synthesis
- **Navigation**: Action servers handle complex path planning with continuous feedback