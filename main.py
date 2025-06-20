from ttkbootstrap import Style, PRIMARY
from util.graph import Graph
from util.serial_comm import SerialClass
from util.tkint import TkintClass
from tkinter import messagebox
import tkinter as tk

font_style = ('Segoe UI', 14)
tkinter_cl = TkintClass('Graph tool', '1000x666', font_style, bg="#F5F7FA")

# Create a custom button style
style = Style()
style.configure(
    "Custom.TButton",
    font=('Segoe UI', 12, 'bold'),
    background="#3B82F6",
    foreground="#FFFFFF",
    borderwidth=0,
    focusthickness=3,
    focuscolor="#2563EB"
)

# --- Layout: Create left (graph) and right (inputs) frames ---
left_frame = tk.Frame(tkinter_cl.root, bg="#F5F7FA")
right_frame = tk.Frame(tkinter_cl.root, bg="#FFFFFF", width=350, height=600)
right_frame.pack(fill=None, expand=True)
right_frame.pack_propagate(False)

# Spacer to push input fields to the bottom
spacer = tk.Frame(right_frame, bg="#FFFFFF")
spacer.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

# Input frame at the bottom of right_frame
input_frame = tk.Frame(right_frame, bg="#FFFFFF")
input_frame.pack(side=tk.BOTTOM, fill=tk.X, padx=40, pady=40)

# Input fields and buttons in input_frame
min_quantity = tkinter_cl.create_input(input_frame, "Minimum Quantity Value", default="10")
max_quantity = tkinter_cl.create_input(input_frame, "Maximum Quantity Value", default="100")
y_label = tkinter_cl.create_input(input_frame, "Y Label", default="Distance (cm)")
title = tkinter_cl.create_input(input_frame, "Title of Graph", default="Real-time Distance Measurement")


def button_click_action():
    if serial_cl is None or not hasattr(serial_cl, 'ser') or not getattr(serial_cl.ser, 'is_open', False):
        messagebox.showerror("Serial Error", "Serial monitor is not connected!")
        return
    graph.toggle_frame(
        min_quantity.get(),
        max_quantity.get(),
        left_frame,
        serial_cl.get_serial_print,
        y_label.get(),
        title.get()
    )
    left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=False)
    right_frame.pack_propagate(False)


btn = tkinter_cl.create_button(
    input_frame,
    'Show graph',
    lambda: button_click_action(),
    "Custom.TButton"
)

save_to_pdf_btn = tkinter_cl.create_button(
    input_frame,
    'Save graph to pdf',
    lambda: graph.save_as_pdf('graph_output.pdf'),
    "Custom.TButton"
)

# Place the graph in the left frame
graph = Graph()

# Attempt to connect to serial port
try:
    serial_cl = SerialClass('COM4', 9600, timeout=0)
except Exception as e:
    print(e)

def window_close():
    tkinter_cl.running = False
    print(graph)
    tkinter_cl.root.destroy()
    if serial_cl is not None:
        serial_cl.close_serial()
    exit(0)

tkinter_cl.root.protocol("WM_DELETE_WINDOW", window_close)


tkinter_cl.run_loop()




