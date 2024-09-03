from .database import Database

# Folder luokan avulla hallitaan/käsitellään kansioita.
class Folder:

    # Konstruktori, joka saa parametrinaan kansion nimen
    def __init__(self, name):
        self.db = Database()
        self.name = name

    # Tallennetaan kansio tietokantaan lisäämällä kansion nimi tietokantaan
    def save(self):
        with self.db.conn:
            self.db.conn.execute("INSERT INTO folders (name) VALUES (?)", (self.name,))

    # Haetaan kaikki kansiot tietokannasta
    @staticmethod
    def get_all_folders():
        db = Database()
        cursor = db.conn.execute("SELECT * FROM folders")
        return cursor.fetchall()

