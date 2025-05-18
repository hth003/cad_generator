from crewai.tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field
import subprocess
import tempfile
import os

class MyCustomToolInput(BaseModel):
    """Input schema for MyCustomTool."""
    argument: str = Field(..., description="Description of the argument.")

class MyCustomTool(BaseTool):
    name: str = "Name of my tool"
    description: str = (
        "Clear description for what this tool is useful for, your agent will need this information to use it."
    )
    args_schema: Type[BaseModel] = MyCustomToolInput

    def _run(self, argument: str) -> str:
        # Implementation goes here
        return "this is an example of a tool output, ignore it and move along."




class OpenSCADValidationTool(BaseTool):
    name: str = "OpenSCADValidationTool"
    description: str = "Validates an OpenSCAD script. Returns syntax errors or confirms it's valid."

    def _run(self, script_code: str) -> str:
        """Validates an OpenSCAD script. Returns syntax errors or confirms it's valid."""
        script_path = "openscad_script.scad"
        try:
            # Write the script to the file
            with open(script_path, 'w') as f:
                f.write(script_code)

            # Attempt to compile with OpenSCAD
            result = subprocess.run(
                ['openscad', '-o', 'output.stl', script_path],
                capture_output=True,
                text=True
            )

            if result.returncode != 0:
                return f"❌ OpenSCAD Validation Failed:\n{result.stderr.strip()}"
            else:
                return "✅ OpenSCAD script is valid and compiled successfully."

        except Exception as e:
            return f"🔥 Tool Exception: {str(e)}"

        finally:
            # Clean up
            if os.path.exists(script_path):
                os.remove(script_path)