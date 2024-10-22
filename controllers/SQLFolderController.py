from models.SQLFolder import SQLFolder

class SQLFolderController:
    # Luodaan uusi kansio ja tallennetaan se tietokantaan kutsumalla SQLFolder luokan save metodia
    def create_folder(self, name):
        folder = SQLFolder(name)
        folder.save()


    # Metodi, joka palauttaa kaikki kansiot listana, jotta taskeja voidaan lisätä niihin
    def folders_for_selection(self):
        folders = SQLFolder.get_all_folders() # Haetaan kaikki kansiot
        folder_list = [] # Luodaan lista, johon lisätään kansiot

        # Käydään läpi kaikki kansiot ja lisätään ne listaan
        for folder in folders:
            folder_list.append({
                'id': folder[0], # Kansion ID
                'name': folder[1] # Kansion nimi
            })
        return folder_list # Palautetaan kansiot listana
    

    # Poistetaan kansio kansion nimen perusteella, kutsumalla Folder luokan delete_folder_by_name metodia
    def delete_folder_by_name(self, folder_name):
        # Haetaan kaikki kansiot ja tallennetaan ne muuttujaan 
        folders = SQLFolder.get_all_folders()

        # Käydään läpi kaikki kansiot muuttujassa ja etsitään poistettava kansio
        folder_to_delete = None
        for folder in folders:
            # folder[1] viittaa kansion nimeen (koska kansiot palautetaan tupleina (id, name), nimi on indeksissä 1)
            if folder[1] == folder_name: # Tarkistetaan vastaako kansio annettua nimeä
                folder_to_delete = folder # Tallennetaan poistettava kansio muuttujaan
                break # Poistutaan silmukasta, koska poistettava kansio on löytynyt
        
        # Jos kansio löytyi, poistetaan se
        if folder_to_delete:
            folder_id = folder_to_delete[0] # Haetaan poistettavab kansion ID
            return SQLFolder.delete_folder(folder_id) # Palauttaa True, jos poisto onnistui
        else:
            return False
        

    # Haetaan kaikki kansiot tietokannasta, kutsumalla Folder luokan get_all_folders metodia
    def get_folders(self):
        folders = SQLFolder.get_all_folders() # Haetaan kaikki kansiot
        # Palautetaan kansiot listana ja muutetaan tuple sanakirjaksi
        return [{'id': folder[0], 'name': folder[1]} for folder in folders]
    

    # Haetaan kansio kansion ID:n perusteella, kutsumalla Folder luokan get_folder_by_id metodia
    def get_folder_by_id(self, folder_id):
        return SQLFolder.get_folder_by_id(folder_id)


    # Poistetaan kansio kansio tietokannasta, kutsumalla folder modelissa olevaa delete_folder metodia
    def delete_folder(self, folder_id):
        return SQLFolder.delete_folder(folder_id)