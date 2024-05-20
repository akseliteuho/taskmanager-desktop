from models.folder import Folder

class FolderController:
    def create_folder(self, name):
        folder = Folder(name)
        folder.save()

    def get_folders(self):
        return Folder.get_all_folders()
