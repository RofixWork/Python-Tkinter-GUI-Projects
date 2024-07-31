from tkinter import *
import phonenumbers
from phonenumbers import carrier,timezone,geocoder
from tkinter.messagebox import showinfo,showerror
class Application(Tk):
    def __init__(self):
        super().__init__()
        self.title("Phone Number Details")
        self.geometry("300x200")
        self.config(bg="#f7f7f7")
        self.resizable(False, False)
        self.main_font = 'Arial Rounded MT Bold'

        self.phone_number = StringVar()

        self.create_widgets() 

        self.mainloop()

    def create_widgets(self):
        lbl_phone_number = Label(self, text='Enter Your NO. with +__:', font=(self.main_font, 16), fg='white', bg='crimson', padx=10)

        ent_phone_number = Entry(self, font=(self.main_font, 16), highlightthickness=2, highlightbackground='crimson', relief='flat', textvariable=self.phone_number)
        btn_phone_number_details = Button(self, text="Get Details", font=(self.main_font, 16), bg='crimson', fg='white', cursor='hand2',command=self.get_details)

        lbl_phone_number.pack(pady=10)
        ent_phone_number.pack(pady=10, fill='x', padx=20)
        btn_phone_number_details.pack(pady=10)

    def get_details(self):
        try:
            phone = phonenumbers.parse(self.phone_number.get())
            time = timezone.time_zones_for_number(phone)
            carier = carrier.name_for_number(phone, 'en')
            geocode = geocoder.description_for_number(phone, 'en')

            phone_number_details = f"Phone Info: {phone}\nTime: {time}\nCarrier: {carier if carier else "Unknown"}\nLocaion: {geocode if geocode else "Unknown"}"

            showinfo("Phone Number Details", phone_number_details)
        except Exception as ex:
            showerror("Error", ex)

Application()