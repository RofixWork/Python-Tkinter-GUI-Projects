from tkinter import *
from tkinter import filedialog
from stegano import lsb
from PIL import Image, ImageTk
from tkinter.scrolledtext import ScrolledText
from tkinter import messagebox
import os

main_bg = "#f4f4f4"
main_font = "Arial Rounded MT Bold"
root = Tk()

#methods
def open_image():
    global filename
    filename = filedialog.askopenfilename(
        title='Select Image File',
        initialdir=os.getcwd(),
        filetypes=(
            ('PNG File', "*.png"),
            ('JPG File', "*.jpg"),
            ('All Files', "*.*"),
    ))
    if filename:
        image = Image.open(filename)
        image_resize = image.resize((250, 250))
        img = ImageTk.PhotoImage(image_resize)
        lbl_image.config(image=img)
        lbl_image.image = img

def hide_data():
    global secret
    try:
        secret_message = secret_text.get("1.0", END)
        secret = lsb.hide(filename, secret_message)
        messagebox.showinfo("Success", "Secret message hidden successfully!")
    except Exception as ex:
        messagebox.showerror('Error', ex)

def save_image():
    file_path = filedialog.asksaveasfilename(filetypes=(
            ('PNG File', "*.png"),
            ('JPG File', "*.jpg"),
            ('All Files', "*.*"),
    ), defaultextension='*.png', initialdir=os.getcwd(), title='Save Image File')

    if file_path and secret:
        secret.save(file_path)
        messagebox.showinfo("Success", "Secret message saved successfully!")
        lbl_image.config(image='')
        lbl_image.image = ''
        secret_text.delete("1.0", END)


def show_data():
    secret_text.delete("1.0", "end")
    clear_message = lsb.reveal(filename)
    secret_text.insert("1.0", clear_message)

#-------config
root.title("Steganography - Hide a Secret Text Message in an Image")
root.geometry("700x500+150+180")
root.resizable(False, False)
root.config(bg=main_bg)
root.iconbitmap("./stegano.ico")
#labels
image = PhotoImage(file='lock.png')
Label(root, text='CYBER SCIENCE', font=(main_font, 20), anchor='w', bg=main_bg, image=image, compound='left').grid(padx=10,column=0, row=0, sticky='we')

#frame one
frame_1 = Frame(root)

lbl_image = Label(frame_1, bg='black')
lbl_image.grid(column=0, row=0, sticky="nswe")

secret_text = ScrolledText(frame_1, font=(main_font, 16))
secret_text.grid(column=1, row=0, sticky="nswe")

#frame 1 grid layout
frame_1.grid_columnconfigure((0,1), weight=1, uniform='column')
frame_1.grid_rowconfigure(0, weight=1, uniform='row')

frame_1.grid(column=0, row=1, sticky="nswe", padx=10)
#frame one

#frame two
frame_2 = Frame(root)

sub_frame_1 = Frame(frame_2, highlightthickness=2, highlightbackground='#415a77')
sub_frame_2 = Frame(frame_2, highlightthickness=2, highlightbackground='#415a77')

#sub frame 1 widgets
Label(sub_frame_1, text='Picure, Image, Photo File', font=(main_font, 12), anchor='w', fg='#415a77').grid(column=0, row=0, columnspan=2, sticky='we', padx=10)
Button(sub_frame_1, text='Open Image', font=(main_font, 10), cursor='hand2', command=open_image).grid(column=0, row=1, sticky='nswe', padx=10, pady=5)
Button(sub_frame_1, text='Save Image', font=(main_font, 10), cursor='hand2', command=save_image).grid(column=1, row=1, sticky='nswe', padx=10, pady=5)

sub_frame_1.grid_columnconfigure((0,1), weight=1,uniform='column')
sub_frame_1.grid_rowconfigure((0,1), weight=1,uniform='row')
#sub frame 1 widgets

#sub frame 2 widgets
Label(sub_frame_2, text='Steganography', fg='#415a77', font=(main_font, 12), anchor='w').grid(column=0, row=0, columnspan=2, sticky='we', padx=10)
Button(sub_frame_2, text='Hide Data', font=(main_font, 10), cursor='hand2', command=hide_data).grid(column=0, row=1, sticky='nswe', padx=10, pady=5)
Button(sub_frame_2, text='Show Data', font=(main_font, 10), cursor='hand2', command=show_data).grid(column=1, row=1, sticky='nswe', padx=10, pady=5)

sub_frame_2.grid_columnconfigure((0,1), weight=1,uniform='column')
sub_frame_2.grid_rowconfigure((0,1), weight=1,uniform='row')
#sub frame 2 widgets

frame_2.grid(column=0, row=2, sticky='nswe', pady=5, padx=10)
sub_frame_1.grid(column=0, row=0, sticky='nswe')
sub_frame_2.grid(column=1, row=0, sticky='nswe', padx=5)

frame_2.grid_columnconfigure((0,1), weight=1,uniform='column')
frame_2.grid_rowconfigure(0, weight=1,uniform='row')

#grid layout
root.columnconfigure(0, weight=1, uniform='column')
root.grid_rowconfigure(0, weight=1, uniform='row')
root.grid_rowconfigure(1, weight=3, uniform='row')
root.grid_rowconfigure(2, weight=1, uniform='row')


root.mainloop()