<<<<<<< HEAD
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
=======
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

    def create_input(self, parent, text, default=""):
        label = tk.Label(
            parent,
            text=text,
            font=self.font,
            fg="#22223B",
            bg=parent["bg"]
        )
        label.pack(anchor="w", pady=(10, 2), fill="x")
        input_field = tk.Entry(
            parent,
            font=self.font,
            fg="#22223B",
            bg="#FFFFFF",
            relief=tk.FLAT,
            highlightthickness=1,
            highlightbackground="#E0E1DD",
            bd=0,
            insertbackground="#22223B",
            width=30
        )
        input_field.insert(0, default)
        input_field.pack(fill="x", pady=(0, 10))
        return input_field

    def create_button(self, parent, text, command, btn_style):
        btn = tb.Button(
            parent,
            text=text,
            command=command,
            bootstyle=btn_style,
            style="Custom.TButton"
        )
        btn.pack(fill="x", pady=10)
        return btn

    def run_loop(self):
        self.root.mainloop()
 
# import tkinter as tk
# import ttkbootstrap as tb

# class TkintClass:
#     def __init__(self, title, dim, font, bg="#F5F7FA"):
#         self.font = font
#         self.bg = bg
#         self.root = tk.Tk()
#         self.root.title(title)
#         self.root.geometry(dim)
#         self.root.configure(bg=self.bg)

#     def run_loop(self):
#         self.root.mainloop()



>>>>>>> 8f0f523fbf85dd72c9bcf0d2a4245390005e7e71
