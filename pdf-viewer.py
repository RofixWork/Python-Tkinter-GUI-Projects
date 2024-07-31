from tkinter import *
import os
from tkPDFViewer import tkPDFViewer as pdf
from tkinter.filedialog import askopenfilename
root = Tk()
def open_pdf_file():
    filename = askopenfilename(title='Select PDF File', initialdir=os.getcwd(), filetypes=(
        ("PDF File", "*.pdf"),
        ("PDF File", "*.PDF"),
        ("All Files", "*.*"),
    ))
    print(filename)
    if filename:

        variable1 = pdf.ShowPdf()
        current_file = variable1.pdf_view(root, pdf_location=open(filename, 'r'))

        current_file.pack(fill='both', expand=True)

root.title("PDF Viewer")
root.geometry("400x600+300+100")
root.config(bg='#f4f4f4')
main_font = 'Arial Rounded MT Bold'
Button(root, text='Open File PDF', font=(main_font, 16), cursor='hand2', command=open_pdf_file).pack(fill='x',pady=10, padx=10)

root.mainloop()