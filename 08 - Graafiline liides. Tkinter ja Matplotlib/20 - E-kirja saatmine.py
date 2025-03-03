from ctypes import alignment
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from email.message import EmailMessage
import smtplib, ssl
import imghdr

sender_email="annaoleks88@gmail.com"

def vali_pilt():
    global file
    file=filedialog.askopenfilename()
    lisaentry.configure(text=file, font="Calibri 8")
    return file

def email_kontroll():
    salvestakiri()
    emails=mailentry.get().split(",")
    for email in emails:
        email=email.strip()
        if "@" not in email or "." not in email:
            messagebox.showerror("Vale e-mail!", "Sul on viga e-mailis. Kontrolli")
            mailentry.configure(bg="slategray")
            return False
        else:
            mailentry.configure(bg="lightgray")
            return True

def kirieelvaade():
    global file
    salvestakiri()
    eel_aken=Toplevel()
    eel_aken.geometry("300x500")
    eel_aken.title("Kirja eelvaade!")

    saatja=Label(eel_aken, text="Saatja: " + sender_email, font="Calibri 12", fg="black",)
    saatja.grid(row=1, column=1, sticky="w")

    saaja=Label(eel_aken, text="Saaja: " + mailentry.get(), font="Calibri 12", fg="black")
    saaja.grid(row=2, column=1, sticky="w")

    teema=Label(eel_aken,text="Teema: " + teemaentry.get(), font="Calibri 12", fg="black")
    teema.grid(row=3, column=1, sticky="w")

    vah=Label(eel_aken, height=2)
    vah.grid(row=4, column=1, sticky="w")

    kiri=Label(eel_aken, text="Kiri:", font="Calibri 12", fg="black")
    kiri.grid(row=5, column=1, sticky="w")

    teks=Label(eel_aken, text=kirientry.get("1.0", END), font="Calibri 12", fg="black", wraplength=250, anchor="w", justify=LEFT)
    teks.grid(row=6, column=1, sticky="w")

    manus=Label(eel_aken, text="lisatud failid: ", font="Calibri 12", fg="black")
    manus.grid(row=7, column=1, sticky="w")

    lisafail=Label(eel_aken, text=file, font="Calibri 12", fg="black")
    lisafail.grid(row=8, column=1, sticky="w")
    
def salvestakiri():
    global mailentry, teemaentry, kirientry, file
    if 'file' not in globals():
        file = ""
    fail = "08 - Graafiline liides. Tkinter ja Matplotlib/drafts.txt"
    draft={"email":mailentry.get(),
           "teema":teemaentry.get(),
           "kiri":kirientry.get("1.0", END),
           "lisa":file}
    with open(fail,'w', encoding="utf-8-sig") as f:
        for key, value in draft.items():
            f.write(f"{key}: {value}\n")
    return fail

def saada_kiri():
    global file
    salvestakiri()
    if email_kontroll()==False:
        return
    kellele=[email.strip() for email in mailentry.get().split(",")]
    kiri=kirientry.get("1.0", END)
    smtp_server="smtp.gmail.com"
    port=587
    password="xsiw uicd bpgw djpf"
    context=ssl.create_default_context()
    msg=EmailMessage()
    msg.set_content(kiri)
    msg['Subject']=teemaentry.get()
    msg['From']="Ana Oleks"
    msg['To']=",".join(kellele)
    if not file:
        messagebox.showerror("Tekkis viga!", "Faili pole valitud!")
    else:
        with open(file,'rb') as fpilt:
            pilt=fpilt.read()
        msg.add_attachment(pilt,maintype='image',subtype=imghdr.what(None,pilt))
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

def close():
    salvestakiri()
    aken.destroy()

aken=Tk()
aken.geometry("550x550")
aken.title("E-kirja saatmine")

mail=Label(aken,text="EMAIL:", font="Calibri 20", fg="white", bg="slategray", width=10)
mail.grid(row=1, column=1)

p1=Label(aken, text=" ", width=2)
p1.grid(row=1, column=2, rowspan=6)

mailentry=Entry(aken,font="Calibri 15", fg="black", bg="lightgray", width=35)
mailentry.grid(row=1, column=3, columnspan=2)

teema=Label(aken,text="TEEMA:", font="Calibri 20", fg="white", bg="slategray",width=10)
teema.grid(row=2, column=1)

teemaentry=Entry(aken,font="Calibri 15", fg="black", bg="lightgray", width=35)
teemaentry.grid(row=2, column=3, columnspan=2)

lisa=Label(aken,text="LISA:", font="Calibri 20", fg="white", bg="slategray", width=10)
lisa.grid(row=3, column=1)

lisaentry=Label(aken,text="...", font="Calibri 15", fg="black")
lisaentry.grid(row=3, column=3, columnspan=2)

kiri=Label(aken, text="KIRI", font="calibri 20", fg="white", bg="slategray", width=10)
kiri.grid(row=4, column=1)

kirientry=Text(aken, font="calibri 15", fg="black", bg="lightgray", width=35, height=5)
kirientry.grid(row=4, column=3, columnspan=2)

p2=Label(aken, text=" ", width=2)
p2.grid(row=5, column=1)

lisapilt=Button(aken, text="LISA FAIL", font="Calibri 20", fg="white", bg="slategray", command=lambda:vali_pilt())
lisapilt.grid(row=6, column=3)

saada=Button(aken, text="SAADA", font="Calibri 20", fg="white", bg="slategray", command=lambda:saada_kiri())
saada.grid(row=6, column=4)

p=Label(aken, text=" ", height=2)
p.grid(row=7, column=1)

eelvaade=Button(aken, text="EELVAADE", font="Calibri 15", fg="white", bg="slategray", command=lambda:kirieelvaade())
eelvaade.grid(row=8, column=1)

aken.protocol("WM_DELETE_WINDOW", close) #chat GPT

aken.mainloop()
