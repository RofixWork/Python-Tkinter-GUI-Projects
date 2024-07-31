from tkinter import *
from random import *
from time import *
from tkinter.scrolledtext import ScrolledText
app = Tk()


# paragraphs for test
paragraphs = ['i love you python', 'hello world', "hi javascript how are you?", "First, determine the number of words you need to write (W). Next, determine your writing speed (S) in words per minute. Use the formula from above = T = W / S. Finally, calculate the Handwriting Time (T) in minutes."]

#varaibles
paragraph_test = StringVar(value = choice(paragraphs))
lbl_speed_value = StringVar(value="Speed: 0 w/sec")
lbl_errors = StringVar(value="Error: 0")
time_start = None
time_end = None

#methods

def start_timer(event):
    global time_start
    if time_start is None:
        time_start = time()

def stop_timer(event):
    global time_end
    time_end = time()

def calc_mistakes(original_paragraph : str, test_paragraph : str) -> int:
    error = 0

    for index in range(len(original_paragraph)):
        try:
            if original_paragraph[index] != test_paragraph[index]:
                error += 1
        except:
            error += 1
    return error

def handle_error_label(errors_count : int) -> None:
    lbl_errors.set(f"Error: {errors_count}")
    if errors_count <= 0:
        lbl_mistakes.config(fg = 'green')
    else:
        lbl_mistakes.config(fg = 'red')

def calc_speed(paragraph : str) -> int:
    global time_start
    global time_end

    time_write = time_end - time_start
    time_R = round(time_write)
    time_final = len(paragraph) / time_R
    return round(time_final)

def verify_test(event):
    original_paragraph = paragraph_test.get()
    test_paragraph = ent_paragraph_value.get('1.0', 'end')

    errors = calc_mistakes(original_paragraph, test_paragraph)
    write_speed_time = calc_speed(test_paragraph)
    handle_error_label(errors)

    lbl_speed_value.set(f"Speed: {write_speed_time} w/sec")
    

app.title("Speed Calculator")
app.geometry("600x500")
app.config(bg='#f4f4f4')

app.resizable(0, 0)
main_font = "Arial Rounded MT Bold"


lbl_title = Label(app, text='Speed Calculator', font=(main_font, 20), bg='crimson', fg='white', padx=10)
lbl_paragraph_test =  Label(app, font=(main_font, 18), fg='red', textvariable=paragraph_test, wraplength=500)
ent_paragraph_value = ScrolledText(app, font=(main_font, 18), relief='solid')
btn_verify = Button(app,text='Verify', font=(main_font, 12), bg='red', fg='white', padx=5, pady=5, cursor='hand2')
lbl_speed =  Label(app, textvariable=lbl_speed_value, font=(main_font, 15))
lbl_mistakes =  Label(app, textvariable=lbl_errors, font=(main_font, 15))
#render widgets
lbl_title.grid(column=0, row=0, pady=5)
lbl_paragraph_test.grid(column=0, row=1, pady=5, padx=10)
ent_paragraph_value.grid(column=0, row=2, pady=5, padx=10, sticky='ns')
btn_verify.grid(column=0, row=3, pady=5, padx=5)
lbl_speed.grid(column=0, row=4, pady=5, padx=5)
lbl_mistakes.grid(column=0, row=5, pady=5, padx=5)

#grid layout
app.grid_columnconfigure(0, weight=1)
app.grid_rowconfigure(0, minsize=50)
app.grid_rowconfigure(1, minsize=70)
app.grid_rowconfigure(2, weight=1)
app.grid_rowconfigure((3,4,5), minsize=30)


#events
btn_verify.bind("<Button>", verify_test)
ent_paragraph_value.bind("<KeyPress>", start_timer)
ent_paragraph_value.bind("<KeyRelease>", stop_timer)

app.mainloop()
