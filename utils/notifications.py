import tkinter as tk
from tkinter import messagebox

def show_notification(title, message):
    root = tk.Tk()
    root.withdraw()
    messagebox.showinfo(title, message)
    root.destroy()
