import json
import os

class JSONDatabase:
    def __init__(self, db_file="json.db"): # JSONDatabase luokan konstruktori, joka saa parametrinaan tietokannan nimen
        self.db_file = db_file # db_file sisältää polun JSON tietokantaan

        # Tarkistetaan tietokannan olemassa olo ja luodaan tietokanta, jos sitä ei ole olemassa
        if not os.path.exists(self.db_file) or os.path.getsize(self.db_file) == 0: # Jos tietokantaa ei ole olemassa tai sen koko on 0
            self._initialize_database()

    # Metodi, joka alutaa tietokannan
    def _initialize_database(self):
        # Alustetaan tietokanta tyhjällä data dictionary rakenteella
        data = {
            "folders": [],
            "tasks": []
        }
        self._write_data(data) # Kirjoitaetaan tyhjä data rakenne JSON tiedostoon kutsumalla _write_data metodia.

    # Metodi, joka hakee kaikki tiedot tietokannasta python dictionary rakenteena
    def _read_data(self):
        with open(self.db_file, "r") as f: # Avataan JSON tiedosto lukutilassa (r) with metodin avulla
            return json.load(f) # Palautetaan JSON tiedoston data python dictionary rakenteena

    # Metodi, joka kirjoittaa dataa tietokantaan
    def _write_data(self, data):
        with open(self.db_file, "w") as f: # Avataan JSON tiedosto kirjoitustilassa (w) with metodin avulla
            json.dump(data, f, indent=4) # Muutetaan python dictionary JSON muotoon ja kirjoitetaan JSON tiedostoon
