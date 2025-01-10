from tkinter import *
from tkinter import ttk
from tkinter import messagebox

root = Tk()
root.title("Átváltó - Főmenü")

def hossz():
    def close():
        hossz_root.destroy()
    mert = ["Méter", "Kilóméter", "Mérföld", "Yard"]

    hossz_root = Toplevel()
    hossz_root.title("Átváltó - Hossz")
    entry1 = Entry(hossz_root, width=10)
    mertegyseg1 = StringVar()
    dropdown1 = ttk.Combobox(hossz_root, textvariable=mertegyseg1, values=mert, state="readonly")
    dropdown1.set(mert[0])
    mertegyseg2 = StringVar()
    dropdown2 = ttk.Combobox(hossz_root, textvariable=mertegyseg2, values=mert, state="readonly")
    dropdown2.set(mert[0])
    count_btn = Button(hossz_root, text="Számol")
    result_lbl = Label(hossz_root, text="Eredmény: ")
    exit_btn = Button(hossz_root, text="Kilép", command=close)

    entry1.grid(column=0, row=0, padx=125, pady=25)
    dropdown1.grid(column=0, row=1, padx=125, pady=10)
    dropdown2.grid(column=0, row=2, padx=125, pady=10)
    result_lbl.grid(column=0, row=3, padx=125, pady=25)
    exit_btn.grid(column=0, row=4, padx=125, pady=25)

    hossz_root.mainloop()

def tomeg():
    pass

def ido():
    pass

hossz_btn = Button(root, text="Hossz", command=hossz)
tomeg_btn = Button(root, text="Tömeg", command=tomeg)
ido_btn = Button(root, text="Idő", command=ido)
exit_btn = Button(root, text="Kilépés", command=exit)

hossz_btn.grid(column=0, row=0, padx=125, pady=25)
tomeg_btn.grid(column=0, row=1, padx=125, pady=25)
ido_btn.grid(column=0, row=2, padx=125, pady=25)
exit_btn.grid(column=0, row=3, padx=125, pady=25)

root.mainloop()