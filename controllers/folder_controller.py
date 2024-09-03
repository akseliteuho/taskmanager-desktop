from models.folder import Folder

class FolderController:
    # Luodaan uusi kansio ja tallennetaan se tietokantaan
    def create_folder(self, name):
        folder = Folder(name)
        folder.save()
    # Haetaan kaikki kansiot tietokannasta, kutsumalla Folder luokan get_all_folders metodia
    def get_folders(self):
        return Folder.get_all_folders()

