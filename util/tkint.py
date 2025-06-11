import tkinter as tk
import ttkbootstrap as tb

class TkintClass:
    def __init__(self, title, dim, font, bg="#F5F7FA"):
        self.font = font
        self.bg = bg
        self.root = tk.Tk()
        self.root.title(title)
        self.root.geometry(dim)
        self.root.configure(bg=self.bg)

    def create_input(self, label_constraints, input_constraints, text):
        label = tk.Label(
            self.root,
            text=text,
            font=self.font,
            fg="#22223B",
            bg=self.bg
        )
        label.pack(**label_constraints)
        input_field = tk.Entry(
            self.root,
            font=self.font,
            fg="#22223B",
            bg="#FFFFFF",
            relief=tk.FLAT,
            highlightthickness=1,
            highlightbackground="#E0E1DD"
        )
        input_field.insert(0, "10")
        input_field.pack(**input_constraints)
        return input_field

    def create_button(self, text, command, btn_style, button_constraints):
        btn = tb.Button(
            self.root,
            text=text,
            command=command,
            bootstyle=btn_style,
            style="Custom.TButton"
        )
        btn.pack(**button_constraints)
        return btn

    def run_loop(self):
        self.root.mainloop()
