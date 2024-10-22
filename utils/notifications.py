import tkinter as tk
from tkinter import messagebox

# Tämä funktio näyttää ilmoituksen käyttäjälle.
def show_notification(title, message):
    root = tk.Tk()
    root.withdraw() # Piilotetaan pääikkuna käyttäjältä
    messagebox.showinfo(title, message) # Näytetään ilmoitus
    root.destroy() # tuhotaan ikkuna
