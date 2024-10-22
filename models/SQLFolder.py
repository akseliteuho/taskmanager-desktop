from .SQLDatabase import SQLDatabase

# Folder luokan avulla hallitaan/käsitellään kansioita.
class SQLFolder:
    # Konstruktori, joka saa parametrinaan kansion nimen ja luo yhteyden tietokantaan
    def __init__(self, name):
        self.db = SQLDatabase() # Luodaan tietokanta yhteys
        self.name = name # Asetetetaan kansion nimi, joka annetaan parametrina konsruktorille

    # Tallennetaan kansio tietokantaan lisäämällä kansion nimi tietokantaan
    def save(self):
        # Avataan tietokanta yhteys with metodin avulla, joka varmistaa että kaikki tietokanta operaatiot suoritetaan oikein ja tietokanta suljetaan automaattisesti.
        with self.db.conn:
            self.db.conn.execute("INSERT INTO folders (name) VALUES (?)", (self.name,))

    # Haetaan kaikki kansiot tietokannasta
    @staticmethod
    def get_all_folders():
        db = SQLDatabase() # Luodaan tietokanta yhteys luomalla Database luokan instanssi
        cursor = db.conn.execute("SELECT * FROM folders") # Haetaan kaikki kansiot tietokannasta SQL kyselyllä
        return cursor.fetchall() # Palautetaan kaikki kansiot listana
    
    # Haetaan kansio kansion nimen perusteella
    @staticmethod
    def get_folder_by_id(folder_id):
        db = SQLDatabase() # Luodaan tietokanta yhteys luomalla Database luokan instanssi
        cursor = db.conn.execute("SELECT * FROM folders WHERE id = ?", (folder_id,)) # Haetaan kansio kansion ID:n perusteella SQL kyselyllä
        return cursor.fetchone() # Palautetaan kansio

    # Poistetaan kansio tietokannasta kansion ID:n perusteella
    @staticmethod
    def delete_folder(folder_id): 
        db = SQLDatabase() # Luodaan tietokanta yhteys
        with db.conn: # Avataan tietokanta yhteys
            db.conn.execute("DELETE FROM folders WHERE id = ?", (folder_id,)) # Poistetaan kansio tietokannasta SQL kyselyllä
        return True # Palautetaan True, jos kansio on poistettu onnistuneesti, jotta GUI toimii oikein.
    