import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from strategies.taught_life import TaughtLife
from strategies.early_extreme_saving import EarlyExtremeSaving
import numpy as np

# Tkinter app
class ProsperityApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Prosperity Strategy Visualizer")

        # Strategy options
        self.strategies = {
            "Taught Life": TaughtLife,
            "Extreme Saver": EarlyExtremeSaving
        }

        # UI Elements
        self.setup_ui()

    def setup_ui(self):
        # Dropdown menu
        self.strategy_var = tk.StringVar(value="Taught Life")
        strategy_menu = ttk.Combobox(self.root, textvariable=self.strategy_var, values=list(self.strategies.keys()))
        strategy_menu.pack(pady=10)

        # Current age input
        self.current_age_var = tk.IntVar(value=25)
        ttk.Label(self.root, text = "Enter you current age:").pack(pady=5)
        current_age_entry = ttk.Entry(self.root, textvariable=self.current_age_var)
        current_age_entry.pack(pady=5)
        
        # Retirement age input
        self.retirement_age_var = tk.IntVar(value=67)
        ttk.Label(self.root, text = "Enter you estimated retirement age:").pack(pady=5)
        retirement_age_entry = ttk.Entry(self.root, textvariable=self.retirement_age_var)
        retirement_age_entry.pack(pady=5)
        
        # Run button
        run_button = tk.Button(self.root, text="Run Simulation", command=self.run_simulation)
        run_button.pack(pady=5)

        # Canvas placeholder
        self.canvas_frame = tk.Frame(self.root)
        self.canvas_frame.pack(fill=tk.BOTH, expand=True)

    def run_simulation(self):
        # Clear previous canvas
        for widget in self.canvas_frame.winfo_children():
            widget.destroy()

        # Strategy setup
        years = np.linspace(self.current_age_var.get(), self.retirement_age_var.get(), 100)
        start_income = 30000
        strategy_class = self.strategies[self.strategy_var.get()]
        strategy = strategy_class(self.strategy_var.get(), years, start_income)
        strategy.run()
        results = strategy.results()

        # Plotting
        fig = plt.figure(figsize=(6, 4))
        ax = fig.add_subplot(111, projection='3d')
        ax.plot(results['income'], results['cost'], results['prosperity'])
        ax.set_xlabel("Income")
        ax.set_ylabel("Cost")
        ax.set_zlabel("Prosperity")
        ax.set_title(f"{strategy.name} Strategy")

        canvas = FigureCanvasTkAgg(fig, master=self.canvas_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

# Run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = ProsperityApp(root)
    root.mainloop()
