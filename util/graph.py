import matplotlib.pyplot as plt
import tkinter as tk
from matplotlib import animation
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class Graph:
    def __init__(self):
        self._ani = None
        self._fig, self._ax = plt.subplots()
        self._x_data, self._y_data = [], []
        self._line, = self._ax.plot([], [], color="#3B82F6")  # Soft blue
        self._canvas = None  # Track the current canvas

        # Subtle background and axis styling
        self._fig.patch.set_facecolor("#FFFFFF")
        self._ax.set_facecolor("#F5F7FA")
        self._ax.tick_params(colors="#22223B")
        for spine in self._ax.spines.values():
            spine.set_color('#E0E1DD')
        self._ax.set_xlabel("Time (s)", fontdict={'fontsize': 12, 'fontweight': 'bold', 'color': '#22223B'})
        self._ax.set_ylabel("Distance (cm)", fontdict={'fontsize': 12, 'fontweight': 'bold', 'color': '#22223B'})
        self._ax.set_title("Real-time Distance Measurement", fontsize=16, fontweight='bold', color="#22223B")

    def data_gen(self, data_fetch):
        t = 0
        while True:
            try:
                data = data_fetch()
                y = int(data)
                yield t, y
                t += 1
                print(t, data)  # Debugging output
            except (ValueError, UnicodeDecodeError):
                continue

    def update(self, frame):
        t, y = frame
        self._x_data.append(t)
        self._y_data.append(y)
        self._line.set_data(self._x_data, self._y_data)
        self._ax.set_xlim(max(0, t - 100), max(100, t + 10))
        return self._line,

    def toggle_frame(self, min_quantity, max_quantity, root, action, y_label, title):
        try:
            min_val = int(min_quantity)
            max_val = int(max_quantity)
        except ValueError:
            from tkinter import messagebox
            messagebox.showerror("Input Error", "Please enter valid integer values for min and max.")
            return

        self._ax.set_ylabel(y_label, fontdict={'fontsize': 12, 'fontweight': 'bold', 'color': '#22223B'})
        self._ax.set_title(title, fontsize=16, fontweight='bold', color="#22223B")

        # Remove previous canvas if it exists
        if self._canvas is not None:
            try:
                self._canvas.get_tk_widget().destroy()
            except Exception as e:
                print("Error destroying previous canvas:", e)
            self._canvas = None

        self._x_data, self._y_data = [], []
        self._ax.set_ylim(min_val, max_val)
        self._ax.set_xlim(0, 1000)

        self._canvas = FigureCanvasTkAgg(self._fig, master=root)
        self._canvas.draw()
        self._canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
        self._ani = animation.FuncAnimation(
            self._fig,
            self.update,
            frames=lambda: self.data_gen(action),
            interval=1000,
            blit=False,
            cache_frame_data=False,
            save_count=200
        )
        self._canvas.draw_idle()

    def save_as_pdf(self, filename="graph_output.pdf"):
        self._fig.savefig(filename, format='pdf')
        print(f"Graph saved as {filename}")


