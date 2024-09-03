import tkinter as tk
from views.main_view import MainView

# MainView luokka on vastuussa käyttöliittymän alustamisesta ja hallitsemisesta.
if __name__ == "__main__":
    root = tk.Tk() # Luodaan pääikkuna
    app = MainView(root) # Luodaan MainView luokan instanssi, jotta GUI saadaan näkyviin
    root.mainloop() # Käynnistetään pääikkuna
