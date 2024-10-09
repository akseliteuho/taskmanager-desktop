# luokka Database määrittelee rajapinnan tietokannan käyttöön käyttäessä valittua tietokantaa
class Database:

    # Määritellään rajapinnan metodit, joita käytettävän tietokanta luokan tulee toteuttaa
    # NotImplementedError poikkeus heitetään, jos metodia ei ole toteuteta perivässä luokassa,
    # jolloin varmistetaan, että perivä luokka toteuttaa rajapinnan metodit oikein

    # Taskeihin liittyvät metodit
    def get_tasks(self):
        raise NotImplementedError("This method must be overridden by subclasses")

    def create_task(self, title, description, due_date, folder_id):
        raise NotImplementedError("This method must be overridden by subclasses")

    def get_tasks_by_folder(self, folder_id):
        raise NotImplementedError("This method must be overridden by subclasses")

    def delete_task(self, task_id):
        raise NotImplementedError("This method must be overridden by subclasses")


    # Folderiin liittyvät metodit
    def get_folders(self):
        raise NotImplementedError("This method must be overridden by subclasses")

    def create_folder(self, name):
        raise NotImplementedError("This method must be overridden by subclasses")

    def get_folder_by_id(self, folder_id):
        raise NotImplementedError("This method must be overridden by subclasses")

    def delete_folder(self, folder_id):
        raise NotImplementedError("This method must be overridden by subclasses")