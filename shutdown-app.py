from tkinter import *
import os

class Application(Tk):
    def __init__(self):
        super().__init__()
        self.title("Shutdown App")
        self.geometry("250x250")
        self.config(bg='#f7f7f7')
        self.resizable(False, False)

        self.create_buttons()

        self.create_grid_layout()

        self.mainloop()

    def create_grid_layout(self):
        self.grid_columnconfigure((0, 1), weight=1, uniform='column')
        self.grid_rowconfigure((0, 1), weight=1, uniform='row')

    def create_buttons(self):
        btn_restart = CustomButton(self, text="Restart", background='#669bbc', command=self.restart)
        btn_restart_time = CustomButton(self, text="Restart Time", background='#003049', command=self.restart_time)
        btn_logout = CustomButton(self, text="Logout", background='#c1121f', command=self.logout)
        btn_shutdowm = CustomButton(self, text="ShutDonw", background='#780000', command=self.shutdown)

        btn_restart.grid(row=0, column=0, padx=2, pady=2, sticky='nswe')
        btn_restart_time.grid(row=0, column=1, padx=2, pady=2, sticky='nswe')
        btn_logout.grid(row=1, column=0, padx=2, pady=2, sticky='nswe')
        btn_shutdowm.grid(row=1, column=1, padx=2, pady=2, sticky='nswe')

    def restart(self):
        os.system("shutdown /r /t 1")

    def restart_time(self):
        os.system("shutdown /r /t 20")

    def logout(self):
        os.system("shutdown /l")

    def shutdown(self):
        os.system("shutdown /s /t 0")

class CustomButton(Button):
    def __init__(self, parent : Misc, text : str, background : str, command):
        super().__init__(parent, text=text, font=("Arial Rounded MT Bold", 13), bg=background, fg='white', cursor='hand2', command=command)

Application()


 