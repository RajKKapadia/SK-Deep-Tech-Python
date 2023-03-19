from tkinter import *
from tkinter import ttk

root = Tk(
    className='MyFirstGUI'
)

frm = ttk.Frame(root, padding=10)
frm.grid()
ttk.Label(frm, text='Hello world...').grid(row=0, column=0)
ttk.Button(frm, text='Quit', command=root.destroy).grid(row=0, column=1)

root.mainloop()
