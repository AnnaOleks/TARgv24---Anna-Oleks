from tkinter import *
from PIL import Image, ImageTk
from tkinter import font
import re   
from tkinter import messagebox

def clearsynentry(event):
    if synentry.get()=="dd.mm.yyyy":
        synentry.delete(0, END)

def kuupaevakontroll():
    kuupaev=synentry.get()
    vorm=r"^([0-2][0-9]|3[01])\.(0[1-9]|1[0-2])\.\d{4}$"
    if re.fullmatch(vorm, kuupaev):
        messagebox.showinfo("Informatsioon", "Õige kuupaev")
        synentry.config(bg="#fdddeb")
    else:
        synentry.config(bg="#c8d3f8")
        messagebox.showinfo("Informatsioon", "Vale kuupaev")

def esimenerida():
    kuupaev=synentry.get()
    rida_list=list(kuupaev)
    tulemus.config(text=f"Sinu tulemus: \n {''.join(rida_list)}")

aken=Tk()
aken.geometry("450x800")
aken.wm_title("Numeroloogia Pythagorase ruut")
aken.resizable(width=False, height=False)

orig_bg=Image.open(r"09 - Iseseisev praktiline töö/bg.png")
resize_bg=orig_bg.resize((450,800))
bg=ImageTk.PhotoImage(resize_bg)

labelbg=Label(aken, image=bg)
labelbg.place(x=0, y=0, relwidth=1, relheight=1)

frame=Frame(aken, bg="white", borderwidth=5, width=350, height=400, highlightbackground="#c8d3f8", highlightcolor="#fdddeb", highlightthickness=3)
frame.place(relx=0.5, rely=0.05, anchor="n", width=350)

title=Label(frame, text="Numeroloogia:\n Pythagorase ruut", font="Times 20 bold", fg="black", bg="white")
title.pack(pady=10)

tekst=Label(frame, text="Proovige arvutada oma Pythagorase ruut ja avastage, milliseid saladusi teie numbrid peidavad!", font="Times 12", fg="black", bg="white", wraplength=300)
tekst.pack(pady=10)

syn=Label(frame, text="Sisesta oma sünniaeg!", font="Times 12 bold", fg="black", bg="white")
syn.pack(pady=10)

synentry_frame=Frame(frame, bg="white")
synentry_frame.pack(pady=10)

synentry=Entry(synentry_frame, font="Times 12 bold", bg="#fdddeb", justify=CENTER)
synentry.pack(side=LEFT, padx=5, fill="y")
synentry.insert(0, "dd.mm.yyyy")
synentry.bind("<FocusIn>", clearsynentry)

arvuta=Button(synentry_frame, text="Arvuta", font="Times 12 bold", bg="#c8d3f8", command=lambda:[kuupaevakontroll(), esimenerida()])
arvuta.pack(side=LEFT, padx=5)

tabel=Frame(aken, bg="white", borderwidth=5, width=350, height=350, highlightbackground="#c8d3f8", highlightcolor="#fdddeb", highlightthickness=3)
tabel.place(relx=0.5, rely=0.4, anchor="n", width=350)

tulemus=Label(tabel, text="Sinu tulemus:", font="Times 12 bold", bg="white")
tulemus.grid(row=1, column=1, columnspan=3, ipady=10)

nupp1=Button(tabel, text=1, font="Times 12 bold", bg="#c8d3f8", width=10)
nupp1.grid(row=2, column=1, padx=5, pady=5)

nupp2=Button(tabel, text=2, font="Times 12 bold", bg="#fdddeb", width=10)
nupp2.grid(row=3, column=1, padx=5, pady=5)

nupp3=Button(tabel, text=3, font="Times 12 bold", bg="#c8d3f8", width=10)
nupp3.grid(row=4, column=1, padx=5, pady=5)

nupp4=Button(tabel, text=4, font="Times 12 bold", bg="#fdddeb", width=10)
nupp4.grid(row=2, column=2, padx=5, pady=5)

nupp5=Button(tabel, text=5, font="Times 12 bold", bg="#c8d3f8", width=10)
nupp5.grid(row=3, column=2, padx=5, pady=5)

nupp6=Button(tabel, text=6, font="Times 12 bold", bg="#fdddeb", width=10)
nupp6.grid(row=4, column=2, padx=5, pady=5)

nupp7=Button(tabel, text=7, font="Times 12 bold", bg="#c8d3f8", width=10)
nupp7.grid(row=2, column=3, padx=5, pady=5)

nupp8=Button(tabel, text=8, font="Times 12 bold", bg="#fdddeb", width=10)
nupp8.grid(row=3, column=3, padx=5, pady=5)

nupp9=Button(tabel, text=9, font="Times 12 bold", bg="#c8d3f8", width=10)
nupp9.grid(row=4, column=3, padx=5, pady=5)

aken.mainloop()