from tkinter import *
import qrcode as qr
import string, random
from tkinter.messagebox import showerror
from PIL import ImageTk
from tkinter.filedialog import asksaveasfilename
app = Tk()
app.title("Qr Code")
app.resizable(False, False)
main_font = "Arial Rounded MT Bold"
main_font_size = 16

#variables
url_value = StringVar()
img = ""
#methods
def generate_qr_code(event):
    global img

    if not url_value.get():
        showerror('Error', "please fill data...")
        return
    
    img = qr.make(url_value.get(), box_size=10)
    img = img.convert('RGB')

    qr_code_img = ImageTk.PhotoImage(img)

    lbl_image.config(image=qr_code_img)
    lbl_image.image = qr_code_img
    btn_save.config(state='normal', command=save_qr_code)

def save_qr_code():
    if img:
        #handle file
        file_types = (
            ('PNG Files', "*.png"),
            ("All Files", "*.*")
        )
        file_path = asksaveasfilename(defaultextension="*.png", filetypes=file_types)

        if file_path:
            img.save(file_path)
            lbl_image.config(image='')
            lbl_image.image = ''
            btn_save.config(state='disabled', command='')
            url_value.set("")
            entry.focus()
        

#widgets
lbl = Label(app, text="QR Code Generator", font=(main_font, 20, "bold"), anchor='w')
lbl2 = Label(app, text='Paste a url or enter a text to create Qr Code', fg="#333", font=(main_font, 11), anchor='w')
entry = Entry(app, font=(main_font, main_font_size), relief='solid', textvariable=url_value)
btn_generate = Button(app, text='Generate QR Code', font=(main_font, main_font_size),  bg='#672eee', fg='white', cursor='hand2')
btn_save = Button(app, text='Save QR Code', font=(main_font, main_font_size), cursor='hand2', state='disabled')
lbl_image = Label(app)

lbl.pack(pady=4, padx=5, fill='x')
lbl2.pack(pady=2, padx=5, fill='x')
entry.pack(pady=4, padx=5, fill='x')
btn_generate.pack(pady=4, padx=5, fill='x')
btn_save.pack(pady=4, padx=5, fill='x')
lbl_image.pack(pady=1, padx=5, fill='x')


#events
btn_generate.bind("<Button>", generate_qr_code)

app.mainloop()