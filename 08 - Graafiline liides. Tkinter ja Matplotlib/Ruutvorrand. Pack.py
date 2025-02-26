
from tkinter import*
from PIL import *
from PIL import Image, ImageTk
from tkinter import messagebox
import matplotlib.pyplot as plt
import numpy as np


global lbl_a, lbl_b, lbl_c, lbl_vastus

def Lahenda():
	try:
		a=float(lbl_a.get())
		b=float(lbl_b.get())
		c=float(lbl_c.get())

		D=b**2-4*2*c

		if D>0:
			x1=round((-b+(D**(1/2)))/(2*a),2)
			x2=round((-b-(D**(1/2)))/(2*a),2)
			lbl_vastus.configure(text=f"D>0 --> 2 решения: \n x1={x1}\n x2={x2}")

		elif D==0:
			x=round((-b/(2*a)),2)
			lbl_vastus.configure(text=f"D=0 -->1 решение: \n x={x}")

		else:
			lbl_vastus.configure(text="Решений нет")
	except:
		messagebox.showerror("error","error")

		#-----СПИСАТЬ КОД У ОЛЕЙНИК------

def Graafik():
	a=float(lbl_a.get())
	b=float(lbl_b.get())
	c=float(lbl_c.get())

	D=b**2-4*2*c
	y=a*x**2+b*x*c

	if D>0:
		x=np.linespase(x1-2,x2+2,100)
	elif D==0:
		x=np.linspase(-20,20,100)
	else:
		lbl_vastus.configure(text="Решений нет")

	plt.plot(x,y, label=(f"{a}x2 + {b}x + {c}"))
	plt.axhline(0, color="black", linemidth=0.5)
	plt.axvline(0, color="black", linemidth=0.5)
	plt.grid()
	plt.legend()
	plt.show

	pass

def entrycolor(event):
	i=lbl_a.get()
	if i == "":
		lbl_a.configure(bg="red")
	else:
		lbl_a.congigure(bg="slategray")

	i=lbl_b.get()
	if i == "":
		lbl_b.configure(bg="red")
	else:
		lbl_b.congigure(bg="slategray")

	i=lbl_c.get()
	if i == "":
		lbl_c.configure(bg="red")
	else:
		lbl_c.congigure(bg="slategray")

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
	f1.pack(side=TOP)

	lbl=Label(f1,text="Ruutvorrandite lahendamine", font="Calibri 26", fg="green", bg="lightblue")
	lbl.pack(side=TOP)

	lbl_vastus=Label(f1,text="Lahendamine", height=4, width=60, font="Calibri 26", bg="yellow")
	lbl_vastus.pack(side=BOTTOM)

	lbl_a=Entry(f1, font="Calibri 26", fg="green", bg="lightblue", width=3)
	lbl_a.pack(side=LEFT)

	x2=Label(f1,text="x^2+", font="Calibri 26", fg="green", padx=10)
	x2.pack(side=LEFT)

	lbl_b=Entry(f1, font="Calibri 26", fg="green", bg="lightblue", width=3)
	lbl_b.pack(side=LEFT)

	x=Label(f1,text="x+", font="Calibri 26", fg="green", padx=10)
	x.pack(side=LEFT)

	lbl_c=Entry(f1, font="Calibri 26", fg="green", bg="lightblue", width=3)
	lbl_c.pack(side=LEFT)

	y=Label(f1,text="x+", font="Calibri 26", fg="green", padx=10)
	y.pack(side=LEFT)

	btn_Lahenda=Button(f1,text="Lahenda", font="Calibri 26", fg="green", command=Lahenda)
	btn_Lahenda.pack(side=LEFT)

	btn_Graafik=Button(f1,text="Grafik", font="Calibri 26", fg="green", command=Graafik)
	btn_Graafik.pack(side=LEFT)


	aken.mainloop()

#aken_pack()

def aken_grid():
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
	f1.pack(side=TOP)

	lbl=Label(f1,text="Ruutvorrandite lahendamine", font="Calibri 26", fg="green", bg="lightblue")
	lbl.grid(row=0, column=0, columnspan=8)

	lbl_vastus=Label(f1,text="Lahendamine", height=4, width=60, font="Calibri 26", bg="yellow")
	lbl_vastus.grid(row=2, column=0, columnspan=8)

	lbl_a=Entry(f1, font="Calibri 26", fg="green", bg="lightblue", width=3)
	lbl_a.grid(row=1, column=0)

	x2=Label(f1,text="x^2+", font="Calibri 26", fg="green", padx=10)
	x2.grid(row=1, column=1)

	lbl_b=Entry(f1, font="Calibri 26", fg="green", bg="lightblue", width=3)
	lbl_b.grid(row=1, column=2)

	x=Label(f1,text="x+", font="Calibri 26", fg="green", padx=10)
	x.grid(row=1, column=3)

	lbl_c=Entry(f1, font="Calibri 26", fg="green", bg="lightblue", width=3)
	lbl_c.grid(row=1, column=4)

	y=Label(f1,text="x+", font="Calibri 26", fg="green", padx=10)
	y.grid(row=1, column=5)

	btn_Lahenda=Button(f1,text="Lahenda", font="Calibri 26", fg="green", command=Lahenda)
	btn_Lahenda.grid(row=1, column=6)

	btn_Graafik=Button(f1,text="Grafik", font="Calibri 26", fg="green", command=Graafik)
	btn_Graafik.grid(row=1, column=7)


	aken.mainloop()

aken_grid()