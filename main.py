from ttkbootstrap import Style, PRIMARY
from util.graph import Graph
from util.serial_comm import SerialClass
from util.tkint import TkintClass
from tkinter import messagebox

# Modern, readable font
font_style = ('Segoe UI', 14)

# Initialize GUI with subtle background
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

min_quantity = tkinter_cl.create_input({'padx': 10, 'pady': 10}, {'padx': 10, 'pady': 10}, "Minimum Quantity Value")
max_quantity = tkinter_cl.create_input({'padx': 10, 'pady': 10}, {'padx': 10, 'pady': 10}, "Maximum Quantity Value")
y_label = tkinter_cl.create_input({'padx': 10, 'pady': 10}, {'padx': 10, 'pady': 10}, "Y Label")
title = tkinter_cl.create_input({'padx': 10, 'pady': 10}, {'padx': 10, 'pady': 10}, "Title of Graph")

graph = Graph()

# Attempt to connect to serial port
try:
    serial_cl = SerialClass('COM4', 9600, timeout=1)
    if not serial_cl.ser.is_open:
        raise Exception("Serial port is not open")
except Exception:
    serial_cl = None

def safe_serial_read():
    if serial_cl is None or not hasattr(serial_cl, 'ser') or not serial_cl.ser.is_open:
        messagebox.showerror("Serial Error", "Serial monitor is not connected!")
        return 0
    try:
        data = serial_cl.get_serial_print()
        return data if data else 0
    except Exception:
        messagebox.showerror("Serial Error", "Failed to read from serial monitor!")
        return 0

btn = tkinter_cl.create_button(
    'Show graph',
    lambda: graph.toggle_frame(
        min_quantity.get(),
        max_quantity.get(),
        tkinter_cl.root,
        safe_serial_read,
        y_label.get(),
        title.get()
    ),
    "Custom.TButton",
    {'pady': 10}
)

save_to_pdf_btn = tkinter_cl.create_button(
    'Save graph to pdf',
    lambda: graph.save_as_pdf('graph_output.pdf'),
    "Custom.TButton",
    {'pady': 10}
)

tkinter_cl.run_loop()