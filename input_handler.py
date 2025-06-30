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
        self.current_age_var = tk.IntVar(value=25)
        self.retirement_age_var = tk.IntVar(value=67)
        self.salary_var = tk.IntVar(value=30000)

        self._create_widgets(root)

    def _create_widgets(self, root):
        ttk.Combobox(root, textvariable=self.strategy_var, values=list(self.strategies.keys())).pack(pady=10)
        ttk.Label(root, text="Enter your current age:").pack()
        ttk.Entry(root, textvariable=self.current_age_var).pack()
        ttk.Label(root, text="Enter estimated retirement age:").pack()
        ttk.Entry(root, textvariable=self.retirement_age_var).pack()
        ttk.Label(root, text="Enter current salary:").pack()
        ttk.Entry(root, textvariable=self.salary_var).pack()

    def get_inputs(self):
        return {
            "strategy_name": self.strategy_var.get(),
            "strategy_class": self.strategies[self.strategy_var.get()],
            "current_age": self.current_age_var.get(),
            "retirement_age": self.retirement_age_var.get(),
            "salary": self.salary_var.get()
        }
