import matplotlib.pyplot as plt
import tkint as tk
from matplotlib import animation
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class Graph:
    def __init__(self):
        # Create figure and axis
        self._ani = None
        self._fig, self._ax = plt.subplots()
        self._x_data, self._y_data = [], []
        self._line, = self._ax.plot([], [], 'r-')

    #Generator for dynamic data
    def data_gen(self, data_fetch):
        t = 0
        while True:
            try:
                data = data_fetch()
                print(t, data)
                if self._line:
                    y = int(data)
                    yield t, y
                    t += 1
            except (ValueError, UnicodeDecodeError):
                continue

    # Update function
    def update(self, frame):
        t, y = frame
        self._x_data.append(t)
        self._y_data.append(y)
        self._line.set_data(self._x_data, self._y_data)
        self._ax.set_xlim(max(0, t - 100), max(100, t + 10))  # Scroll x-axis
        # ax.set_ylim(-1.5, 1.5)
        return self._line,

    # Toggle function
    def toggle_frame(self, min_quantity, max_quantity, root, action):
        try:
            min_val = int(min_quantity)
            max_val = int(max_quantity)
        except ValueError:
            print("Invalid min/max quantity input.")
            return

        self._ax.set_ylim(min_val, max_val)
        self._ax.set_xlim(0, 1000)

        canvas = FigureCanvasTkAgg(self._fig, master=root)
        canvas.draw()
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

        self._ani = animation.FuncAnimation(self._fig, self.update, frames=lambda: self.data_gen(action), interval=1000, blit=False)
        canvas.draw_idle()