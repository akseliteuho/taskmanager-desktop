import tkinter as tk
from tkinter import messagebox
from tkcalendar import DateEntry
from controllers.task_controller import TaskController
from controllers.folder_controller import FolderController

# MainView luokka on vastuussa käyttöliittymän alustamisesta ja hallitsemisesta.
class MainView:
    # Konstruktori saa parametrinaan root-olion, joka on pääikkuna GUI:ssa.
    def __init__(self, root):
        self.root = root # Tallennetaan root-olio luokan muuttujaan.
        self.root.title("Task Manager")

       # Luodaan TaskController ja FolderController -oliot, joiden avulla voidaan hallita tehtäviä ja kansioita.
        self.task_controller = TaskController()
        self.folder_controller = FolderController()

        # Kutsutaan create_widgets -metodia, joka luo GUI:n komponentit.
        self.create_widgets()


    # Metodi luo GUI:n komponentit.
    def create_widgets(self):

        # Luodaan painike, joka kutsuu create_task metodia ja mahdollistaa uuden tehtävän luomisen.
        self.create_task_button = tk.Button(self.root, text="Create Task", command=self.create_task)
        self.create_task_button.pack()

        # Luodaan painike, joka kutsuu create_folder metodia ja mahdollistaa uuden kansion luomisen.
        self.create_folder_button = tk.Button(self.root, text="Create Folder", command=self.create_folder)
        self.create_folder_button.pack()

        # Luodaan Listbox-komponentti, johon lisätään tehtävät.
        self.tasks_listbox = tk.Listbox(self.root)
        self.tasks_listbox.pack(fill=tk.BOTH, expand=True)

        # Luodaan painike, joka kutsuu delete_task metodia ja mahdollistaa tehtävän poistamisen.
        self.delete_task_button = tk.Button(self.root, text="Delete Task", command=self.delete_task)
        self.delete_task_button.pack()

        # Luodaan Listbox-komponentti, johon lisätään kansiot.
        self.folders_listbox = tk.Listbox(self.root)
        self.folders_listbox.pack(fill=tk.BOTH, expand=True)

        # Päivitetään tehtävät ja kansiot, jotta ne saadaan näkyviin.
        self.refresh_tasks()
        self.refresh_folders()


    # Metodi avaa uuden ikkunan, jossa käyttäjä voi luoda uuden tehtävän.
    def create_task(self):
        
        create_task_window = tk.Toplevel(self.root) # Luodaan uusi ikkuna.
        create_task_window.title("Create Task") # Asetetaan ikkunalle otsikko.

        # Luodaan tekstikenttä tehtävän nimen lisäämistä varten.
        tk.Label(create_task_window, text="Title:").pack() 
        title_entry = tk.Entry(create_task_window) 
        title_entry.pack() 

        # Luodaan tekstikenttä tehtävän kuvauksen lisäämistä varten.
        tk.Label(create_task_window, text="Description:").pack()
        description_entry = tk.Entry(create_task_window)
        description_entry.pack()

        # Luodaan DateEntry-komponentti, joka mahdollistaa dl. päivämäärän valitsemisen uuteen tehtävään.
        tk.Label(create_task_window, text="Due Date:").pack()
        due_date_entry = DateEntry(create_task_window)
        due_date_entry.pack()


        #Metodi, jonka avulla uusi tehtövö voidaaan luoda ja tallentaa.
        def save_task():
            
            title = title_entry.get() # Haetaan tehtävän nimi tekstikentästä.
            description = description_entry.get() # Haetaan tehtävän kuvaus tekstikentästä.
            due_date = due_date_entry.get_date() # Haetaan tehtävän deadline DateEntry-komponentista.
            folder_id = None  
            self.task_controller.create_task(title, description, due_date, folder_id) # Kutsutaan TaskControllerin create_task metodia, jotta tehtävä tallennetaan tietokantaan.
            self.refresh_tasks() # Päivitetään tehtävälista GUI:ssa.
            create_task_window.destroy() # Suljetaan ikkuna destroy() metodilla.

        # Luodaan painike, joka kutsuu save_task metodia ja mahdollistaa tehtävän tallentamisen.
        tk.Button(create_task_window, text="Save Task", command=save_task).pack()

    def delete_task(self):
        # Haetaan valitun tehtävän ID Listbox-komponentista.
        selected_task_id = self.tasks_listbox.curselection()
        print(selected_task_id)
        if selected_task_id:
            # Haetaan valitun tehtävän sisältö (otsikko ja due date).
            task_text = self.tasks_listbox.get(selected_task_id)
            print(task_text)
            # Haetaan tehtävän otsikko poistamalla ylimääräinen sisältö task_text.
            task_title = task_text.split(",")[0]
            print(task_title)
            # Haetaan tehtävä tietokannasta task_controllerin get_tasks metodilla.
            tasks = self.task_controller.get_tasks()
            # Etsitään tehtävä, jonka otsikko vastaa valitun tehtävän otsikkoa.
            task_to_delete = next((task for task in tasks if task[2] == task_title), None)

            # Jos tehtävä löytyy, poistetaan se tietokannasta task_controllerin avulla (joka käyttää task modelissa olevaa poisto metodia).
            if task_to_delete:
                task_id = task_to_delete[0] # Haetaan tehtävän ID.
                self.task_controller.delete_task(task_id)
                self.refresh_tasks()
            else:
                messagebox.showerror("Error", "Task not found")
        else:
            messagebox.showerror("Error", "Select a task to delete")



    # Metodi avaa uuden ikkunan, jossa käyttäjä voi luoda uuden kansion.
    def create_folder(self):
        
        # Luodaan uusi ikkuna kansion luomista varten.
        create_folder_window = tk.Toplevel(self.root)
        create_folder_window.title("Create Folder")

        # Luodaan tekstikenttä kansion nimen lisäämistä varten.
        tk.Label(create_folder_window, text="Folder Name:").pack()
        folder_name_entry = tk.Entry(create_folder_window)
        folder_name_entry.pack()

        # Metodi, jonka avulla uusi kansio voidaaan luoda ja tallentaa.
        def save_folder():
            
            name = folder_name_entry.get() # Haetaan kansion nimi tekstikentästä.
            # If metodin tarkoitus varmistaa, että kansion nimi ei ole tyhjä.
            if name:
                self.folder_controller.create_folder(name) # Kutsutaan FolderControllerin create_folder metodia, jotta kansio tallennetaan tietokantaan.
                self.refresh_folders() # Päivitetään kansioiden lista GUI:ssa.
                create_folder_window.destroy() # Suljetaan ikkuna destroy() metodilla.
            else:
                messagebox.showerror("Error", "Folder name cannot be empty") # Jos kansion nimi on tyhjä, näytetään virheilmoitus messagebox widgetillä.

        # Luodaan painike, joka kutsuu save_folder metodia ja mahdollistaa kansion tallentamisen.
        tk.Button(create_folder_window, text="Save Folder", command=save_folder).pack() 

    # Metodi päivittää tehtävät GUI:ssa.
    def refresh_tasks(self):
        self.tasks_listbox.delete(0, tk.END) # Tyhjennetään tehtävälista.

        tasks = self.task_controller.get_tasks() # Haetaan kaikki tehtävät tietokannasta.

        # Lisätään tehtävät Listbox-komponenttiin.
        for task in tasks:
            task_display = f"{task[2]}, Due Date: {task[4]}" # Muodostetaan tehtävän tiedot merkkijonoksi.
            self.tasks_listbox.insert(tk.END, task_display) # Lisätään tehtävä Listbox-komponenttiin.

    # Metodi päivittää kansiot GUI:ssa.
    def refresh_folders(self):
        self.folders_listbox.delete(0, tk.END) # Tyhjennetään kansioiden lista.

        folders = self.folder_controller.get_folders() # Haetaan kaikki kansiot tietokannasta.

        # Lisätään kansiot Listbox-komponenttiin.
        for folder in folders:
            self.folders_listbox.insert(tk.END, folder[1]) 
