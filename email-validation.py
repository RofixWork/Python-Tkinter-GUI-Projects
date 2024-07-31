from tkinter import *
from re import search
from tkinter.messagebox import showerror, showinfo
app = Tk()

#variables
email = StringVar()

#mehods
def verify_email(event):
    check_email = search("^[a-z]+[-|_|.]?[a-z0-9]+@[a-z]+.\w{2,3}$", email.get())
    
    if check_email:
        showinfo('Success', 'Email is valid.')
    else:
        showerror('Error', 'Email is not valid.')

#qpp configuration
app.title("Email Verification")
app.resizable(False, False)
app.config(bg = '#f4f4f4')
main_font = "Arial Rounded MT Bold"
main_font_size = 14

lbl = Label(app, text='Enter Your Email:', font=(main_font, main_font_size))
entry = Entry(app, font=(main_font, main_font_size), textvariable=email)
btn_verify = Button(app, text='Verifiy', font=(main_font, main_font_size), bg='crimson', fg='white', cursor='hand2')
lbl.grid(column=0, row=0, padx=5, pady=10)
entry.grid(column=1, row=0, columnspan=2, sticky='we', padx=5, pady=6)
btn_verify.grid(column=0, row=1, columnspan=3, ipadx=10, ipady=5, pady=5)
# grid
app.grid_columnconfigure((0,1,2), weight=1, uniform='column')
app.grid_rowconfigure((0,1), weight=1, uniform='row')

#events
btn_verify.bind("<Button>", verify_email)

app.mainloop()