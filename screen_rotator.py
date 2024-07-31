from tkinter import *
import rotatescreen
from tkinter.messagebox import showerror
app = Tk()

def screen_rotate(side : str):
    screen = rotatescreen.get_primary_display()
    match side:
        case 'up':
            screen.set_landscape()
            
        case 'right':
            screen.set_portrait_flipped()
            
        case 'left':
            screen.set_portrait()
            
        case 'bottom':
            screen.set_landscape_flipped()
            
        case _:
            showerror("Error", "Invalid side specified")

app.title("Screen Rotator")
app.geometry("250x250")
app.config(bg='#f45632')
app.resizable(False, False)
main_font="Arial Rounded MT Bold"
main_font_size = 13

Button(app, text="UP", font=(main_font, main_font_size), cursor="hand2", anchor='center', padx=10, command=lambda: screen_rotate('up')).place(relx=0.5, rely=0, y=30, anchor='center')
Button(app, text="Right", font=(main_font, main_font_size), cursor="hand2", anchor='center', padx=10, command=lambda: screen_rotate('right')).place(rely=0.5,relx=1, anchor='e', x=-10)
Button(app, text="Left", font=(main_font, main_font_size), cursor="hand2", anchor='center', padx=10, command=lambda: screen_rotate('left')).place(rely=0.5,relx=0, anchor='w', x=10)
Button(app, text="Bottom", font=(main_font, main_font_size), cursor="hand2", anchor='center', padx=10, command=lambda: screen_rotate('bottom')).place(rely=1,relx=0.5, anchor='s', y=-10)

app.mainloop()