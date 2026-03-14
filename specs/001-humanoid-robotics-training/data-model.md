# Data Model: Humanoid Robotics Training Modules

**Feature**: 001-humanoid-robotics-training | **Date**: 2026-02-07

## Core Entities

### TrainingModule
Represents a major section of the book containing related concepts and learning objectives

- **id**: Unique identifier (e.g., "module-1-ros", "module-2-simulation", "module-3-ai-brain")
- **title**: Display name of the module
- **goal**: Primary learning objective for the module
- **focus**: Key concepts covered in the module
- **constraints**: Boundaries of what is/not covered
- **output**: Expected deliverables or learning outcomes
- **prerequisites**: Knowledge required before starting the module
- **estimatedTime**: Approximate hours needed to complete the module
- **sections**: Array of Section entities that compose the module

### Section
A subsection within a module containing specific concepts

- **id**: Unique identifier within the module
- **title**: Display name of the section
- **description**: Brief explanation of what the section covers
- **learningObjectives**: Specific skills/knowledge learners should gain
- **contentPath**: File path for the markdown content
- **order**: Sequential position within the parent module

### Concept
An individual concept or topic within a section

- **id**: Unique identifier within the section
- **name**: Name of the concept
- **definition**: Clear explanation of the concept
- **analogy**: Biological or familiar analogy for understanding
- **examples**: Practical examples demonstrating the concept
- **validationMethods**: Ways to validate understanding

### Diagram
Visual representation of a concept (described textually for accessibility)

- **id**: Unique identifier
- **title**: Description of the diagram
- **type**: Category (architecture, flowchart, comparison, etc.)
- **description**: Textual description of what the diagram shows
- **keyElements**: Main components shown in the diagram
- **relationToConcept**: Which concept(s) this diagram illustrates

### UserScenario
Learner scenario defining expected capabilities after completing content

- **id**: Unique identifier
- **description**: Narrative of the learner's capability
- **givenContext**: Prerequisites or initial conditions
- **whenAction**: Action the learner performs
- **thenOutcome**: Expected result or demonstration of knowledge
- **priority**: Importance level (P1/P2/P3)
- **testability**: How this can be independently verified

## Relationships

### Module Contains Sections
- **TrainingModule** (1) → **Section** (0..n)
- A module contains zero or more sections

### Section Contains Concepts
- **Section** (1) → **Concept** (0..n)
- A section contains zero or more concepts

### Concept Associated With Diagrams
- **Concept** (1) → **Diagram** (0..n)
- A concept may be illustrated by zero or more diagrams

### Scenario Validates Learning Objectives
- **UserScenario** (1) → **Section.learningObjectives** (0..n)
- A scenario validates one or more specific learning objectives

## Validation Rules

### TrainingModule Validation
- Must have a non-empty title, goal, and estimatedTime
- Estimated time must be between 1 and 20 hours
- Sections must be ordered sequentially with no gaps
- Must have at least one section defined

### Section Validation
- Must have a non-empty title and description
- Learning objectives must be specific and measurable
- Content path must point to a valid markdown file
- Order must be a positive integer

### Concept Validation
- Name and definition must not be empty
- Analogy must relate to the concept appropriately
- Examples must be relevant to humanoid robotics
- Must have at least one example

### UserScenario Validation
- Description must clearly state the learner's capability
- Given/When/Then format must be followed
- Priority must be one of P1, P2, or P3
- Testability must describe a concrete verification method

## State Transitions

### Module States
- **Draft**: Initial state, content being developed
- **Reviewed**: Content reviewed by subject matter experts
- **Published**: Content ready for learners
- **Archived**: Content deprecated or outdated

### Section States
- **Planning**: Outline being developed
- **Development**: Content being written
- **Review**: Content under review
- **Complete**: Content finalized

## Example Instance

```yaml
TrainingModule:
  id: "module-1-ros"
  title: "The Robotic Nervous System (ROS 2)"
  goal: "Explain ROS 2 as the nervous system of a humanoid robot"
  focus: ["ROS 2 architecture", "Nodes, topics, services, actions", "Python agents with rclpy", "URDF basics"]
  constraints: ["Conceptual only", "No full code or hardware details"]
  output: ["High-level chapters", "Diagrams (described)", "Learning outcomes"]
  prerequisites: ["None - beginner friendly"]
  estimatedTime: 5
  sections:
    - id: "architecture-overview"
      title: "ROS 2 Architecture Overview"
      description: "Understanding the distributed computing framework of ROS 2"
      learningObjectives: ["Explain nodes as computational units", "Identify different communication patterns"]
      contentPath: "module-1-ros/architecture.md"
      order: 1
    - id: "nodes-topics-services"
      title: "Communication Patterns"
      description: "How different parts of the robot communicate"
      learningObjectives: ["Distinguish between topics, services, and actions", "Recognize appropriate use cases"]
      contentPath: "module-1-ros/nodes-topics.md"
      order: 2

UserScenario:
  id: "scenario-1-ros-basics"
  description: "Learner can identify components in a ROS 2 system diagram"
  givenContext: "Humanoid robot system architecture diagram"
  whenAction: "Learner identifies nodes, topics, services, and actions"
  thenOutcome: "Correctly matches each component to its role in the robot's nervous system"
  priority: "P1"
  testability: "Exercise with labeled diagrams showing different components"
```