"""
Handles user input for the Prosperity Strategy Visualizer.

Provides UI elements to collect input values such as strategy selection,
calendar year and birth year.
"""

import tkinter as tk
from tkinter import ttk
from strategies.taught_life import TaughtLife
from strategies.early_extreme_saving import EarlyExtremeSaving

class InputHandler:
    def __init__(self, root):
        self.strategies = {
            "Taught Life": TaughtLife,
            "Extreme Saver": EarlyExtremeSaving
        }

        self.strategy_var = tk.StringVar(value="Taught Life")
        self.calender_year_var = tk.IntVar(value=2025)
        self.birth_year_var = tk.IntVar(value=1978)

        self._create_widgets(root)

    def _create_widgets(self, root):
        ttk.Label(root, text="Select strategy:").pack()
        ttk.Combobox(root, textvariable=self.strategy_var, values=list(self.strategies.keys())).pack(pady=10)

        ttk.Label(root, text="Enter calendar year (simulation starts):").pack()
        ttk.Entry(root, textvariable=self.calender_year_var).pack()

        ttk.Label(root, text="Enter birth year of the person:").pack()
        ttk.Entry(root, textvariable=self.birth_year_var).pack()

    def get_inputs(self):
        return {
            "strategy_name": self.strategy_var.get(),
            "strategy_class": self.strategies[self.strategy_var.get()],
            "calender_year": self.calender_year_var.get(),
            "birth_year": self.birth_year_var.get()
        }
