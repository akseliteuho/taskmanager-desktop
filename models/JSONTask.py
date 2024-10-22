from .JSONDatabase import JSONDatabase
import datetime

# Luodaan JSONTask luokka, joka vastaa tehtävien hallinnasta JSON tietokannassa
class JSONTask:
    # Konstruktori, joka initialisoi Task luokan ominaisuudet
    def __init__(self, title, description='', due_date=None, folder_id=None):
        self.db = JSONDatabase() # Luodaan tietokanta yhteys
        self.title = title # Tehtävän otsikko
        self.description = description # Tehtävän kuvaus
        self.due_date = due_date # Tehtävän deadline
        self.folder_id = folder_id # Kansion id, johon tehtävä kuuluu

    # Tallennetaan tehtävä JSON tietokantaan
    def save(self):
        # Luetaan olemassa olevat tiedot tietokannasta _read_data metodilla ja tallennetaan ne muuttujaan
        data = self.db._read_data()

        # Jos tehtäviä on olemassa, haetaan suurin ID ja lisätään yksi, jotta saadaan uusi ID. Muuten ID on 1.
        if data["tasks"]:
            task_id = max([task["id"] for task in data["tasks"]]) + 1 # Luodaan uusi ID, joka on suurempi kuin suurin olemassa oleva ID
        else:
            task_id = 1

        # Uusi task objekti
        # Duedate piti muuttaa ISO muotoon, jotta se voidaan tallentaa JSON tiedostoon
        task = {
            "id": task_id, # Uusi ID
            "title": self.title, # Tehtävän otsikko
            "description": self.description, # Tehtävän kuvaus
            "due_date": self.due_date.isoformat() if self.due_date else None, # Tehtävän deadline
            "folder_id": self.folder_id # Kansion ID, johon tehtävä kuuluu
        }
        data["tasks"].append(task) # Lisätään tehtävä listaan
        self.db._write_data(data) # Viedään päivitetyt tiedot tietokantaan _write_data metodilla

    # Haetaan kaikki tehtävät tietokannasta
    @staticmethod
    def get_all_tasks():
        db = JSONDatabase() # Luodaan tietokanta yhteys
        data = db._read_data() # Luetaan tietokannan tiedot
        return data["tasks"] # Palautetaan kaikki tehtävät listana

    # Haetaan tehtävät kansion ID:n perusteella
    @staticmethod
    def get_tasks_by_folder_id(folder_id):
        db = JSONDatabase() # Luodaan tietokanta yhteys
        data = db._read_data() # Luetaan tietokannan tiedot
        return [task for task in data["tasks"] if task["folder_id"] == folder_id] # Palautetaan tehtävät listana

    # Poistetaan tehtävä tietokannasta tehtävän ID:n perusteella
    @staticmethod
    def delete_task(task_id):
        db = JSONDatabase() # Luodaan tietokanta yhteys
        data = db._read_data() # Luetaan tietokannan tiedot
        data["tasks"] = [task for task in data["tasks"] if task["id"] != task_id] # Käydään läpi tehtävien lista ja luodaan uusi, jossa ei ole poistettavaa tehtävää
        db._write_data(data) # Viedään päivitetyt tiedot tietokantaan