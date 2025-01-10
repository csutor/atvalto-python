from tkinter import *
from tkinter import ttk
from tkinter import messagebox

root = Tk()
root.title("Átváltó - főmenü")

def hossz():
    pass

def tomeg():
    pass

def ido():
    pass

hossz_btn = Button(root, text="Hossz", command=hossz)
tomeg_btn = Button(root, text="Tömeg", command=tomeg)
ido_btn = Button(root, text="Idő", command=ido)

hossz_btn.grid(column=0, row=0, padx=125, pady=25)
tomeg_btn.grid(column=0, row=1, padx=125, pady=25)
ido_btn.grid(column=0, row=2, padx=125, pady=25)

root.mainloop()