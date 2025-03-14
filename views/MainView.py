import tkinter as tk
from tkinter import messagebox
from tkcalendar import DateEntry
from controllers.SQLTaskController import SQLTaskController
from controllers.SQLFolderController import SQLFolderController
from controllers.JSONTaskController import JSONTaskController
from controllers.JSONFolderController import JSONFolderController
from datetime import datetime
from utils.notifications import show_notification


# MainView luokka on vastuussa käyttöliittymän alustamisesta ja hallitsemisesta.
class MainView:
    # MainView luokan konstruktori, joka alustaa MainView luokan ominaisuudet, jossa root olio kuvastaa ohjelman pääikkunaa.
    def __init__(self, root):
        self.root = root # Asetetaan root olio MainView luokan ominaisuudeksi, jotta sitä voidaan käyttää muissa metodeissa.
        self.root.title("Task Manager")
        self.database_selection() # Kutsutaan database_selection metodia, joka luo uuden ikkunan tietokannan valintaa varten.

    def database_selection(self):
        # Luodaan uusi ikkuna tietokannan valintaa varten.
        database_selection_window = tk.Toplevel(self.root)
        database_selection_window.title("Select Database")

        tk.Label(database_selection_window, text="Select database type").pack(pady=10)

        # Lambda funktion avulla initialize_database ajetaan vasta, kun painiketta painetaan. Ilman tätä painike ei siis toimisi oikein.
        # Luodaan painike SQL tietokannan valintaa varten.
        sql_button = tk.Button(database_selection_window, text="SQL Database", command=lambda: self.initialize_database('SQL', database_selection_window))
        sql_button.pack()
        # Luodaan painike JSON tietokannan valintaa varten.
        json_button = tk.Button(database_selection_window, text="JSON Database", command=lambda: self.initialize_database('JSON', database_selection_window))
        json_button.pack() 


    # Metodi alustaa tietokannan valinnan perusteella joko SQL tai JSON tietokannan.
    def initialize_database(self, database_type, window):
        # Luodaan TaskController ja FolderController instanssit riippuen valitusta tietokannasta.
        if database_type == 'SQL':
            self.task_controller = SQLTaskController()
            self.folder_controller = SQLFolderController()
        elif database_type == 'JSON':
            self.task_controller = JSONTaskController()
            self.folder_controller = JSONFolderController()

        window.destroy() # Suljetaan ikkuna destroy() metodilla.


        # Kutsutaan create_widgets -metodia, joka luo GUI:n komponentit.
        self.create_widgets()
        # Kutsutaan check_due_dates metodia, joka tarkistaa onko tehtävän deadline mennyt.
        self.check_due_dates()


    # Metodi luo GUI:n komponentit.
    def create_widgets(self):

        #TASK Buttons

        # Luodaan Frame-komponentti, task painikkeiden sijoittamista varten.
        task_button_frame = tk.Frame(self.root)
        task_button_frame.pack(fill=tk.X, padx=20, pady=5)
        task_button_frame.pack_propagate(False)
        
        # Luodaan painike, joka kutsuu create_task metodia ja mahdollistaa uuden tehtävän luomisen.
        self.create_task_button = tk.Button(task_button_frame, text="Create Task", command=self.create_task)
        self.create_task_button.grid(row=0, column=0, padx=5)

        # Luodaan painike, joka kutsuu delete_task metodia ja mahdollistaa tehtävän poistamisen.
        self.delete_task_button = tk.Button(task_button_frame, text="Delete Task", command=self.delete_task)
        self.delete_task_button.grid(row=0, column=1, padx=5)

        # Luodaan Listbox-komponentti, johon lisätään tehtävät.
        self.tasks_listbox = tk.Listbox(self.root)
        self.tasks_listbox.pack(fill=tk.BOTH, expand=True, padx=20, pady=5)

        # Luodaan Frame-komponentti, folder painikkeiden sijoittamista varten.
        folder_button_frame = tk.Frame(self.root)
        folder_button_frame.pack(fill=tk.X, padx=20, pady=5)
        folder_button_frame.pack_propagate(False)

        # Luodaan painike, joka kutsuu create_folder metodia ja mahdollistaa uuden kansion luomisen.
        self.create_folder_button = tk.Button(folder_button_frame, text="Create Folder", command=self.create_folder)
        self.create_folder_button.grid(row=0, column=0, padx=5)

        # Luodaan painike, joka kutsuu delete_folder metodia ja mahdollistaa kansion poistamisen.
        self.delete_folder_button = tk.Button(folder_button_frame, text="Delete Folder", command=self.delete_folder)
        self.delete_folder_button.grid(row=0, column=1, padx=5)

        # Luodaan painike, joka kutsuu show_all_tasks metodia ja mahdollistaa palaamisen alkunäyttötilaan.
        self.return_to_mainview_button = tk.Button(self.root, text="Return to Main View", command=self.show_all_tasks)
        self.return_to_mainview_button.pack()
        self.return_to_mainview_button.pack_forget() # Piilotetaan painike, kun se ei ole tarpeellinen, eli kun palataan päänäyttöön.

        # Luodaan Listbox-komponentti, johon lisätään kansiot.
        self.folders_listbox = tk.Listbox(self.root)
        self.folders_listbox.pack(fill=tk.BOTH, expand=True, padx=20, pady=5)

        # Listbox-komponenttiin lisätään tapahtumankäsittelijä, joka kutsuu display_tasks_in_folder metodia, kun käyttäjä valitsee kansion.
        self.folders_listbox.bind("<<ListboxSelect>>", self.display_tasks_in_folder)

        # Päivitetään tehtävät ja kansiot, jotta ne saadaan näkyviin.
        self.refresh_tasks()
        self.refresh_folders()

    # Metodi tarkistaa onko tehtävän deadline mennyt.
    def check_due_dates(self):
        # Haetaan kaikki tehtävät task_controllerin avulla, joiden deadline on tänään ja tallennetaan ne muuttujaan.
        tasks_due_today = self.task_controller.get_tasks_due_today()

        # Käydään läpi kaikki tehtävät, joiden deadline on tänään.
        for task in tasks_due_today:
            # Kutsutaan show_notification metodia notifcations luokasta, ja näytetään ilmoitus, jossa kerrotaan, että tehtävän deadline on tänään.
            show_notification("Task due", f"This task is due today!\n {task['title']}")
 

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

        # Luodaan DateEntry-komponentti kalenteriin, joka mahdollistaa dl. päivämäärän valitsemisen uuteen tehtävään.
        tk.Label(create_task_window, text="Due Date:").pack()
        due_date_entry = DateEntry(create_task_window, width=12, background='darkblue', foreground='white', borderwidth=2)
        due_date_entry.pack(pady=20)
        due_date_entry.focus_set()

        # Tekstikenttä tehtävän kansioon liittämistä varten.
        tk.Label(create_task_window, text="Select Folder:").pack() 
        folder_selection = tk.Listbox(create_task_window, height=5)

        # Haetaan kaikki kansiot, jotta ne voidaan lisätä Listbox-komponenttiin.
        folders = self.folder_controller.folders_for_selection()
        folder_ids = [] # Luodaan lista, johon tallennetaan kansio id:t.

        # Käydään läpi kaikki kansiot ja lisätään ne Listbox-komponenttiin.
        for folder in folders:
            folder_selection.insert(tk.END, folder['name']) # Lisätään kansio Listbox-komponenttiin.
            folder_ids.append(folder['id']) # Lisätään kansio id folder_ids listaan.
   
        folder_selection.pack()

        #Metodi, jonka avulla uusi tehtövö voidaaan luoda ja tallentaa controller luokkien avulla.
        def save_task():
            title = title_entry.get() # Haetaan tehtävän nimi tekstikentästä get() metodilla ja tallennetaan se muuttujaan.
            description = description_entry.get() # Haetaan tehtävän kuvaus tekstikentästä.
            due_date = due_date_entry.get_date() # Haetaan tehtävän deadline DateEntry-komponentista.

            selected_folder_id = folder_selection.curselection() # Haetaan valittu kansio listbox-komponentista (palautaa indeksin).
            if selected_folder_id:
                folder_id = folder_ids[selected_folder_id[0]] # Haetaan valitun kansion ID folder_ids listasta.
            else:
                folder_id = None  # Jos kansiota ei ole valittu, asetetaan folder_id arvoksi None.
                print("No folder selected")
            self.task_controller.create_task(title, description, due_date, folder_id) # Kutsutaan TaskControllerin create_task metodia, jotta tehtävä tallennetaan tietokantaan.
            self.refresh_tasks() # Päivitetään tehtävälista GUI:ssa.
            create_task_window.destroy() # Suljetaan ikkuna destroy() metodilla.

        # Luodaan painike, joka kutsuu save_task metodia ja mahdollistaa tehtävän tallentamisen.
        tk.Button(create_task_window, text="Save Task", command=save_task).pack()


    # Metodi näyttää kaikki tehtävät valitussa kansiossa. Koska metodi on tapahtumankäsittelijä, se saa parametrin event.
    def display_tasks_in_folder(self, event):
        # Haetaan valitun kansion ID Listbox-komponentista.
        selected_folder_id = self.folders_listbox.curselection()
        print(selected_folder_id)

        # Jos kansio on valittu, haetaan kansion tehtävät ja näytetään ne GUI:ssa.
        if selected_folder_id:
            # Haetaan valitun kansion ID folder_ids listasta.
            folder_id = self.folder_ids[selected_folder_id[0]]
            print(folder_id)
            # Haetaan kaikki kansiot task_controllerin avulla ja tallennetaan ne muuttujaan.
            tasks = self.task_controller.get_tasks_by_folder_id(folder_id)
            print(tasks)

            self.return_to_mainview_button.pack() # Näytetään painike, joka mahdollistaa palaamisen alkunäyttötilaan.
            self.tasks_listbox.delete(0, tk.END) # Tyhjennetään tehtävälista, ennen kuin lisätään uudet tehtävät.

            # Käydään haetut tehtävät läpi ja lisätään ne Listbox-komponenttiin niiden näyttämiseksi.
            for task in tasks:
                # Muodostetaan tehtävän tiedot merkkijonoksi.
                task_display = f"{task['title']}, {task['description']}, Due Date: {task['due_date']}"
                self.tasks_listbox.insert(tk.END, task_display) # Lisätään tehtävä Listbox-komponenttiin.


    # Metodi, jonka avulla valittu tehtävä voidaan poistaa.
    def delete_task(self):
        # Haetaan valitun tehtävän ID Listbox-komponentista.
        selected_task_id = self.tasks_listbox.curselection()
        print(selected_task_id)

        # Jos tehtävä on valittu, poistetaan se tietokannasta.
        if selected_task_id:

            # Haetaan valitun tehtävän kaikki näkyvät tiedot Listbox-komponentista ja tallennetaan ne muuttujaan.
            task_text = self.tasks_listbox.get(selected_task_id)
            print(task_text)

            # Erotetaan tehtävän otsikko task_text muuttujasta. Otsikko on ensimmäinen osa, joka erotetaan pilkulla ',' ja välilyönnillä.
            # Tämä tehdään, jotta otsikko saadaan helposti poistamista varten.
            task_title = task_text.split(",")[0]
            print(task_title)

            # Haetaan tehtävän tiedot task_controllerin avulla ja tallennetaan se muuttujaan, jotta se voidaan poistaa sen otsikon perusteella.
            task_to_delete = self.task_controller.delete_task_by_title(task_title)

            
            # Jos tehtävä löytyy, poistetaan se tietokannasta task_controllerin avulla.
            if task_to_delete:
                task_id = task_to_delete['id'] # Tallennetaan tehtävän ID muuttujaan, jotta sitä voidaan käyttää poistamisessa.
                self.task_controller.delete_task(task_id) # Poistetaan tehtävä tietokannasta task_controllerin avulla, joka käyttää delete_task metodia.
                self.refresh_tasks() # Päivitetään tehtävät GUI:ssa.
            else:
                messagebox.showerror("Error", "Task not found")
        else:
            messagebox.showerror("Error", "Select a task to delete")


    # Metodi näyttää kaikki tehtävät GUI:ssa, käytetään kun halutaan palata alkunäyttötilaan folder näkymästä.
    def show_all_tasks(self):
        self.return_to_mainview_button.pack_forget() # Piilotetaan painike pack_forget() metodilla, kun se ei ole enää tarpeellinen.
        self.refresh_tasks() # Päivitetään tehtävät GUI:ssa.


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

        # Luodaan painike, joka kutsuu save_folder metodia painettaessa ja mahdollistaa kansion tallentamisen.
        tk.Button(create_folder_window, text="Save Folder", command=save_folder).pack() 


    # Metodi, jonka avulla valittu kansio voidaan poistaa.
    def delete_folder(self):
        # Haetaan valitun kansion ID Listbox-komponentista ja tallennetaan se muuttujaan.
        selected_folder_id = self.folders_listbox.curselection()
        if selected_folder_id:
            # Haetaan valitun kansion nimi Listbox-komponentista.
            folder_name = self.folders_listbox.get(selected_folder_id)

            # Hoidetaan kansion poistaminen folder controllerin avulla kansion nimen perusteella.
            folder_deletion = self.folder_controller.delete_folder_by_name(folder_name)

            # Jos kansion poisto onnistui, päivitetään kansioiden lista GUI:ssa.
            if folder_deletion:
                self.refresh_folders()
            else:
                messagebox.showerror("Error", "Folder not found")
        else:
            messagebox.showerror("Error", "Select a folder to delete")


    # Metodi päivittää tehtävät GUI:ssa, jotta ne näkyvät oikein.
    def refresh_tasks(self):
        self.tasks_listbox.delete(0, tk.END) # Tyhjennetään tehtävälista.
        tasks = self.task_controller.get_tasks() # Haetaan kaikki tehtävät tietokannasta.

        # Lisätään tehtävät Listbox-komponenttiin.
        for task in tasks:
            task_display = f"{task['title']}, {task['description']}, Due Date: {task['due_date']}" # Muodostetaan tehtävän tiedot merkkijonoksi.
            self.tasks_listbox.insert(tk.END, task_display) # Lisätään tehtävä Listbox-komponenttiin.


    # Metodi päivittää kansiot GUI:ssa, jotta ne näkyvät oikein.
    def refresh_folders(self):
        self.folders_listbox.delete(0, tk.END) # Tyhjennetään kansioiden lista.
        folders = self.folder_controller.get_folders() # Haetaan kaikki kansiot tietokannasta.

        self.folder_ids = [] # Luodaan lista, johon tallennetaan kansio id:t.

        # Lisätään kansiot Listbox-komponenttiin.
        for folder in folders:
            folder_name = folder['name']
            folder_id = folder['id']

            self.folders_listbox.insert(tk.END, folder_name) # Lisätään kansio Listbox-komponenttiin.
            self.folder_ids.append(folder_id) # Lisätään kansio id folder_ids listaan.