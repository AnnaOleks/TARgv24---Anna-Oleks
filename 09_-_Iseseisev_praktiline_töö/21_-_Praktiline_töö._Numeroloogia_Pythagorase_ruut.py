from tkinter import *
from PIL import Image, ImageTk
from tkinter import font
import re   
from tkinter import messagebox
from datetime import *
from email.message import EmailMessage
import smtplib, ssl


global textlbl1, synentry

def clearsynentry(event):
    if synentry.get()=="dd.mm.yyyy":
        synentry.delete(0, END)

def kuupaevakontroll():
    kuupaev=synentry.get()
    vorm=r"^([0-2][0-9]|3[01])\.(0[1-9]|1[0-2])\.\d{4}$"
    if not re.fullmatch(vorm, kuupaev):
        synentry.config(bg="#c8d3f8")
        messagebox.showinfo("Informatsioon", "Vale kuupaeva formaat.")
    else: 
        try:
            datetime.strptime(kuupaev, "%d.%m.%Y")
            synentry.config(bg="#fdddeb")
            return True
        except:
            synentry.config(bg="#c8d3f8")
            messagebox.showinfo("Informatsioon", "Sellist kuupäeva ei ole")
            return False

def esimenerida():
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
    global nupp_text
    global nupunumbrid
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
    nupunumbrid=[]
    for i in range(1, 10):
        global nupp_text
        nupp_text = f"ei ole ({str(i)})" if count[str(i)] == 0 else str(i) * count[str(i)]
        nuppud[i].configure(text=nupp_text) 
        nupunumbrid.append(nupp_text)
    return nupunumbrid

def failiavamine(fail):
    global number_tahendus
    number_tahendus={}
    tahendus_number={}
    numbrid=[]
    tahendused=[]
    with open(r"09_-_Iseseisev_praktiline_töö/Text.txt","r",encoding="utf-8") as file:
        for line in file:
            k,v=line.strip().split('-',1)
            number_tahendus[k]=v
            tahendus_number[v]=k
            numbrid.append(k)
            tahendused.append(v)
    return number_tahendus

def tulemuseaken():
    global textlbl1

    lisaaken=Toplevel()
    lisaaken.geometry("450x800")
    lisaaken.title("Sinu tulemus")
    lisaaken.resizable(width=False, height=False)

    orig_lisabg=Image.open(r"09_-_Iseseisev_praktiline_töö/bg.png")
    resize_lisabg=orig_lisabg.resize((450,800))
    bg=ImageTk.PhotoImage(resize_lisabg)
    lisaaken.bg=bg
    labelbg=Label(lisaaken, image=lisaaken.bg)
    labelbg.place(x=0, y=0, relwidth=1, relheight=1)

    lisaframe=Frame(lisaaken, bg="white", borderwidth=5, width=350, height=400, highlightbackground="#c8d3f8", highlightcolor="#fdddeb", highlightthickness=3)
    lisaframe.pack(padx=10, pady=10, expand=True)

    failiavamine("09_-_Iseseisev_praktiline_töö/Text.txt")
    
    textlbl1=Label(lisaframe, text=f"{number_tahendus['*1']}\n{number_tahendus[nupunumbrid[0]]}\n\n{number_tahendus['*2']}\n{number_tahendus[nupunumbrid[1]]}\n\n{number_tahendus['*3']}\n{number_tahendus[nupunumbrid[2]]}\n\n{number_tahendus['*4']}\n{number_tahendus[nupunumbrid[3]]}\n\n{number_tahendus['*5']}\n{number_tahendus[nupunumbrid[4]]}\n\n{number_tahendus['*6']}\n{number_tahendus[nupunumbrid[5]]}\n\n{number_tahendus['*7']}\n{number_tahendus[nupunumbrid[6]]}\n\n{number_tahendus['*8']}\n{number_tahendus[nupunumbrid[7]]}\n\n{number_tahendus['*9']}\n{number_tahendus[nupunumbrid[8]]}", bg="white", wraplength=350)
    textlbl1.pack(padx=10, pady=10)

    tulmeilile=Button(lisaframe, text="Soovin tulemust meilile saada", font="Times 12 bold", bg="#fdddeb", width=30, command=lambda: kiri())
    tulmeilile.pack(padx=10, pady=10, side="bottom")
    return textlbl1

def numbriaken(nup):
    global textlbl1
    numbriaken=Toplevel()
    numbriaken.geometry("450x800")
    numbriaken.title("Sinu tulemus")
    numbriaken.resizable(width=False, height=False)

    orig_numbg=Image.open(r"09_-_Iseseisev_praktiline_töö/bg.png")
    resize_numbg=orig_numbg.resize((450,800))
    bg=ImageTk.PhotoImage(resize_numbg)
    numbriaken.bg=bg
    labelbg=Label(numbriaken, image=numbriaken.bg)
    labelbg.place(x=0, y=0, relwidth=1, relheight=1)

    numframe=Frame(numbriaken, bg="white", borderwidth=5, width=350, height=300, highlightbackground="#c8d3f8", highlightcolor="#fdddeb", highlightthickness=3)
    numframe.pack(padx=10, pady=10, expand=True)

    seletuslb=Label(numframe, text=f"{numtahendus(nup)}", bg="white", wraplength=350)
    seletuslb.pack(padx=10, pady=10)

    numtulmeilile=Button(numframe, text="Soovin tulemust meilile saada", font="Times 12 bold", bg="#fdddeb", width=30, command=lambda: kiri())
    numtulmeilile.pack(padx=10, pady=10, side="bottom")
    
def numtahendus(nup):
    nupunumbrid=tabelitaitmine()
    failiavamine("09_-_Iseseisev_praktiline_töö/Text.txt")
    selet=number_tahendus[nupunumbrid[int(nup)-1]]
    return selet

def saadakiri():
    global textlbl1
    tulemuseaken()
    sender_email="annaoleks88@gmail.com"
    kellele=[email.strip() for email in mailentry.get().split(",")]
    kiri=textlbl1.cget("text")
    smtp_server="smtp.gmail.com"
    port=587
    password="xsiw uicd bpgw djpf"
    context=ssl.create_default_context()
    msg=EmailMessage()
    msg.set_content(kiri)
    msg['Subject']="Numeroloogia Pythagorase ruudu tulemus"
    msg['From']="Ana Oleks"
    msg['To']=",".join(kellele)
    try:
        server=smtplib.SMTP(smtp_server,port)
        server.starttls(context=context)
        server.login(sender_email,password)
        server.send_message(msg)
        messagebox.showinfo("Informatsioon", "Kiri oli saadetud")
    except Exception as e:
        messagebox.showerror("Tekkis viga!",e)
    finally:
        server.quit()

def kiri():
    global mailentry
    global nimientry

    kiriaken=Toplevel()
    kiriaken.geometry("450x800")
    kiriaken.title("Sinu tulemus")
    kiriaken.resizable(width=False, height=False)

    orig_kiribg=Image.open(r"09_-_Iseseisev_praktiline_töö/bg.png")
    resize_kiribg=orig_kiribg.resize((450,800))
    bg=ImageTk.PhotoImage(resize_kiribg)
    kiriaken.bg=bg
    labelbg=Label(kiriaken, image=kiriaken.bg)
    labelbg.place(x=0, y=0, relwidth=1, relheight=1)

    kiriframe=Frame(kiriaken, bg="white", borderwidth=5, width=100, height=400, highlightbackground="#c8d3f8", highlightcolor="#fdddeb", highlightthickness=3)
    kiriframe.pack(padx=10, pady=10, expand=True)

    nimi=Label(kiriframe, text="Sinu nimi: ", bg="white", font="Times 12 bold", fg="black", width=35, anchor="w")
    nimi.pack(padx=10, pady=10)

    nimientry=Entry(kiriframe, font="Times 12", fg="black", bg="#fdddeb", width=40)
    nimientry.pack(padx=10, pady=10)

    mail=Label(kiriframe, text="Sinu e-mail: ", bg="white", font="Times 12 bold", fg="black", width=35, anchor="w")
    mail.pack(padx=10, pady=10)

    mailentry=Entry(kiriframe, font="Times 12", fg="black", bg="#fdddeb", width=40)
    mailentry.pack(padx=10, pady=10)

    saada=Button(kiriframe, text="SAADA", font="Times 12 bold", fg="black", bg="#c8d3f8", width=10, command=lambda: (faililisamine() and saadakiri()))
    saada.pack(padx=10, pady=10)

def email_kontroll():
    if email_kontroll()==False:
        return
    emails=mailentry.get().split(",")
    for email in emails:
        email=email.strip()
        if "@" not in email or "." not in email:
            messagebox.showerror("Vale e-mail!", "Sul on viga e-mailis. Kontrolli")
            mailentry.configure(bg="#c8d3f8")
            return False
        else:
            mailentry.configure(bg="#fdddeb")
            return True

def faililisamine():
    global nimientry, mailentry, rida1, rida2, textlbl1, synentry
    if 'file' not in globals():
        fail = ""
    fail = "09_-_Iseseisev_praktiline_töö/pythagorase_andmed.txt"
    osaleja={"nimi":nimientry.get(),
           "mail":mailentry.get(),
           "sunnipaev":synentry.get(),
           "rida1":esimenerida(),
           "rida2":teinerida(),
           "tulemus":textlbl1.cget("text")}
    try:
        with open(fail,'a', encoding="utf-8-sig") as f:
            for key, value in osaleja.items():
                f.write(f"{key}: {value}\n")
        messagebox.showinfo("Informatsioon", "Andmed on salvestatud")
    except:
        messagebox.showinfo("Informatsioon", "Tekkis viga!")
    return fail

aken=Tk()
aken.geometry("450x800")
aken.title("Numeroloogia Pythagorase ruut")
aken.resizable(width=False, height=False)

orig_bg=Image.open(r"09_-_Iseseisev_praktiline_töö/bg.png")
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

nupp1=Button(tabel, text="1", font="Times 12 bold", bg="#c8d3f8", width=10, command=lambda: numbriaken("1"))
nupp1.grid(row=2, column=1, padx=5, pady=5)

nupp2=Button(tabel, text="2", font="Times 12 bold", bg="#fdddeb", width=10, command=lambda: numbriaken("2"))
nupp2.grid(row=3, column=1, padx=5, pady=5)

nupp3=Button(tabel, text="3", font="Times 12 bold", bg="#c8d3f8", width=10, command=lambda: numbriaken("3"))
nupp3.grid(row=4, column=1, padx=5, pady=5)

nupp4=Button(tabel, text="4", font="Times 12 bold", bg="#fdddeb", width=10, command=lambda: numbriaken("4"))
nupp4.grid(row=2, column=2, padx=5, pady=5)

nupp5=Button(tabel, text="5", font="Times 12 bold", bg="#c8d3f8", width=10, command=lambda: numbriaken("5"))
nupp5.grid(row=3, column=2, padx=5, pady=5)

nupp6=Button(tabel, text="6", font="Times 12 bold", bg="#fdddeb", width=10, command=lambda: numbriaken("6"))
nupp6.grid(row=4, column=2, padx=5, pady=5)

nupp7=Button(tabel, text="7", font="Times 12 bold", bg="#c8d3f8", width=10, command=lambda: numbriaken("7"))
nupp7.grid(row=2, column=3, padx=5, pady=5)

nupp8=Button(tabel, text="8", font="Times 12 bold", bg="#fdddeb", width=10, command=lambda: numbriaken("8"))
nupp8.grid(row=3, column=3, padx=5, pady=5)

nupp9=Button(tabel, text="9", font="Times 12 bold", bg="#c8d3f8", width=10, command=lambda: numbriaken("9"))
nupp9.grid(row=4, column=3, padx=5, pady=5)

vahe=Label(tabel, text=" ")
vahe.grid(row=5,column=1)
vahe.grid_forget()

vastus=Button(tabel, text="Tulemus", font="Times 12 bold", bg="#c8d3f8", width=10, command = lambda: tulemuseaken())
vastus.grid(row=6, column=2)
vastus.grid_forget()

aken.mainloop()