"""
Handles visual presentation of simulation results using Matplotlib within a Tkinter frame.

Provides methods to clear the canvas and render plots and results for the selected strategy.
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
        # 3D-plot
        fig_3d = plt.figure(figsize=(6, 4))
        ax3d = fig_3d.add_subplot(111, projection='3d')
        ax3d.plot(results['income'], results['cost'], results['prosperity'])
        ax3d.set_xlabel("Income")
        ax3d.set_ylabel("Cost")
        ax3d.set_zlabel("Prosperity")
        ax3d.set_title(f"{title} Strategy (3D View)")

        canvas_3d = FigureCanvasTkAgg(fig_3d, master=self.canvas_frame)
        canvas_3d.draw()
        canvas_3d.get_tk_widget().pack(fill=tk.BOTH, expand=True)

        # 2D-plot: prosperity over time
        if 'years' in results:
            fig_2d = plt.figure(figsize=(6, 2.5))
            ax2d = fig_2d.add_subplot(111)
            ax2d.plot(results['years'], results['prosperity'])
            ax2d.set_xlabel("Age")
            ax2d.set_ylabel("Prosperity")
            ax2d.set_title(f"{title} Classical Perspective - Disposable Wealth Over Time")

        canvas_2d = FigureCanvasTkAgg(fig_2d, master=self.canvas_frame)
        canvas_2d.draw()
        canvas_2d.get_tk_widget().pack(fill=tk.BOTH, expand=True)