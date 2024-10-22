from models.JSONFolder import JSONFolder

class JSONFolderController:
    # Luodaan uusi kansio ja tallennetaan se tietokantaan kutsumalla JSONFolder luokan save metodia
    def create_folder(self, name):
        folder = JSONFolder(name) # Luodaan uusi kansio JSONFolder luokan avulla
        folder.save() # Tallennetaan kansio tietokantaan kutsumalla save metodia JSONFolder luokasta


    # Metodi, joka palauttaa kaikki kansiot listana, jotta taskeja voidaan lisätä niihin
    def folders_for_selection(self):
        folders = JSONFolder.get_all_folders() # Haetaan kaikki kansiot ja tallennetaan ne muuttujaan JSONFolder luokan avulla
        folder_list = [] # Luodaan lista, johon lisätään kansiot

        # Käydään läpi kaikki kansiot ja lisätään ne listaan
        for folder in folders:
            folder_list.append({
                'id': folder["id"], # Kansion ID
                'name': folder["name"] # Kansion nimi
            })
        return folder_list # Palautetaan kansiot listana
    

    # Haetaan poistettava kansio sen nimen perusteella ja poistetaan se sen ID:n perusteella kutsumalla JSONFolder luokan delete_folder metodia
    def delete_folder_by_name(self, folder_name):
        folders = JSONFolder.get_all_folders() # Haetaan kaikki kansiot ja tallennetaan ne muuttujaan folders

        # Käydään läpi kaikki kansiot muuttujassa ja etsitään poistettava kansio
        folder_to_delete = None
        for folder in folders:
            if folder["name"] == folder_name: # Tarkistetaan vastaako kansion nimi annettua nimeä
                folder_to_delete = folder # Tallennetaan poistettava kansio muuttujaan
                break # Poistutaan silmukasta, koska poistettava kansio on löytynyt
        
        # Jos kansio löytyi, poistetaan se
        if folder_to_delete:
            folder_id = folder_to_delete["id"] # Haetaan poistettavan kansion ID
            return JSONFolder.delete_folder(folder_id) # Poistetaan kansio kutsumalla delete_folder metodia JSONFolder luokasta
        else:
            return False # Palauttaa False, jos poistettavaa kansiota ei löytynyt


    # Haetaan kaikki kansiot tietokannasta, kutsumalla JSONFolder luokan get_all_folders metodia
    def get_folders(self):
        return JSONFolder.get_all_folders()


    # Haetaan kansio kansion ID:n perusteella, kutsumalla JSONFolder luokan get_folder_by_id metodia
    def get_folder_by_id(self, folder_id):
        return JSONFolder.get_folder_by_id(folder_id)


    # Poistetaan kansio tietokannasta, kutsumalla JSONFolder luokan olevaa delete_folder metodia
    def delete_folder(self, folder_id):
        return JSONFolder.delete_folder(folder_id)