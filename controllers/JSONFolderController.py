from models.JSONFolder import JSONFolder

class JSONFolderController:
    # Luodaan uusi kansio ja tallennetaan se tietokantaan
    def create_folder(self, name):
        folder = JSONFolder(name)
        folder.save()
    # Haetaan kaikki kansiot tietokannasta, kutsumalla Folder luokan get_all_folders metodia
    def get_folders(self):
        return JSONFolder.get_all_folders()

    # Haetaan kansio kansion ID:n perusteella, kutsumalla Folder luokan get_folder_by_id metodia
    def get_folder_by_id(self, folder_id):
        return JSONFolder.get_folder_by_id(folder_id)

    # Poistetaan kansio kansio tietokannasta, kutsumalla folder modelissa olevaa delete_folder metodia
    def delete_folder(self, folder_id):
        return JSONFolder.delete_folder(folder_id)