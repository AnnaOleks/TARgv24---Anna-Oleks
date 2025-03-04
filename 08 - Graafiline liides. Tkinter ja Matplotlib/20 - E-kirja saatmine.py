from ctypes import alignment
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from email.message import EmailMessage
import smtplib, ssl
import imghdr
from PIL import Image, ImageTk

sender_email="annaoleks88@gmail.com"

def vali_pilt():
    global file
    file=filedialog.askopenfilename()
    lisaentry.configure(text=file, font="Calibri 8", justify=LEFT)
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
    eel_aken.iconbitmap(default="08 - Graafiline liides. Tkinter ja Matplotlib/letter_opened.ico")
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

def heleteema():
    global sendicon
    global saveicon
    global lisaicon
    global vaataicon

    aken.configure(bg="#f5f5f5")

    send_icon=Image.open(r"08 - Graafiline liides. Tkinter ja Matplotlib/send.png")
    send_icon_resize=send_icon.resize((20,20))
    sendicon=ImageTk.PhotoImage(send_icon_resize)

    saada.configure(image=sendicon, fg="black", bg="Gainsboro")

    lahter2.configure(bg="#f5f5f5")

    save_icon=Image.open(r"08 - Graafiline liides. Tkinter ja Matplotlib/save_icon.png")
    save_icon_resize=save_icon.resize((20,20))
    saveicon=ImageTk.PhotoImage(send_icon_resize)

    salvesta.configure(image=saveicon, fg="black", bg="Gainsboro")

    lahter4.configure(bg="#f5f5f5")

    lisa_icon=Image.open(r"08 - Graafiline liides. Tkinter ja Matplotlib/PaperClip.png")
    lisa_icon_resize=lisa_icon.resize((20,20))
    lisaicon=ImageTk.PhotoImage(lisa_icon_resize)

    lisapilt.configure(image=lisaicon, fg="black", bg="Gainsboro")

    lahter6.configure(bg="#f5f5f5")

    vaata_icon=Image.open(r"08 - Graafiline liides. Tkinter ja Matplotlib/iconfinder.png")
    vaata_icon_resize=vaata_icon.resize((20,20))
    vaataicon=ImageTk.PhotoImage(vaata_icon_resize)

    eelvaade.configure(image=vaataicon, fg="black", bg="Gainsboro")
    
    vahe1.configure(bg="#f5f5f5")
    mail.configure(fg="black", bg="lightgray")
    mailentry.configure(fg="black", bg="lightgray")
    teema.configure(fg="black", bg="lightgray")
    teemaentry.configure(fg="black", bg="lightgray")
    lisa.configure(fg="black", bg="lightgray")
    lisaentry.configure(bg="#f5f5f5", fg="black")
    kiri.configure(fg="black", bg="lightgray")
    kirientry.configure(fg="black", bg="lightgray")
    reziim.configure(bg="#f5f5f5", fg="black")
    hele.configure(fg="black", bg="lightgray")
    tume.configure(fg="black", bg="lightgray")

def tumeteema():
    global tumesendicon
    global tumesaveicon
    global tumelisaicon
    global tumevaataicon

    aken.configure(bg="black")

    tume_send_icon=Image.open(r"08 - Graafiline liides. Tkinter ja Matplotlib/envelope_mail_letter_send.png")
    tume_send_icon_resize=tume_send_icon.resize((30,20))
    tumesendicon=ImageTk.PhotoImage(tume_send_icon_resize)

    saada.configure(image=tumesendicon, bg="#242426", fg="white")

    lahter2.configure(bg="black")

    tume_save_icon=Image.open(r"08 - Graafiline liides. Tkinter ja Matplotlib/Floppy-disc.png")
    tume_save_icon_resize=tume_save_icon.resize((20,20))
    tumesaveicon=ImageTk.PhotoImage(tume_save_icon_resize)

    salvesta.configure(image=tumesaveicon, bg="#242426", fg="white")

    lahter4.configure(bg="black")

    tume_lisa_icon=Image.open(r"08 - Graafiline liides. Tkinter ja Matplotlib/Paper-clip.png")
    tume_lisa_icon_resize=tume_lisa_icon.resize((20,20))
    tumelisaicon=ImageTk.PhotoImage(tume_lisa_icon_resize)

    lisapilt.configure(image=tumelisaicon, bg="#242426", fg="white")

    lahter6.configure(bg="black")

    tume_vaata_icon=Image.open(r"08 - Graafiline liides. Tkinter ja Matplotlib/document.png")
    tume_vaata_icon_resize=tume_vaata_icon.resize((20,20))
    tumevaataicon=ImageTk.PhotoImage(tume_vaata_icon_resize)

    eelvaade.configure(image=tumevaataicon, bg="#242426", fg="white")
    
    vahe1.configure(bg="black")
    mail.configure(bg="#242426", fg="white")
    mailentry.configure(bg="#242426", fg="white")
    teema.configure(bg="#242426", fg="white")
    teemaentry.configure(bg="#242426", fg="white")
    lisa.configure(bg="#242426", fg="white")
    lisaentry.configure(bg="black", fg="white")
    kiri.configure(bg="#242426", fg="white")
    kirientry.configure(bg="#242426", fg="white")
    reziim.configure(bg="black", fg="white")
    hele.configure(bg="#242426", fg="white")
    tume.configure(bg="#242426", fg="white")
    
def close():
    salvestakiri()
    aken.destroy()

aken=Tk()
aken.iconbitmap(default="08 - Graafiline liides. Tkinter ja Matplotlib/letter_icon.ico")
aken.geometry("470x470")
aken.title("E-kirja saatmine")

global sendicon
global saveicon
global lisaicon
global vaataicon

send_icon=Image.open(r"08 - Graafiline liides. Tkinter ja Matplotlib/send.png")
send_icon_resize=send_icon.resize((20,20))
sendicon=ImageTk.PhotoImage(send_icon_resize)

saada=Button(aken, image=sendicon, text="SAADA", compound=TOP, font="Calibri 14", fg="black", bg="Gainsboro", width=70, padx=10, pady=10, command=lambda:saada_kiri())
saada.grid(row=1, column=1)

lahter2=Label(aken, text=" ", width=1)
lahter2.grid(row=1, column=2)

save_icon=Image.open(r"08 - Graafiline liides. Tkinter ja Matplotlib/save_icon.png")
save_icon_resize=save_icon.resize((20,20))
saveicon=ImageTk.PhotoImage(send_icon_resize)

salvesta=Button(aken, image=saveicon, text="SALVESTA", compound=TOP, font="Calibri 14", fg="black", bg="Gainsboro", width=70, padx=10, pady=10, command=lambda:salvestakiri())
salvesta.grid(row=1, column=3)

lahter4=Label(aken, text=" ", width=1)
lahter4.grid(row=1, column=4)

lisa_icon=Image.open(r"08 - Graafiline liides. Tkinter ja Matplotlib/PaperClip.png")
lisa_icon_resize=lisa_icon.resize((20,20))
lisaicon=ImageTk.PhotoImage(lisa_icon_resize)

lisapilt=Button(aken, image=lisaicon, text="LISA", compound=TOP, font="Calibri 14", fg="black", bg="Gainsboro", width=70, padx=10, pady=10, command=lambda:vali_pilt())
lisapilt.grid(row=1, column=5)

lahter6=Label(aken, text=" ", width=1)
lahter6.grid(row=1, column=6)

vaata_icon=Image.open(r"08 - Graafiline liides. Tkinter ja Matplotlib/iconfinder.png")
vaata_icon_resize=vaata_icon.resize((20,20))
vaataicon=ImageTk.PhotoImage(vaata_icon_resize)

eelvaade=Button(aken, image=vaataicon, text="VAATA", compound=TOP, font="Calibri 14", fg="black", bg="Gainsboro", width=70, padx=10, pady=10, command=lambda:kirieelvaade())
eelvaade.grid(row=1, column=7)

vahe1=Label(aken, text=" ", width=2)
vahe1.grid(row=2, column=1)

mail=Label(aken,text="EMAIL:", font="Calibri 14", fg="black", bg="lightgray", width=10, anchor="w")
mail.grid(row=3, column=1)

mailentry=Entry(aken,font="Calibri 14", fg="black", bg="lightgray", width=33)
mailentry.grid(row=3, column=3, columnspan=5)

teema=Label(aken,text="TEEMA:", font="Calibri 14", fg="black", bg="lightgray", width=10, anchor="w")
teema.grid(row=4, column=1)

teemaentry=Entry(aken,font="Calibri 14", fg="black", bg="lightgray", width=33)
teemaentry.grid(row=4, column=3, columnspan=5)

lisa=Label(aken,text="LISA:", font="Calibri 14", fg="black", bg="lightgray", width=10, anchor="w")
lisa.grid(row=5, column=1)

lisaentry=Label(aken,text="...", font="Calibri 14", fg="black")
lisaentry.grid(row=5, column=3, columnspan=5)

kiri=Label(aken, text="KIRI:", font="Calibri 14", fg="black", bg="lightgray", width=10, anchor="w")
kiri.grid(row=6, column=1, sticky="nsew")

kirientry=Text(aken, font="calibri 14", fg="black", bg="lightgray", width=33, height=5)
kirientry.grid(row=6, column=3, columnspan=5)

reziim=Label(aken, text="Vali reziimi: ", font="Calibri 14")
reziim.place(x=230, y=430)

hele=Button(text="HELE", font="calibri 14", fg="black", bg="lightgray", width=5, command=lambda:heleteema())
hele.place(x=329, y=423)

tume=Button(text="TUME", font="calibri 14", fg="black", bg="lightgray", width=5, command=lambda:tumeteema())
tume.place(x=388, y=423)

aken.protocol("WM_DELETE_WINDOW", close) #chat GPT

aken.mainloop()
