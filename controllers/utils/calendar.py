from tkcalendar import Calendar, DateEntry
import tkinter as tk

def create_calendar(root):
    cal = Calendar(root, selectmode='day', year=2024, month=5, day=22)
    cal.pack(pady=20)

    def grad_date():
        date.config(text="Selected Date is: " + cal.get_date())

    date = tk.Label(root, text="")
    date.pack(pady=20)

    tk.Button(root, text="Get Date", command=grad_date).pack(pady=20)
