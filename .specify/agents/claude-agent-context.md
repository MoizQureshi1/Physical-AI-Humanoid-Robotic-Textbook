# Spec-Driven Book on Physical AI & Humanoid Robotics Development Guidelines

Auto-generated from all feature plans. Last updated: 2026-02-07

## Active Technologies

- **Documentation Framework**: Docusaurus 3.x
- **Programming Languages**: Markdown (.md), JavaScript/TypeScript
- **ROS 2**: Humble Hawksbill (LTS) for robotic middleware
- **Simulation Platforms**: Gazebo Garden, Unity 2023.x
- **AI/ML Framework**: NVIDIA Isaac ecosystem (Isaac Sim, Isaac ROS, Nav2)
- **Hosting**: GitHub Pages
- **Build Tools**: Node.js 18+, npm

## Project Structure

```text
project-root/
├── docs/
│   ├── intro/
│   ├── module-1-ros/
│   ├── module-2-simulation/
│   ├── module-3-ai-brain/
│   └── capstone/
├── specs/001-humanoid-robotics-training/
│   ├── plan.md
│   ├── research.md
│   ├── data-model.md
│   ├── quickstart.md
│   ├── contracts/
│   └── tasks.md
├── docusaurus.config.js
├── package.json
└── src/
    ├── css/
    └── pages/
```

## Commands

### Development
- `npm start` - Start local development server with hot reload
- `npm run build` - Build static site for production
- `npm run serve` - Serve built site locally for preview

### Documentation Structure
- Create content in appropriate module directory in `/docs/`
- Update `_category_.json` files to manage navigation
- Use consistent frontmatter in all markdown files
- Include descriptive alt text for all images/diagrams

### Content Guidelines
- Focus on beginner-friendly explanations using biological analogies
- Maintain consistency with specified technologies (ROS 2, Gazebo, Unity, Isaac)
- Prioritize conceptual understanding over implementation details
- Ensure all technical claims are verified against official documentation

## Code Style

### Markdown Style
- Use H1 for document titles, H2-H4 for sections
- Include frontmatter with title and sidebar_label
- Use numbered lists for sequential processes
- Use bullet points for non-sequential information
- Add code blocks with appropriate language tags (```python, ```bash, etc.)

### Content Style
- Use analogies consistently (robotic concepts → biological equivalents)
- Explain concepts before introducing technical terminology
- Include practical examples relevant to humanoid robotics
- Provide visual descriptions for all diagrams and figures
- Write for beginner-level audience with no prior robotics experience

### Technical Accuracy
- Verify all technical claims against official documentation
- Use official terminology from ROS 2, Gazebo, Unity, NVIDIA Isaac
- Cross-reference information with source documentation
- Clearly distinguish between simulation and real-world scenarios

## Recent Changes

- **001-humanoid-robotics-training**: Created initial training modules on ROS 2 as robotic nervous system, digital twin simulation, and AI brain concepts
- **Module 1**: Established ROS 2 architecture foundations with biological analogies
- **Module 2**: Defined simulation workflows using Gazebo and Unity for digital twins

<!-- MANUAL ADDITIONS START -->
<!-- MANUAL ADDITIONS END -->