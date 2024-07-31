from tkinter import *
from tkinter.scrolledtext import ScrolledText
import pyttsx3
app = Tk()

def speak():
    text = text_value.get("1.0", END)

    if text:
        engine = pyttsx3.init()
        engine.say(text)
        engine.runAndWait()

app.title("Text to Speech")
app.geometry("400x600+100+100")
app.resizable(0,0)

Label(app, text='Text to Speech', font=("Arial Rounded MT Bold", 20), bg='crimson', fg='white', pady=5, padx=10).grid(column=0, row=0, pady=5)

text_value = ScrolledText(app, font=("Arial Rounded MT Bold", 16), bd=2, relief=GROOVE)
text_value.grid(column=0, row=1, sticky="nswe", padx=5, pady=5)

Button(app, text='Speak', font=("Arial Rounded MT Bold", 16), bg='crimson', fg='white', bd=2, cursor='hand2', command=speak).grid(column=0, row=2)

app.grid_columnconfigure(0, weight=1, uniform='column')
app.grid_rowconfigure(0, weight=1, uniform='row')
app.grid_rowconfigure(1, weight=8, uniform='row')
app.grid_rowconfigure(2, weight=1, uniform='row')


app.mainloop()