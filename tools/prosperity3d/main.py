"""
Entry point for the Prosperity Strategy Visualizer.

Initializes the Tkinter app and connects the input, simulation, and presentation layers.
"""

import tkinter as tk
from tools.prosperity3d.input_handler import InputHandler
from tools.prosperity3d.presentation import Presentation
from simulation.engine import run_simulation

class ProsperityApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Prosperity Strategy Visualizer")
        self.input_handler = InputHandler(root)
        self.presentation = Presentation(root)

        run_button = tk.Button(root, text="Run Simulation", command=self.run)
        run_button.pack(pady=5)

    def run(self):
        self.presentation.clear()
        inputs = self.input_handler.get_inputs()
        results, strategy_name = run_simulation(inputs)
        self.presentation.plot(results, strategy_name)

if __name__ == "__main__":
    root = tk.Tk()
    app = ProsperityApp(root)
    root.mainloop()