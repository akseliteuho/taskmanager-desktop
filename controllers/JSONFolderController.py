from models.JSONFolder import JSONFolder

class JSONFolderController:
    # Luodaan uusi kansio ja tallennetaan se tietokantaan
    def create_folder(self, name):
        folder = JSONFolder(name)
        folder.save()

    # Poistetaan kansio kansion nimen perusteella, kutsumalla Folder luokan delete_folder_by_name metodia
    def delete_folder_by_name(self, folder_name):
        folders = JSONFolder.get_all_folders() # Haetaan kaikki kansiot ja tallennetaan ne muuttujaan

        # Käydään läpi kaikki kansiot muuttujassa ja etsitään poistettava kansio
        folder_to_delete = None
        for folder in folders:
            if folder["name"] == folder_name: # Tarkistetaan vastaako kansio annettua nimeä
                folder_to_delete = folder # Tallennetaan poistettava kansio muuttujaan
                break # Poistutaan silmukasta, koska poistettava kansio on löytynyt
        
        # Jos kansio löytyi, poistetaan se
        if folder_to_delete:
            folder_id = folder_to_delete["id"] # Haetaan poistettavan kansion ID
            return JSONFolder.delete_folder(folder_id) # Palauttaa True, jos poisto onnistui
        else:
            return False # Palauttaa False, jos poistettavaa kansiota ei löytynyt

    # Haetaan kaikki kansiot tietokannasta, kutsumalla Folder luokan get_all_folders metodia
    def get_folders(self):
        return JSONFolder.get_all_folders()

    # Haetaan kansio kansion ID:n perusteella, kutsumalla Folder luokan get_folder_by_id metodia
    def get_folder_by_id(self, folder_id):
        return JSONFolder.get_folder_by_id(folder_id)

    # Poistetaan kansio kansio tietokannasta, kutsumalla folder modelissa olevaa delete_folder metodia
    def delete_folder(self, folder_id):
        return JSONFolder.delete_folder(folder_id)