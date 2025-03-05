from tkinter import *
from PIL import Image, ImageTk
from tkinter import font

aken=Tk()
aken.geometry("1080x1920")
aken.wm_title("Numeroloogia Pythagorase ruut")
aken.resizable(width=False, height=False)
aken.image=PhotoImage(file="09 - Iseseisev praktiline töö/bg.png")
bg=Label(aken, image=aken.image)
bg.grid(row=0, column=0)
aken.iconbitmap(default="09 - Iseseisev praktiline töö/icon.ico")


title=Label(aken, text="Numeroloogia: Pythagorase ruut", font="Times 25 bold", fg="white", bg="#0c0623", width=25)
title.place(relx=.4, rely=.1, anchor="n")

tekst=Label(aken, text="Proovige arvutada oma Pythagorase ruut ja avastage, milliseid saladusi teie numbrid peidavad!", font="Times 16", fg="white", bg="#0c0623", wraplength=500, width=42)
tekst.place(relx=.4, rely=.2, anchor="n")

syn=Label(aken, text="Sisesta oma sünniaeg!", font="Times 16", fg="white", bg="#0c0623")
syn.place(relx=.4, rely=.4, anchor="n")

synentry=Entry(aken, text="dd.mm.yyyy", font="Times 16")
synentry.place(relx=.4, rely=.5, anchor="n")
synentry.insert(0, "dd.mm.yyyy")

aken.mainloop()