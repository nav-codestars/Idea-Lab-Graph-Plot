import tkinter as tk
import ttkbootstrap as tb

class TkintClass:
    def __init__(self, title, dim, font):
        self.font = font
        self.root = tk.Tk()
        self.root.title(title)
        self.root.geometry(dim)


    def create_input(self, label_constraints, input_constrants):
        tk.Label(self.root, text="Maximum Quantity Value", font=self.font).pack(**label_constraints)
        input_field = tk.Entry(self.root, font=self.font)
        input_field.insert(0, "10")
        input_field.pack(**input_constrants)
        return input_field



    def create_button(self, text, command, btn_style, button_constraints):
        btn = tb.Button(self.root, text="Show Graph", command=command, bootstyle=btn_style)
        btn.pack(**button_constraints)
        return btn


    def run_loop(self):
        self.root.mainloop()