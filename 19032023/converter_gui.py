from tkinter import *
from tkinter import ttk

def calculate(*args):
    value = float(feet.get())
    meter.set(int(value*0.305))

root = Tk()
root.title('Unit Converter')
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

main_frame = ttk.Frame(root, padding='3 3 12 12')
main_frame.grid(column=0, row=0, sticky=(N, W, E, S))

feet = StringVar()
feet_entry = ttk.Entry(main_frame, width=10, textvariable=feet, font=('Arial', 25))
feet_entry.grid(column=2, row=1, sticky=(W, E))
feet_entry.focus()

meter = StringVar()
ttk.Label(main_frame, textvariable=meter, font=('Arial', 25)).grid(column=2, row=2, sticky=(W, E))

style = ttk.Style()
style.configure('W.TButton', font=('Arial', 25))

ttk.Button(main_frame, text='Calculate', command=calculate, style='W.TButton').grid(column=3, row=3, sticky=W)
ttk.Button(main_frame, text='Quit', command=root.destroy, style='W.TButton').grid(column=3, row=4, sticky=W)

ttk.Label(main_frame, text='Feet', font=('Arial', 25)).grid(column=3, row=1, sticky=W)
ttk.Label(main_frame, text='is equivalent to', font=('Arial', 25)).grid(column=1, row=2, sticky=E)
ttk.Label(main_frame, text='Meter', font=('Arial', 25)).grid(column=3, row=2, sticky=W)

for child in main_frame.winfo_children():
    child.grid_configure(padx=5, pady=5)

root.bind('<Return>', calculate)

root.mainloop()
