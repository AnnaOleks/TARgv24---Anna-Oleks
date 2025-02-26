from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from email.message import EmailMessage
import smtplib, ssl
import imghdr

def vali_pilt():
    global file
    file=filedialog.askopenfilename()
    lisaentry.configure(text=file, font="Calibri 8")
    return file

def saada_kiri():
    kellele=mailentry.get()
    kiri=kirientry.get("1.0", END)
    smtp_server="smtp.gmail.com"
    port=587
    sender_email="annaoleks88@gmail.com"
    password="xsiw uicd bpgw djpf"
    context=ssl.create_default_context()
    msg=EmailMessage()
    msg.set_content(kiri)
    msg['Subject']=teemaentry.get()
    msg['From']="Ana Oleks"
    msg['To']=kellele
    if not file:
        messagebox.showerror("Tekkis viga!", "Faili pole valitud!")
    return
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

aken=Tk()
aken.geometry("550x550")
aken.title("E-kirja saatmine")

mail=Label(aken,text="EMAIL:", font="Calibri 24", fg="white", bg="slategray", width=10)
mail.grid(row=1, column=1)

mailentry=Entry(aken,font="Calibri 24", fg="black", bg="lightgray")
mailentry.grid(row=1, column=2, columnspan=2)

teema=Label(aken,text="TEEMA:", font="Calibri 24", fg="white", bg="slategray",width=10)
teema.grid(row=2, column=1)

teemaentry=Entry(aken,font="Calibri 24", fg="black", bg="lightgray")
teemaentry.grid(row=2, column=2, columnspan=2)

lisa=Label(aken,text="LISA:", font="Calibri 24", fg="white", bg="slategray", width=10)
lisa.grid(row=3, column=1)

lisaentry=Label(aken,text="...", font="Calibri 24", fg="black")
lisaentry.grid(row=3, column=2, columnspan=2)

kiri=Label(aken, text="KIRI", font="calibri 24", fg="white", bg="slategray", width=10)
kiri.grid(row=4, column=1)

kirientry=Text(aken, font="calibri 24", fg="black", bg="lightgray", width=20, height=5)
kirientry.grid(row=4, column=2, columnspan=2)

lisapilt=Button(aken, text="LISA FAIL", font="Calibri 24", fg="white", bg="slategray", command=lambda:vali_pilt())
lisapilt.grid(row=5, column=2)

saada=Button(aken, text="SAADA", font="Calibri 24", fg="white", bg="slategray", command=lambda:saada_kiri())
saada.grid(row=5, column=3)

aken.mainloop()
