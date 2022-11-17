import tkinter
from tkinter import ttk

window = tkinter.Tk()

# window.columnconfigure(0, weight=1)
# window.columnconfigure(0, weight=3)


selected = tkinter.StringVar()
r1 = ttk.Radiobutton(window, text="Si", value=1, variable=selected)
r2 = ttk.Radiobutton(window, text="No", value=2, variable=selected)

r1.grid(column=0, row=0, padx=5, pady=5)
r2.grid(column=0, row=1, padx=5, pady=5)


def reiniciarProg(reinicio):
    print("Se reiniciara el programa")
    


boton = tkinter.Button(window, text="Reinicio")
boton.grid(column=2, row=3, padx=5, pady=5)
boton.bind('<Button-1>', reiniciarProg)

window.mainloop()
