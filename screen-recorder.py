from tkinter import *
from PIL import Image, ImageTk
from tkinter.messagebox import showinfo
import pyscreenrec
app = Tk()

#variables
video_name = StringVar(value='untitled')
rec = pyscreenrec.ScreenRecorder()
#methods
def start_recording():
    file_name = video_name.get()
    rec.start_recording(f"{file_name}.mp4", 30)

def pause_recording():
    rec.pause_recording()
    showinfo('Recording', "Recording is Paused")

def resume_recording():
    rec.resume_recording()
    showinfo('Recording', "Resume Recording")

def stop_recording():
    rec.stop_recording()
    showinfo('Recording', "Recording is Stop")

app.title("Screen Recorder")
app.geometry("300x500")
app.resizable(0,0)
app.config(bg='#f4f4f4')

Label(app, text='Screen Recorder', font=('Arial Rounded MT Bold', 22), fg="#111").pack(pady=10)

screen_record_img = PhotoImage(file='./screen_recorder.png')
Label(app, image=screen_record_img).pack(pady=10)

ent_video_name = Entry(app, font=('Arial Rounded MT Bold', 16), highlightthickness=2, highlightbackground='crimson', textvariable=video_name)
ent_video_name.pack(fill='x', padx=20, pady=10)

frame = Frame(app)
frame.pack(pady=10)

frame.grid_columnconfigure((0,1,2, 3), weight=1, uniform='column')
frame.grid_columnconfigure(0, weight=1, uniform='row')

Button(frame, text='Start', relief="raised",font=('Arial Rounded MT Bold', 14), cursor='hand2', command=start_recording).grid(column=0, row=0, pady=10,padx=10, sticky='wens')

start_record_img = ImageTk.PhotoImage(Image.open('./start_record.png').resize((50,50)))
Button(frame, image=start_record_img, relief="flat", cursor='hand2', command=pause_recording).grid(column=1, row=0, pady=10,padx=10, sticky='wens')

pause_record_img = ImageTk.PhotoImage(Image.open('./pause_record.png').resize((50,50)))
Button(frame, image=pause_record_img, relief="flat", cursor='hand2', command=resume_recording).grid(column=2, row=0, pady=10,padx=10, sticky='wens')

stop_record_img = ImageTk.PhotoImage(Image.open('./stop_record.png').resize((50,50)))
Button(frame, image=stop_record_img, relief="flat", cursor='hand2', command=stop_recording).grid(column=3, row=0, pady=10,padx=10, sticky='wens')

app.mainloop()