from models.JSONTask import JSONTask
from datetime import datetime


class JSONTaskController:
    # Luodaan uusi tehtävä ja tallennetaan se tietokantaan
    def create_task(self, title, description, due_date, folder_id):
        task = JSONTask(title, description, due_date, folder_id)
        task.save()


    # Haetaan kaikki tehtävät tietokannasta, kutsumalla Task luokan get_all_tasks metodia
    def get_tasks(self):
        return JSONTask.get_all_tasks()
    
    
    # Haetaan tehtävät kansion ID:n perusteella, kutsumalla Task luokan get_tasks_by_folder_id metodia
    def get_tasks_by_folder_id(self, folder_id):
        return JSONTask.get_tasks_by_folder_id(folder_id)
    

    # Poistetaan tehtävä tietokannasta, kutsumalla Task luokan delete_task metodia
    def delete_task(self, task_id):
        return JSONTask.delete_task(task_id)
    
    
    # Haetaan erääntyvät tehtävät
    def get_tasks_due_today(self):
        tasks = JSONTask.get_all_tasks() # Haetaan kaikki tehtävät
        today = datetime.now().date() # Haetaan tämän päivän päivämäärä
        due_today = [] # Luodaan lista, johon lisätään erääntyvät tehtävät

        for task in tasks:
            due_date = datetime.strptime(task["due_date"], "%Y-%m-%d").date() # Muodonmuutos päivämäärästä string muotoon
            if due_date == today: # Tarkistetaan, onko tehtävän deadline tänään
                due_today.append(task) # Lisätään tehtävä listaan, jos sen deadline on tänään
        return due_today # Palautetaan erääntyvät tehtävät listana
    
    
    # Haetaan tehtävät kansion ID:n perusteella (taskien näyttäminen foldereissa)
    def get_tasks_by_fodler_id(self, folder_id):
        tasks = JSONTask.get_tasks_by_folder_id(folder_id)
        tasks_in_folder = []

        # Käydään läpi kaikki kansion tehtävät ja lisätään ne listaan
        for task in tasks:
            # Lisätään tehtävä listaan
            tasks_in_folder.append({
                'title': task["title"], # Tehtävän nimi
                'description': task["description"], # Tehtävän kuvaus
                'due_date': task["due_date"] # Tehtävän duedate
            })
        return tasks_in_folder # Palautetaan tehtävät listana
    
    
    # Haetaan tehtävä tehtävän otsikon perusteella, poistoa varten
    def delete_task_by_title(self, title):
        tasks = JSONTask.get_all_tasks() # Haetaan kaikki tehtävät

        # Käydään läpi kaikki tehtävät ja etsitään poistettava tehtävä
        for task in tasks:
            if task["title"] == title: # Tarkistetaan, vastaako tehtävän otsikko annettua nimeä
                return {'id': task["id"], 'title': task["title"]} # Palautetaan poistettava tehtävä
            