
from tkinter import*
from PIL import *
from PIL import ImageTk



def Lahenda():
	pass

def Graafik():
	pass

def aken_pack():
	aken=Tk()
	aken.geometry("650x260")
	aken.title("Ruutvorrand")
	aken.resizable(False,False)

	original_image= Image.open(r"08 - Graafiline liides. Tkinter ja Matplotlib/fon.jpg")
	resized_image=original_image.resize((650,260))
	bgimage=ImageTk.PhotoImage(resized_image)

	lblLBG=Label(aken,image=bgimage)
	lblLBG.place(x=0, y=0)

	f1=Frame(aken,width=650,height=260)
	f1.pack()

	lbl=Label(f1,text="Ruutvorrandite lahendamine", font="Calibri 26", fg="green", bg="lightblue")
	lbl.pack(side=TOP)

	lbl_vastus=Label(f1,text="Lahendamine", heidht=4, width=60, font="Calibri 26", bg="yellow")
	lbl_vastus.pack(side=BOTTOM)

	lbl_a=Entry(f1, font="Calibri 26", fg="green", bg="lightblue", width=3)
	lbl_a.pack(side=LEFT)

	x2=Label(f1,text="x^2+", font="Calibri 26", fg="green", padx=10)
	x2.pack(LEFT)

	x=Label(f1,text="x+", font="Calibri 26", fg="green", padx=10)
	x.pack(LEFT)

	lbl_c=Entry(f1, font="Calibri 26", fg="green", bg="lightblue", width=3)
	lbl_c.pack(side=LEFT)

	y=Label(f1,text="x+", font="Calibri 26", fg="green", padx=10)
	y.pack(LEFT)

	btn_Lahenda=Button(f1,text="Lahenda", font="Calibri 26", fg="green", command=lahenda)
	btn_Lahenda.pack(side=LEFT)

	btn_Graafik=Button(f1,text="Grafik", font="Calibri 26", fg="green", command=Graafik)
	btn_Graafik.pack(side=LEFT)


	aken_pack.mainloop()

aken_pack()