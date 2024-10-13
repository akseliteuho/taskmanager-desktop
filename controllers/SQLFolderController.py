from models.SQLFolder import SQLFolder

class SQLFolderController:
    # Luodaan uusi kansio ja tallennetaan se tietokantaan
    def create_folder(self, name):
        folder = SQLFolder(name)
        folder.save()
    # Haetaan kaikki kansiot tietokannasta, kutsumalla Folder luokan get_all_folders metodia
    def get_folders(self):
        return SQLFolder.get_all_folders()

    # Haetaan kansio kansion ID:n perusteella, kutsumalla Folder luokan get_folder_by_id metodia
    def get_folder_by_id(self, folder_id):
        return SQLFolder.get_folder_by_id(folder_id)

    # Poistetaan kansio kansio tietokannasta, kutsumalla folder modelissa olevaa delete_folder metodia
    def delete_folder(self, folder_id):
        return SQLFolder.delete_folder(folder_id)