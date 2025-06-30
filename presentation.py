"""
Handles visual presentation of simulation results using Matplotlib within a Tkinter frame.

Provides methods to clear the canvas and render a 3D plot of the selected strategy.
"""

import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class Presentation:
    def __init__(self, root):
        self.canvas_frame = tk.Frame(root)
        self.canvas_frame.pack(fill=tk.BOTH, expand=True)

    def clear(self):
        for widget in self.canvas_frame.winfo_children():
            widget.destroy()

    def plot(self, results, title):
        fig = plt.figure(figsize=(6, 4))
        ax = fig.add_subplot(111, projection='3d')
        ax.plot(results['income'], results['cost'], results['prosperity'])
        ax.set_xlabel("Income")
        ax.set_ylabel("Cost")
        ax.set_zlabel("Prosperity")
        ax.set_title(f"{title} Strategy")

        canvas = FigureCanvasTkAgg(fig, master=self.canvas_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)