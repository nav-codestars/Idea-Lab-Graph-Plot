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
right_frame = tk.Frame(tkinter_cl.root, bg="#FFFFFF")
right_frame.pack(fill=None, expand=True)

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

def safe_serial_read():
    try:
        if serial_cl is None or not hasattr(serial_cl, 'ser') or not serial_cl.ser.is_open:
            messagebox.showerror("Serial Error", "Serial monitor is not connected!")
            return 0
        data = serial_cl.get_serial_print()
        return data if data else 0
    except Exception:
        messagebox.showerror("Serial Error", "Failed to read from serial monitor!")
        return 0

def button_click_action():
    graph.toggle_frame(
        min_quantity.get(),
        max_quantity.get(),
        left_frame,
        safe_serial_read,
        y_label.get(),
        title.get()
    )
    left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

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
    serial_cl = SerialClass('COM6', 9600, timeout=1)
    if not serial_cl.ser.is_open:
        raise Exception("Serial port is not open")
except Exception:
    serial_cl = None

tkinter_cl.run_loop()




