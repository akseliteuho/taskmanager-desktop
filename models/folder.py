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
        db = Database() # Luodaan tietokanta yhteys luomalla Database luokan instanssi
        cursor = db.conn.execute("SELECT * FROM folders") # Haetaan kaikki kansiot tietokannasta SQL kyselyllä
        return cursor.fetchall() # Palautetaan kaikki kansiot listana
    
    @staticmethod
    def get_folder_by_id(folder_id):
        db = Database() # Luodaan tietokanta yhteys luomalla Database luokan instanssi
        cursor = db.conn.execute("SELECT * FROM folders WHERE id = ?", (folder_id,)) # Haetaan kansio kansion ID:n perusteella SQL kyselyllä
        return cursor.fetchone() # Palautetaan kansio

    # Poistetaan kansio tietokannasta kansion ID:n perusteella
    @staticmethod
    def delete_folder(folder_id): 
        db = Database() # Luodaan tietokanta yhteys
        with db.conn: # Avataan tietokanta yhteys
            db.conn.execute("DELETE FROM folders WHERE id = ?", (folder_id,)) # Poistetaan kansio tietokannasta SQL kyselyllä

    