import tkinter
from tkinter import ttk

window = tkinter.Tk()

window.columnconfigure(0, weight=5)
window.columnconfigure(0, weight=5)

lista = ['Lapices', 'Cuadernos', 'Sacapuntas', 'Borradores', 'Marcadores', 'Crayolas', 'Resaltadores']
lista_items = tkinter.StringVar(value=lista)
listabox = tkinter.Listbox(window, height=20, listvariable=lista_items)
listabox.grid(column=0, row=0, sticky=tkinter.W, padx=50, pady=50)


window.mainloop()