from .JSONDatabase import JSONDatabase

# Luodaan JSONFolder luokka, joka vastaa kansioiden hallinnasta JSON tietokannassa
class JSONFolder:
    # Konstruktori, joka initialisoi Folder luokan ominaisuudet ja luo yhteyden tietokantaan
    def __init__(self, name):
        self.db = JSONDatabase() # Luodaan tietokanta yhteys
        self.name = name # Asetetetaan kansion nimi, joka annetaan parametrina konsruktorille

    # Tallennetaan kansio JSON tietokantaan 
    def save(self):
        data = self.db._read_data() # Luetaan tietokannan tiedot _read_data metodilla ja tallennetaan ne muuttujaan

        # Jos kansioita on olemassa, haetaan suurin ID ja lisätään yksi, jotta saadaan uusi ID. Muuten ID on 1.
        if data["folders"]: 
            folder_id = max([folder["id"] for folder in data["folders"]]) + 1 # Luodaan uusi ID, joka on suurempi kuin suurin olemassa oleva ID
        else:
            folder_id = 1
        # Kansion tiedot
        folder = {
            "id": folder_id, 
            "name": self.name
        }
        data["folders"].append(folder) # Lisätään kansio listaan
        self.db._write_data(data) # Viedään päivitetyt tiedot tietokantaan _write_data metodilla

    # Haetaan kaikki kansiot tietokannasta
    @staticmethod
    def get_all_folders():
        db = JSONDatabase() # Luodaan tietokanta yhteys
        data = db._read_data() # Luetaan tietokannan tiedot
        return data["folders"] # Palautetaan kaikki kansiot listana
    
    # Haetaan kansio kansion ID:n perusteella
    @staticmethod
    def get_folder_by_id(folder_id):
        db = JSONDatabase() # Luodaan tietokanta yhteys
        data = db._read_data() # Luetaan tietokannan tiedot
        return [folder for folder in data["folders"] if folder["id"] == folder_id] # Palautetaan kansio sen ID:n perusteella

    # Poistetaan kansio tietokannasta kansion ID:n perusteella
    @staticmethod
    def delete_folder(folder_id):
        db = JSONDatabase() # Luodaan tietokanta yhteys
        data = db._read_data() # Luetaan tietokannan tiedot
        data["folders"] = [folder for folder in data["folders"] if folder["id"] != folder_id] # Käydään läpi kansioden lista ja luodaan uusi, jossa ei ole poistettavaa kansiota
        db._write_data(data) # Viedään päivitetyt tiedot tietokantaan
        return True # Palautetaan True, jos kansio on poistettu onnistuneesti, jotta GUI toimii oikein.