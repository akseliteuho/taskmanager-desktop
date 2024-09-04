from .database import Database

# Task luokka, jolla hallitaan/käsitellään tehtäviä
class Task:
    # Konstruktori, joka initialisoi Task luokan ominaisuudet
    def __init__(self, title, description='', due_date=None, folder_id=None):
        self.db = Database() # Luodaan tietokanta yhteys
        self.title = title # Tehtävän otsikko
        self.description = description # Tehtävän kuvaus
        self.due_date = due_date # Tehtävän deadline
        self.folder_id = folder_id # Kansion id, johon tehtävä kuuluu

    # Tallennetaan tehtävä tietokantaan
    def save(self):
        with self.db.conn: # Avataan tietokanta yhteys 

            # Lisätään tehtävä tietokantaan SQL kyselyllä
            self.db.conn.execute(
                "INSERT INTO tasks (folder_id, title, description, due_date) VALUES (?, ?, ?, ?)",
                (self.folder_id, self.title, self.description, self.due_date)
            )

    # Haetaan kaikki tehtävät tietokannasta ja palautetaan ne listana
    @staticmethod
    def get_all_tasks():
        db = Database() # Luodaan tiedokanta yhteys luomalla Database luokan instanssi
        cursor = db.conn.execute("SELECT * FROM tasks") # Haetaan kaikki tehtävät tietokannasta SQL kyselyllä
        return cursor.fetchall() # Palautetaan kaikki tehtävät listana

    # Poistetaan tehtävä tietokannasta tehtävän ID:n perusteella
    @staticmethod
    def delete_task(task_id):
        db = Database() # Luodaan tiedokanta yhteys luomalla Database luokan instanssi
        with db.conn: # Avataan tietokanta yhteys
            db.conn.execute("DELETE FROM tasks WHERE id = ?", (task_id,)) # Poistetaan tehtävä tietokannasta SQL kyselyllä