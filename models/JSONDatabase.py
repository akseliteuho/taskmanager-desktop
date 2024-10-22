import json
import os

# JSONDatabase luokka, joka vastaa JSON tietokannan toiminnoista
class JSONDatabase:
    def __init__(self, db_file="json.db"): # JSONDatabase luokan konstruktori, joka saa parametrinaan tietokannan nimen ja alustaa tietokanta tiedoston
        self.db_file = db_file # db_file sisältää polun JSON tietokantaan

        # Tarkistetetaan onko tietokanta olemassa
        if not os.path.exists(self.db_file) or os.path.getsize(self.db_file) == 0: # Jos tietokantaa ei ole olemassa tai sen koko on 0
            self._initialize_database() # Alustetaan tietokanta kutsumalla _initialize_database metodia

    # Metodi, joka alutaa tietokannan
    def _initialize_database(self):
        # Alustetaan tietokanta tyhjällä data dictionary rakenteella
        data = {
            "folders": [], # Tyhjä kansio lista
            "tasks": [] # Tyhjä tehtävä lista
        }
        self._write_data(data) # Kirjoitaetaan tyhjä data rakenne JSON tietokanta tiedostoon kutsumalla _write_data metodia.

    # Metodi, joka hakee kaikki tiedot tietokannasta python dictionary rakenteena
    def _read_data(self):
        with open(self.db_file, "r") as f: # Avataan JSON tiedosto lukutilassa (r) with metodin avulla
            return json.load(f) # Palautetaan JSON tiedoston data python dictionary rakenteena

    # Metodi, joka kirjoittaa dataa tietokantaan
    def _write_data(self, data):
        with open(self.db_file, "w") as f: # Avataan JSON tiedosto kirjoitustilassa (w) with metodin avulla
            
            # Muutetaan python dictionary JSON muotoon ja kirjoitetaan JSON tiedostoon.
            #indent=4' varmistaa, että JSON-data on muotoiltu sisennyksellä luettavuuden vuoksi.
            json.dump(data, f, indent=4) 
