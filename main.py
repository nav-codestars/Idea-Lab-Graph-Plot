from ttkbootstrap import Style, PRIMARY
from util.graph import Graph
from util.serial_comm import SerialClass
from util.tkint import TkintClass
from tkinter import messagebox
import tkinter as tk

def change_min_max_avg_values(min_val, max_val, avg_val):
    if(min_val is not None):
        min_value.config(text=f"Min: {min_val}")
    if(max_val is not None):
        max_value.config(text=f"Max: {max_val}")
    if(avg_val is not None):
        avg_value.config(text=f"Avg: {avg_val:.2f}")

font_style = ('Segoe UI', 14)
tkinter_cl = TkintClass('Graph tool', '1500x1000', font_style, bg="#F5F7FA")

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
right_frame = tk.Frame(tkinter_cl.root, bg="#FFFFFF", width=350, height=800)
right_frame.pack(fill=None, expand=True)
right_frame.pack_propagate(False)

# Spacer to push input fields to the bottom
spacer = tk.Frame(right_frame, bg="#FFFFFF")
spacer.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

# Input frame at the bottom of right_frame
input_frame = tk.Frame(right_frame, bg="#FFFFFF")
input_frame.pack(side=tk.BOTTOM, fill=tk.X, padx=40, pady=40)

# --- COM Port ComboBox ---
from ttkbootstrap.widgets import Combobox

def get_com_ports():
    return [port.device for port in SerialClass.get_ports()]

com_ports = get_com_ports()
selected_port = tk.StringVar(value=com_ports[0] if com_ports else "")

com_label = tk.Label(input_frame, text="Select COM Port:", bg="#FFFFFF", font=font_style)
com_label.pack(anchor="w", pady=(0, 5))

com_combo = Combobox(
    input_frame,
    textvariable=selected_port,
    values=com_ports,
    font=font_style,
    bootstyle="primary"
)
com_combo.pack(fill=tk.X, pady=(0, 10))

# Input fields and buttons in input_frame
min_quantity = tkinter_cl.create_input(input_frame, "Minimum Quantity Value", default="10")
max_quantity = tkinter_cl.create_input(input_frame, "Maximum Quantity Value", default="100")
y_label = tkinter_cl.create_input(input_frame, "Y Label", default="Temeprature(°C)")
title = tkinter_cl.create_input(input_frame, "Title of Graph", default="Real-time Temperature Measurement")

min_value = tk.Label(input_frame, text="", font=("Helvetica", 16))
max_value = tk.Label(input_frame, text="", font=("Helvetica", 16))
avg_value = tk.Label(input_frame, text="", font=("Helvetica", 16))

min_value.pack(anchor="center", fill="x", pady=(10, 0))
max_value.pack(anchor="center", fill="x", pady=(0, 0)) 
avg_value.pack(anchor="center", fill="x", pady=(0, 10))
serial_cl = None  # Will be initialized on button click

def button_click_action():
    global serial_cl
    port = selected_port.get()
    if not port:
        messagebox.showerror("Serial Error", "No COM port selected!")
        return
    if serial_cl is None or not hasattr(serial_cl, 'ser') or not getattr(serial_cl.ser, 'is_open', False):
        try:
            serial_cl = SerialClass(port, 9600, timeout=1)
        except Exception as e:
            messagebox.showerror("Serial Error", f"Could not open {port}:\n{e}")
            return
    if serial_cl is None or not hasattr(serial_cl, 'ser') or not getattr(serial_cl.ser, 'is_open', False):
        messagebox.showerror("Serial Error", "Serial monitor is not connected!")
        return
    graph.toggle_frame(
        min_quantity.get(),
        max_quantity.get(),
        left_frame,
        serial_cl.get_serial_print,
        y_label.get(),
        title.get(),
        change_min_max_avg_values
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

graph = Graph()

def window_close():
    tkinter_cl.running = False
    tkinter_cl.root.destroy()
    global serial_cl
    if serial_cl is not None:
        serial_cl.close_serial()
    exit(0)

tkinter_cl.root.protocol("WM_DELETE_WINDOW", window_close)

tkinter_cl.run_loop()




