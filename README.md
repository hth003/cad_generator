# CadGenerator

A powerful CAD generation system built with crewAI that leverages AI agents to create and manipulate 3D models. This project combines the capabilities of OpenSCAD, PyVista, and PyQt6 to provide a comprehensive CAD generation and visualization solution.

## Features

- AI-powered CAD model generation using crewAI agents
- 3D model visualization with PyVista
- Interactive GUI using PyQt6
- OpenSCAD script generation and STL output
- Knowledge base for CAD design patterns
- Training and replay capabilities for model generation

## Installation

Ensure you have Python >=3.10 <3.13 installed on your system. This project uses [UV](https://docs.astral.sh/uv/) for dependency management and package handling.

First, if you haven't already, install uv:

```bash
pip install uv
```

Next, navigate to your project directory and install the dependencies:

```bash
uv pip install -e .
```

### Environment Setup

**Add your `OPENAI_API_KEY` into the `.env` file**

## Usage

The project provides several command-line interfaces:

```bash
# Run the main CAD generation crew
cad_generator

# Run the crew with specific configuration
run_crew

# Train the model with new data
train

# Replay previous generations
replay

# Run tests
test

# Launch the GUI interface
gui
```

## Project Structure

- `src/cad_generator/` - Main source code
  - `config/` - Configuration files for agents and tasks
  - `crew.py` - Crew setup and management
  - `main.py` - Entry points for different commands
- `knowledge/` - Knowledge base for CAD design patterns
- `db/` - Database for storing generated models and configurations
- `tests/` - Test suite

## Dependencies

- crewAI[tools] >= 0.119.0
- numpy >= 2.2.5
- pyvista >= 0.45.2
- pyvistaqt >= 0.9.0
- PyQt6 >= 6.4.0

## Support

For support, questions, or feedback:
- Visit the [crewAI documentation](https://docs.crewai.com)
- Check the [crewAI GitHub repository](https://github.com/joaomdmoura/crewai)
- [Join the crewAI Discord](https://discord.com/invite/X4JWnZnxPb)

## License

This project is licensed under the MIT License - see the LICENSE file for details.
