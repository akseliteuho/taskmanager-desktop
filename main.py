import tkinter as tk
from views.MainView import MainView

# Käynnistetään sovellus
if __name__ == "__main__":
    root = tk.Tk() # Luodaan pääikkuna käyttöliittymälle
    app = MainView(root) # Luodaan MainView luokan instanssi, jotta GUI saadaan näkyviin
    root.mainloop() # Käynnistetään pääikkuna
