from tkinter import *
from tkinter import ttk
import speedtest_cli as speedtest
from time import *
app = Tk()

#vars
download_value = StringVar(value="0.0 Mbps")
upload_value = StringVar(value="0.0 Mbps")

#methods
def check_speed():
    btn_check.config(text='Processing...', state='disabled', command='', bg='#333', fg='white')
    app.update_idletasks()
    sleep(1)
    sp = speedtest.Speedtest()
    sp.get_servers()

    download = round(sp.download() / (10**6), 2)
    upload = round(sp.upload() / (10**6), 2)

    download_value.set(f"{download} Mbps")
    upload_value.set(f"{upload} Mbps")
    btn_check.config(text='Check Speed', state='normal', command=check_speed, bg='crimson', fg='white')


app.title('Speed Test')
app.geometry('300x400')
app.resizable(0,0)
app.config(bg = "#111")
main_font = "Arial Rounded MT Bold"
#----------------------------------
Label(app, text="Speed Test", fg='white',bg='#111', font=(main_font, 30), underline=4).pack(fill='x', pady=10)
#----------------------------------
Label(app, text="Download", fg='white',bg='#111', font=(main_font, 25)).pack(fill='x', pady=10)
Label(app, textvariable=download_value, fg='white',bg='#111', font=(main_font, 25)).pack(fill='x', pady=10)
ttk.Separator(app).pack(fill='x', padx=20)
#----------------------------------
Label(app, text="Upload", fg='white',bg='#111', font=(main_font, 25)).pack(fill='x', pady=10)
Label(app, textvariable=upload_value, fg='white',bg='#111', font=(main_font, 25)).pack(fill='x', pady=10)
ttk.Separator(app).pack(fill='x', padx=20)
#----------------------------------
btn_check = Button(app, text='Check Speed', fg='white', bg='crimson', font=(main_font, 20), cursor='hand2', command=check_speed)
btn_check.pack(fill='x', pady=10, padx=20)

app.mainloop()