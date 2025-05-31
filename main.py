from ttkbootstrap import PRIMARY
from util.graph import Graph
from util.serial_comm import SerialClass
from util.tkint import TkintClass

font_style = ('Arial', 16)

tkinter_cl = TkintClass('Graph tool', '1000x666', font_style)
min_quantity = tkinter_cl.create_input({'padx':10, 'pady':10}, {'padx':10, 'pady':10})
max_quantity = tkinter_cl.create_input({'padx':10, 'pady':10}, {'padx':10, 'pady':10})
btn = tkinter_cl.create_button('Show graph', lambda: graph.toggle_frame(min_quantity.get(), max_quantity.get(), tkinter_cl.root, lambda :
serial_cl.get_serial_print()), PRIMARY, {'pady':10})


graph = Graph()
serial_cl = SerialClass('COM4', 9600, timeout=1)

tkinter_cl.run_loop()