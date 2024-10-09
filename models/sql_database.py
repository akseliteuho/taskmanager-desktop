import sqlite3
from .database import Database

# Periytetään Database luokka SQLDatabase luokasta
class SQLDatabase():
    def __init__(self, db_name="tasks.db"): # Initalisoidaan SQLite tietokanta
        self.conn = sqlite3.connect(db_name) # Yhdistetään tietokantaan 
        self.create_tables() # Luodaan tietokannan taulut

    # Luodaan sqlite tietokannan taulut
    def create_tables(self):
        with self.conn: # Avataan tietokanta yhteys käyttäen context manageria, joka huolehtii tietokannasta automaattisesti
            # Luodaan kansiot taulu
            self.conn.execute(
                """CREATE TABLE IF NOT EXISTS folders (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL
                )"""
            )
            # Luodaan tehtävät taulu
            self.conn.execute(
                """CREATE TABLE IF NOT EXISTS tasks (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    folder_id INTEGER,
                    title TEXT NOT NULL,
                    description TEXT,
                    due_date TEXT,
                    FOREIGN KEY(folder_id) REFERENCES folders(id)
                )"""
            )

 # Haetaan kaikki tehtävät tietokannasta ja palautetaan ne listana
    @staticmethod
    def get_all_tasks():
        db = SQLDatabase() # Luodaan tiedokanta yhteys luomalla Database luokan instanssi
        cursor = db.conn.execute("SELECT * FROM tasks") # Haetaan kaikki tehtävät tietokannasta SQL kyselyllä
        return cursor.fetchall() # Palautetaan kaikki tehtävät listana