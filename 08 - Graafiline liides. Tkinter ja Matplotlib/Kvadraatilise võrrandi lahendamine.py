from tkinter import *
from Grafik import *

def lahendus():
    try:
        a = blok1.get()
        b = blok3.get()
        c = blok5.get()
    except ValueError:
        tulemus.config(text="Пожалуйста, введите корректные числа", fg="white", font="Times_New_Roman 14")
        return
    if a=="":
        blok1.config(bg="black")
    else:
        blok1.config(bg="Slategray")
    if b=="":
        blok3.config(bg="black")
    else:
        blok3.config(bg="Slategray")
    if c=="":
        blok5.config(bg="black")
    else:
        blok5.config(bg="Slategray")
    if a != "" and b != "" and c != "":
        try:
            a = float(blok1.get())
            b = float(blok3.get())
            c = float(blok5.get())
        except:
            tulemus.config(text="Пожалуйста, введите корректные числа", fg="white", font="Times_New_Roman 14")
            return
        D=b**2-4*a*c
        if D>0:
            x1=(-b+D**0.5)/(2*a)
            x2=(-b-D**0.5)/(2*a)
            tulemus.config(text=f"D={D}\nx1={x1}\nx2={x2}", fg="white", font="Times_New_Roman 14")
        elif D==0:
            x=-b/2*a
            tulemus.config(text=f"D={D}\nx1={x}", fg="white", font="Times_New_Roman 14")
        elif D<0:
            tulemus.config(text=f"Не имеет корней", fg="white", font="Times_New_Roman 14")

def show_grafik():
    try:
        a=float(blok1.get())
        b=float(blok3.get())
        c=float(blok5.get())
        grafik(a, b, c)
    except ValueError:
        tulemus.config(text="Пожалуйста, введите корректные числа", fg="white", font="Times_New_Roman 14")

aken=Tk()
aken.geometry("800x400")
aken.title("Решение квадратного уравнения")

pealkiri=Label(aken,text="Решение квадратного уравнения", font="Times_New_Roman 24",fg="white", bg="Slategray", pady=20, width=80)
pealkiri.pack()

blok1=Entry(aken,font="Times_New_Roman 14", fg="white", bg="slategray",width=3)
blok1.place(x=70,y=120)

blok2=Label(aken,text="x**2+", fg="black", font="Times_New_Roman 14")
blok2.place(x=110,y=120)

blok3=Entry(aken,font="Times_New_Roman 14", fg="white", bg="slategray",width=3)
blok3.place(x=170,y=120)

blok4 = Label(aken, text="x +", fg="black", font="Times_New_Roman 14")
blok4.place(x=210, y=120)

blok5 = Entry(aken, font="Times_New_Roman 14", fg="white", bg="slategray", width=3)
blok5.place(x=250, y=120)

blok6 = Label(aken, text="= 0", fg="black", font="Times_New_Roman 14")
blok6.place(x=300, y=120)

nupp=Button(aken, text="Решить", font="Times_New_Roman 24", fg="white", bg="Slategray", activebackground="black", activeforeground="white", command=lahendus)
nupp.place(x=350, y=100)

tulemus= Label(aken, text="Решение", fg="white", bg="black", font="Times_New_Roman 14", width=38)
tulemus.place(x=70, y=190)

nupp2=Button(aken, text="График", font="Times_New_Roman 24", fg="white", bg="Slategray", activebackground="black", activeforeground="white", command=show_grafik)
nupp2.place(x=500, y=100)

aken.mainloop()