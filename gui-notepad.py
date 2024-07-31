from tkinter import *
from tkinter.scrolledtext import ScrolledText
from tkinter.filedialog import askopenfile, asksaveasfile
from tkinter.messagebox import showinfo
import os
app = Tk()

def open_file():
    file = askopenfile(initialdir=os.getcwd(), title='Select File', filetypes=(
        ("Text File", "*.txt"),
        ("All Files", "*.*")
    ))

    if file:
        file_input.delete("1.0", END)
        file_content = file.read()
        file_input.insert("1.0", file_content)
        file.close()

def save_file():
    file_path = asksaveasfile(initialdir=os.getcwd(), filetypes=(
        ("Text File", "*.txt"),
        ("All Files", "*.*")
    ), defaultextension="*.txt", title='Save File')

    if file_path:
        file_path.write(file_input.get("1.0", "end"))
        file_path.close()
        showinfo("Success", "File saved successfully.")
        file_input.delete("1.0", END)

def exit():
    app.quit()


app.geometry("400x500")
app.title("Notepad 2.0")
#menus
main_menu = Menu(app, tearoff=False)
file_menu = Menu(main_menu, tearoff=False)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=exit)

main_menu.add_cascade(label='File', menu=file_menu)
#menus

file_input = ScrolledText(app,  font=("Arial Rounded MT Bold", 18))
file_input.pack(fill='both', padx=10, pady=10, expand=True)

app.config(menu=main_menu)
app.mainloop()