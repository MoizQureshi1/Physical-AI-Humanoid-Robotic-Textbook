# Quickstart Guide: Humanoid Robotics Training Modules

**Feature**: 001-humanoid-robotics-training | **Date**: 2026-02-07

## Overview

This guide will help you set up the environment for developing and contributing to the Spec-Driven Book on Physical AI & Humanoid Robotics. The book is built with Docusaurus and hosted on GitHub Pages.

## Prerequisites

- **Node.js**: Version 18.x or higher
- **npm** or **yarn**: Package manager (npm preferred)
- **Git**: Version control
- **GitHub account**: For collaboration
- **Text editor**: VS Code recommended with Markdown extensions

## Environment Setup

### 1. Clone the Repository
```bash
git clone <repository-url>
cd <repository-name>
```

### 2. Install Dependencies
```bash
npm install
```

### 3. Verify Installation
```bash
npm run build
```
If this command completes without errors, your environment is properly configured.

### 4. Start Local Development Server
```bash
npm start
```
This command starts a local development server with live reloading. The site will be available at http://localhost:3000.

## Project Structure

```
project-root/
├── docs/                    # Content source files (Markdown)
│   ├── intro/
│   ├── module-1-ros/
│   ├── module-2-simulation/
│   ├── module-3-ai-brain/
│   └── capstone/
├── docusaurus.config.js     # Site configuration
├── package.json            # Dependencies and scripts
├── src/
│   ├── css/
│   └── pages/
├── static/                 # Static assets
└── babel.config.js         # JavaScript transpilation config
```

## Content Creation Workflow

### 1. Create New Content

1. Navigate to the appropriate module directory in `/docs/`
2. Create a new `.md` file with descriptive name
3. Follow the content template below:

```markdown
---
title: Your Content Title
sidebar_label: Sidebar Label
---

# Your Content Title

## Overview
Brief description of what this section covers.

## Key Concepts
- Point 1
- Point 2
- Point 3

## Examples
Practical examples relevant to humanoid robotics.

## Summary
Key takeaways for the reader.
```

### 2. Update Navigation

Edit the `_category_.json` files in each module directory to add your new content to the sidebar:

```json
{
  "label": "Your Page Title",
  "position": 3,
  "link": {
    "type": "generated-index",
    "description": "Description of this section"
  }
}
```

### 3. Add Diagram Descriptions

Since diagrams are described textually for accessibility, add them using the following format:

```markdown
import Mermaid from '@theme/Mermaid';

<div className="mermaid">
graph TD;
    A[Humanoid Robot] --> B[ROS 2 Network];
    B --> C[Navigation Node];
    B --> D[Perception Node];
    B --> E[Control Node];
</div>

*Figure: ROS 2 network architecture showing the communication between different nodes in a humanoid robot system.*
```

## Writing Guidelines

### For Beginners
- Use analogies consistently (e.g., robotic nodes compared to neurons)
- Explain concepts before introducing technical terminology
- Provide visual descriptions for all diagrams
- Include practical examples relevant to humanoid robotics

### Content Standards
- All content must be in Markdown format
- Follow Docusaurus best practices for structure
- Use H1 for page titles, H2-H4 for sections
- Include code blocks with appropriate language tagging
- Add alt text for all images

### Technical Accuracy
- Cross-reference all technical claims with official documentation
- Verify ROS 2, Gazebo, Unity, and Isaac documentation
- Maintain consistency with the specified technologies (ROS 2 Humble, Gazebo Garden, etc.)

## Building and Testing

### Build for Production
```bash
npm run build
```
This creates a production-ready build in the `build/` directory.

### Preview Build
```bash
npm run serve
```
Serves the production build locally for preview before deployment.

### Check for Broken Links
```bash
npm run build
npx @docusaurus/module-type-aliases
```

## Contributing Process

1. **Fork and Clone**: Fork the repository and clone your fork
2. **Create Branch**: Create a feature branch (`git checkout -b feature/your-feature`)
3. **Develop**: Make your changes following the guidelines above
4. **Test Locally**: Run `npm start` to verify your changes work properly
5. **Commit**: Commit your changes with clear, descriptive messages
6. **Push**: Push to your fork (`git push origin feature/your-feature`)
7. **Pull Request**: Create a pull request to the main repository

## Technology Stack Reference

### ROS 2 (Humble Hawksbill)
- **Documentation**: https://docs.ros.org/en/humble/
- **Core Concepts**: Nodes, Topics, Services, Actions, Parameters
- **Client Libraries**: rclpy (Python), rclcpp (C++)

### Gazebo (Garden)
- **Documentation**: https://gazebosim.org/docs/garden/
- **Features**: Physics simulation, sensor simulation, 3D environments
- **Integration**: ros_gz_bridge for ROS 2 communication

### Unity Integration
- **Package**: Unity Robotics Package
- **Features**: Visualization, user interfaces, enhanced graphics
- **Connection**: ROS TCP Connector for communication

### NVIDIA Isaac
- **Components**: Isaac Sim, Isaac ROS packages, Nav2
- **Documentation**: https://docs.nvidia.com/isaac/
- **Focus Areas**: Perception, navigation, sim-to-real transfer

## Troubleshooting

### Common Issues
1. **Build errors**: Run `npm install` to ensure all dependencies are installed
2. **Missing content**: Verify file paths in `_category_.json` and frontmatter
3. **Link errors**: Check that all internal links use relative paths
4. **Style issues**: Run `npm start` to see the site as users will view it

### Verification Steps
- [ ] Local development server starts without errors
- [ ] All pages load correctly
- [ ] Navigation works as expected
- [ ] Content renders properly
- [ ] Links are functional