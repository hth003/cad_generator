import logging
logging.getLogger().setLevel(logging.ERROR)
import warnings
warnings.filterwarnings("ignore")

import sys
import subprocess
from pathlib import Path
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QTextEdit, QPushButton, QLabel, QSplitter, QSizePolicy
)
from PyQt6.QtCore import Qt
import pyvista as pv
from pyvistaqt import QtInteractor
from cad_generator.crew import CadGenerator

class CadGeneratorGUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("CAD Generator")
        self.setMinimumSize(1200, 700)

        # Main widget and layout
        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        main_layout = QVBoxLayout(main_widget)
        main_layout.setContentsMargins(12, 12, 12, 12)
        main_layout.setSpacing(8)

        # Prompt row (label, input, button)
        prompt_row = QHBoxLayout()
        prompt_label = QLabel("Enter your prompt:")
        prompt_label.setMinimumWidth(120)
        self.input_text = QTextEdit()
        self.input_text.setPlaceholderText("Enter your CAD generation prompt here...")
        self.input_text.setFixedHeight(40)
        self.input_text.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        self.run_button = QPushButton("Generate")
        self.run_button.setFixedWidth(100)
        self.run_button.clicked.connect(self.generate_cad)
        prompt_row.addWidget(prompt_label)
        prompt_row.addWidget(self.input_text)
        prompt_row.addWidget(self.run_button)
        prompt_row.setSpacing(8)
        main_layout.addLayout(prompt_row)

        # Splitter for script and 3D view
        splitter = QSplitter(Qt.Orientation.Horizontal)
        splitter.setHandleWidth(4)

        # Script output panel
        script_widget = QWidget()
        script_layout = QVBoxLayout(script_widget)
        script_layout.setContentsMargins(0, 0, 0, 0)
        script_label = QLabel("OpenSCAD Script:")
        self.script_output = QTextEdit()
        self.script_output.setReadOnly(True)
        self.script_output.setMinimumWidth(350)
        self.script_output.setMaximumWidth(600)
        self.script_output.setMinimumHeight(400)
        script_layout.addWidget(script_label)
        script_layout.addWidget(self.script_output)
        script_layout.setSpacing(4)

        # 3D viewer panel
        viewer_widget = QWidget()
        viewer_layout = QVBoxLayout(viewer_widget)
        viewer_layout.setContentsMargins(0, 0, 0, 0)
        viewer_label = QLabel("3D Preview:")
        self.viewer = QtInteractor(viewer_widget)
        self.viewer.setMinimumHeight(400)
        viewer_layout.addWidget(viewer_label)
        viewer_layout.addWidget(self.viewer)
        viewer_layout.setSpacing(4)

        splitter.addWidget(script_widget)
        splitter.addWidget(viewer_widget)
        splitter.setSizes([400, 800])
        main_layout.addWidget(splitter)

    def generate_cad(self):
        prompt = self.input_text.toPlainText()
        if not prompt:
            return
        try:
            # Get the CAD generation result
            generator = CadGenerator()
            generator.crew().kickoff(inputs={'user_prompt': prompt})

            # Read the generated OpenSCAD script
            script_path = Path('openscad_script.scad')
            if script_path.exists():
                with open(script_path, 'r') as f:
                    self.script_output.setText(f.read())
                # Generate STL from OpenSCAD script
                stl_path = script_path.with_suffix('.stl')
                subprocess.run(['openscad', '-o', str(stl_path), str(script_path)], check=True)
                # Display STL in viewer
                self.viewer.clear()
                mesh = pv.read(str(stl_path))
                self.viewer.add_mesh(mesh, color="skyblue", show_edges=False)
                self.viewer.add_mesh(mesh, style='wireframe', color='black', line_width=1)
                self.viewer.reset_camera()
        except Exception as e:
            self.script_output.setText(f"Error: {str(e)}")

def main_gui():
    app = QApplication(sys.argv)
    window = CadGeneratorGUI()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main_gui()