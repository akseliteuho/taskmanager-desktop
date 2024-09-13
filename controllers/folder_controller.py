from models.folder import Folder

class FolderController:
    # Luodaan uusi kansio ja tallennetaan se tietokantaan
    def create_folder(self, name):
        folder = Folder(name)
        folder.save()
    # Haetaan kaikki kansiot tietokannasta, kutsumalla Folder luokan get_all_folders metodia
    def get_folders(self):
        return Folder.get_all_folders()

    # Haetaan kansio kansion ID:n perusteella, kutsumalla Folder luokan get_folder_by_id metodia
    def get_folder_by_id(self, folder_id):
        return Folder.get_folder_by_id(folder_id)

    # Poistetaan kansio kansio tietokannasta, kutsumalla folder modelissa olevaa delete_folder metodia
    def delete_folder(self, folder_id):
        return Folder.delete_folder(folder_id)