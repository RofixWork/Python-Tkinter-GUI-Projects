from tkinter import * 
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfilename
app = Tk()

def open_image():
    file_path = askopenfilename(filetypes=(
        ("PNG File", '*.png'),
        ("JPEG File", '*.jpg'),
        ("All Files", '*.*')
    ), title='Select Image File')

    if file_path:
        image = Image.open(file_path)
        image_resize = image.resize((500, 500))
        img = ImageTk.PhotoImage(image_resize)
        lbl_image.config(image=img)
        lbl_image.image = img

app.title("Image Viewer")
app.geometry("600x600") 
app.minsize(600, 600)

frame = Frame(app, bg='#f4f4f4')

frame.pack(side='top', padx=5, pady=5, fill='both', expand=True)

lbl_image = Label(frame)
lbl_image.pack(expand=True, fill='both')

Button(frame, text='Open Image', font=("Arial Rounded MT Bold", 12), cursor='hand2', command=open_image).pack(side='left', pady=5)
Button(frame, text='Exit', font=("Arial Rounded MT Bold", 12), cursor='hand2', command=lambda: exit()).pack(side='right', pady=5)

app.mainloop()