from tkinter import *
from GraafilineLiides import *
global varv,tekst

def varvi_valik():
    varv="white"
    if tekst.get()!="":
        tekst.configure(bg="green")
        varv=tekst.get()
    else:
        tekst.configure(bg="blue")
    return varv

def figuur(varv:str):
    # global varv
    # varv=varvi_valik()
    valik=var.get()
    if valik==1:
        vaal(varv)
    elif valik==2:
        liblikas(varv)


aken=Tk()
aken.geometry("800x400")
aken.title("Graafikud")
pealkiri=Label(aken,text="Erinevad pildid Matplotlib abil", font="Calibri 24",fg="white", bg="Slategray", pady=20, width=100)

var=IntVar()
r1=Radiobutton(aken,text="Vaal", font="Calibri 18", variable=var, value=1, command=lambda:figuur(varv=varvi_valik()))
r2=Radiobutton(aken,text="Liblikas", font="Calibri 18", variable=var, value=2, command=lambda:figuur(varv=varvi_valik()))

tekst=Entry(aken, font="Calibri 24", fg="red", bg="yellow", width=50)

nupp=Button(aken, text="Värvi valik", font="Calibri 24", command=varvi_valik())



pealkiri.pack() #place(x=...., y=...), grid(column=..., row...)
tekst.pack()
nupp.pack()
r1.pack()
r2.pack()
aken.mainloop()
