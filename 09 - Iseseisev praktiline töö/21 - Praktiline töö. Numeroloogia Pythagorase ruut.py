from ast import Lambda
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
        return True
    else:
        synentry.config(bg="#c8d3f8")
        messagebox.showinfo("Informatsioon", "Vale kuupaev")
        return False

def esimenerida():
    global rida_list
    global rida1
    kuupaev=synentry.get()
    rida_list=list(kuupaev)
    for mark in rida_list:
        if "." in rida_list:
            mark_index=rida_list.index(".")
            rida_list.pop(mark_index)
        if "0" in rida_list:
            mark_index=rida_list.index("0")
            rida_list.pop(mark_index)
    rida1=''.join(rida_list)
    return rida1

def esimenetooarv():
    global rida_list
    global arv1
    kuupaev=synentry.get()
    rida_list=list(kuupaev)
    paev1=int(rida_list[0])
    paev2=int(rida_list[1])
    kuu1=int(rida_list[3])
    kuu2=int(rida_list[4])
    arv1=paev1+paev2+kuu1+kuu2
    return arv1

def teinetooarv():
    global rida_list
    global aasta
    aasta1=int(rida_list[6])
    aasta2=int(rida_list[7])
    aasta3=int(rida_list[8])
    aasta4=int(rida_list[9])
    aasta=aasta1+aasta2+aasta3+aasta4
    return aasta

def kolmastooarv(): 
    global arv3
    arv1 = esimenetooarv()
    aasta = teinetooarv()
    arv3=arv1+aasta
    return arv3

def neljastooarv():
    global arv4
    arv3=kolmastooarv()
    arv3_str=str(arv3)
    arv4=int(arv3_str[0])+int(arv3_str[1])
    return arv4

def viiestooarv():
    global rida_list
    arv3=kolmastooarv()
    arv5=arv3-2*int(rida_list[0])
    return arv5

def kuuestooarv():
    global arv6
    arv5=viiestooarv()
    arv5_str=str(arv5)
    arv6=int(arv5_str[0])+int(arv5_str[1])
    return arv6

def teinerida():
    global rida2_list
    global rida2
    arv3=kolmastooarv()
    arv4=neljastooarv()
    arv5=viiestooarv()
    arv6=kuuestooarv()
    rida2_list=[arv3,arv4,arv5,arv6]
    rida2=""
    for arv in rida2_list:
        rida2+=str(arv)
    return rida2

def readarvud():
    if kuupaevakontroll():
        rida1=esimenerida()
        arv1=esimenetooarv()
        aasta=teinetooarv()
        arv3=kolmastooarv()
        arv4=neljastooarv()
        arv5=viiestooarv()
        arv6=kuuestooarv()
        rida2=teinerida()
        tulemus.config(text=f"Sinu tulemus: \nEsimene rida: {rida1}\nTeine rida: {rida2}\n\nEsimene tööarv: {arv1}\nTeine tööarv: {aasta}\nKolmas tööarv: {arv3}\nNeljas tööarv: {arv4}\nViies tööarv: {arv5}\nKuues tööarv: {arv6}")
        tabelitaitmine()
        vahe.grid(row=5,column=1)
        vastus.grid(row=6,column=2)

def tabelitaitmine():
    global rida_list
    global rida2_list
    rida2_list2 = list(rida2)
    count={str(i):0 for i in range(1,10)}
    for arv in rida_list:
        if arv in count:
            count[arv]+=1
    for arv in rida2_list2:
        if arv in count:
            count[arv]+=1
    nuppud={
        1: nupp1,
        2: nupp2,
        3: nupp3,
        4: nupp4,
        5: nupp5,
        6: nupp6,
        7: nupp7,
        8: nupp8,
        9: nupp9,
    }
    for i in range(1, 10):
        global nupp_text
        nupp_text = f"ei ole ({str(i)})" if count[str(i)] == 0 else str(i) * count[str(i)]
        nuppud[i].configure(text=nupp_text)  

def analuus():
    global number_tahendus
    number_tahendus={}
    tahendus_number={}
    numbrid=[]
    tahendused=[]
    with open(r"09 - Iseseisev praktiline töö\Text.txt","r",encoding="utf-8") as file:
        for line in file:
            k,v=line.strip().split('-',1)
            number_tahendus[k]=v
            tahendus_number[v]=k
            numbrid.append(k)
            tahendused.append(v)

def tulemuseaken():
    lisaaken=Tk()
    lisaaken.geometry("450x800")
    lisaaken.title("Numeroloogia Pythagorase ruut")
    lisaaken.resizable(width=False, height=False)

    orig_lisabg=Image.open(r"09 - Iseseisev praktiline töö/bg.png")
    resize_lisabg=orig_lisabg.resize((450,800))
    bg=ImageTk.PhotoImage(resize_lisabg)

    labelbg=Label(lisaaken, image=bg)
    labelbg.place(x=0, y=0, relwidth=1, relheight=1)

    lisaframe=Frame(lisaaken, bg="white", borderwidth=5, width=350, height=400, highlightbackground="#c8d3f8", highlightcolor="#fdddeb", highlightthickness=3)
    lisaframe.place(relx=0.5, rely=0.05, anchor="n", width=350)


    

aken=Tk()
aken.geometry("450x800")
aken.title("Numeroloogia Pythagorase ruut")
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

arvuta=Button(synentry_frame, text="Arvuta", font="Times 12 bold", bg="#c8d3f8", command=lambda:(kuupaevakontroll() and readarvud()))
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

vahe=Label(tabel, text=" ")
vahe.grid(row=5,column=1)
vahe.grid_forget()

vastus=Button(tabel, text="Tulemus", font="Times 12 bold", bg="#c8d3f8", width=10, command = lambda: tulemuseaken())
vastus.grid(row=6, column=2)
vastus.grid_forget()

aken.mainloop()