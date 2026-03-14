---
sidebar_position: 2
---

# Capstone Project: The Autonomous Delivery Humanoid

## Project Mission

The goal of this capstone project is to design the software architecture and simulation workflow for a humanoid robot tasked with **delivering a package in a dynamic office environment**.

This project requires you to integrate concepts from all three modules:
1.  **Module 1 (ROS 2)**: Communication and node structure.
2.  **Module 2 (Simulation)**: Digital twin environment and physics.
3.  **Module 3 (AI Brain)**: Perception and navigation.

---

## Part 1: System Architecture (The Nervous System)

### Node Map
Design a ROS 2 system that includes the following nodes:

*   **`perception_node`**: Subscribes to camera/LiDAR data and publishes detected object locations.
*   **`navigation_server`**: Uses Nav2 to plan paths and avoid obstacles.
*   **`task_orchestrator`**: A high-level node (possibly using Behavior Trees) that manages the delivery workflow.
*   **`hardware_interface`**: Bridges ROS 2 commands to the robot's actuators (simulated or real).

### Biological Analogy
Describe how your ROS 2 architecture mimics a biological nervous system:
*   Which nodes represent the "eyes" and "ears"?
*   Which nodes represent the "muscles"?
*   How does the "spine" (ROS 2 middleware) ensure fast communication?

---

## Part 2: The Digital Twin (Simulation Workflow)

### Environment Setup
1.  **Simulation Platform**: Choose between Gazebo (for physics testing) or Isaac Sim (for AI training).
2.  **Scene Creation**: Design an office environment with corridors, desks, and moving people (dynamic obstacles).
3.  **Digital Twin Sync**: Ensure the URDF model in simulation perfectly matches the physical robot's dimensions and mass properties.

### Sim-to-Real Strategy
*   What **Domain Randomization** techniques will you use to ensure the robot doesn't get confused by different lighting in the real office?
*   How will you model the **sensor noise** of the depth camera in simulation?

---

## Part 3: The AI Brain (Intelligence)

### Perception & Navigation
1.  **Mapping**: Use VSLAM to create a 3D map of the office.
2.  **Path Planning**: Configure the **Global Planner** to find the shortest route and the **Local Planner** to dodge walking colleagues.
3.  **Social Norms**: Ensure the robot maintains a "personal zone" distance (45-120cm) when passing humans in the hallway.

---

## Part 4: End-to-End Workflow

### The Delivery Loop

1.  **Pickup**: The robot receives a "Delivery Request" via a ROS 2 Action. It identifies the package using the perception system.
2.  **Navigation**: The Nav2 stack generates a path to the destination office.
3.  **Dynamic Adaptation**: A colleague steps in front of the robot. The Local Planner detects this and recalculates a safe path.
4.  **Verification**: Upon arrival, the robot uses its camera to verify it is at the correct desk before signaling completion.

---

## Conclusion

By completing this conceptual project design, you have demonstrated a comprehensive understanding of how to build a modern humanoid robot. You have moved from individual components to a unified system that can perceive, think, and act in a complex world.

### Learning Summary
*   **Module 1**: You mastered the infrastructure.
*   **Module 2**: You learned to build safe, virtual playgrounds.
*   **Module 3**: You gave the robot intelligence.
*   **Capstone**: You became a robotics systems architect.

**Welcome to the future of Physical AI!**
