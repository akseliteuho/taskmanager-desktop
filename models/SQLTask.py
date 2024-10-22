from .SQLDatabase import SQLDatabase

# Task luokka, jolla hallitaan/käsitellään tehtäviä SQL tietokannassa
class SQLTask:
    # Konstruktori, joka initialisoi Task luokan ominaisuudet ja luo yhteyden tietokantaan
    def __init__(self, title, description='', due_date=None, folder_id=None):
        self.db = SQLDatabase() # Luodaan tietokanta yhteys
        self.title = title # Tehtävän otsikko
        self.description = description # Tehtävän kuvaus
        self.due_date = due_date # Tehtävän deadline
        self.folder_id = folder_id # Kansion id, johon tehtävä kuuluu

    # Tallennetaan tehtävä SQL tietokantaan
    def save(self):
        with self.db.conn: # Avataan tietokanta yhteys with metodin avulla, joka varmistaa että kaikki tietokanta operaatiot suoritetaan oikein ja tietokanta suljetaan automaattisesti.

            # Lisätään tehtävä tietokantaan SQL kyselyllä
            self.db.conn.execute(
                "INSERT INTO tasks (folder_id, title, description, due_date) VALUES (?, ?, ?, ?)",
                (self.folder_id, self.title, self.description, self.due_date) # Tehtävän tiedot
            )

    # Haetaan kaikki tehtävät tietokannasta ja palautetaan ne listana
    @staticmethod
    def get_all_tasks():
        db = SQLDatabase() # Luodaan tiedokanta yhteys luomalla Database luokan instanssi
        cursor = db.conn.execute("SELECT * FROM tasks") # Haetaan kaikki tehtävät tietokannasta SQL kyselyllä
        return cursor.fetchall() # Palautetaan kaikki tehtävät listana

    # Haetaan tehtävät kansion ID:n perusteella
    @staticmethod
    def get_tasks_by_folder_id(folder_id):
        db = SQLDatabase() # Luodaan tiedokanta yhteys luomalla Database luokan instanssi
        cursor = db.conn.execute("SELECT * FROM tasks WHERE folder_id = ?", (folder_id,)) # Haetaan tehtävät kansion ID:n perusteella SQL kyselyllä
        return cursor.fetchall() # Palautetaan tehtävät listana

    # Poistetaan tehtävä tietokannasta tehtävän ID:n perusteella
    @staticmethod
    def delete_task(task_id):
        db = SQLDatabase() # Luodaan tiedokanta yhteys luomalla Database luokan instanssi
        with db.conn: # Avataan tietokanta yhteys
            db.conn.execute("DELETE FROM tasks WHERE id = ?", (task_id,)) # Poistetaan tehtävä tietokannasta SQL kyselyllä