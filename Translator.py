from tkinter import *
from tkinter import ttk, messagebox
import googletrans
import textblob
# import pyttsx3

root = Tk()
root.title("Google Translator")
root.geometry("1080x400")
root.resizable(False, False)
image_icon = PhotoImage(file="img/icon.png")
root.iconphoto(False, image_icon)
root.config(bg="white") 

def label_change():
    c1 = combo1.get()
    c2 = combo2.get()
    label1.configure(text=c1)
    label2.configure(text=c2)
    root.after(1000, label_change)

def translate_now():
    global language
    try:
        text_ = text1.get(1.0, END)
        c3 = combo1.get()
        c4 = combo2.get()
        if (text_):
            words = textblob.TextBlob(text_)
            lan = words.detect_language()
            for i, x in language.items():
                if (x == c4):
                    lan_= i
            words = words.translate(from_lang=lan, to=str(lan_))
            text2.delete(1.0, END)
            text2.insert(END, words)
    except Exception as e:
        messagebox.showerror("Google trans","Please try again")

def speech():
    engine = pyttsx3.init()   
    engine.say(words)
    engine.runAndWait()

arrow_image = PhotoImage(file="img/trans.png").subsample(5)
image_label = Label(root, image=arrow_image)
image_label.place(x=480, y=50)


language = googletrans.LANGUAGES
languageV = list(language.values())
lang1 = language.keys()

combo1 = ttk.Combobox(root, values=languageV, font="Roboto 14", state="r")
combo1.place(x=100, y=20)
combo1.set("ENGLISH")

label1 = Label(root, text="ENGLISH", font="segoe 30 bold", bg="white", width=18, bd=5, relief=GROOVE)
label1.place(x=10, y=50)

f1 = Frame(root, bg="black", bd=5)
f1.place(x=10, y=118, width=430, height=210)

text1 = Text(f1, font="Roboto 20", bg="white", relief=GROOVE, wrap=WORD)
text1.place(x=0, y=0, width=430, height=200)

scrollbar1 = Scrollbar(f1)
scrollbar1.pack(side="right", fill="y")
scrollbar1.configure(command=text1.yview)
text1.configure(yscrollcommand=scrollbar1.set)

combo2 = ttk.Combobox(root, values=languageV, font="Roboto 14", state="r")
combo2.place(x=730, y=20)
combo2.set("SELECT LANGUAGE")

label2 = Label(root, text="ENGLISH", font="segoe 30 bold", bg="white", width=18, bd=5, relief=GROOVE)
label2.place(x=620, y=50)

f2 = Frame(root, bg="black", bd=5)
f2.place(x=620, y=118, width=430, height=210)

text2 = Text(f2, font="Roboto 20", bg="white", relief=GROOVE, wrap=WORD)
text2.place(x=0, y=0, width=430, height=200)


scrollbar2 = Scrollbar(f2)
scrollbar2.pack(side="right", fill="y")
scrollbar2.configure(command=text2.yview)
text2.configure(yscrollcommand=scrollbar2.set)

translate = Button(root, text="Tanslate", font="Roboto 15 bold italic", activebackground="purple", cursor="hand2", bg="red", fg="white", command=translate_now)
translate.place(x=480, y=250)

speaker_img = PhotoImage(file="img/volume.png").subsample(15)
speaker = Button(f2, image=speaker_img, bg="white", command=speech)
speaker.pack(side=BOTTOM )


label_change()

root.mainloop()
