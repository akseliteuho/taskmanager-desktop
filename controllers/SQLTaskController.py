from models.SQLTask import SQLTask
from datetime import datetime

class SQLTaskController:
    # Luodaan uusi tehtävä ja tallennetaan se tietokantaan
    def create_task(self, title, description, due_date, folder_id):
        task = SQLTask(title, description, due_date, folder_id)
        task.save()

    # Haetaan kaikki tehtävät tietokannasta, kutsumalla Task luokan get_all_tasks metodia
    def get_tasks(self):
        return SQLTask.get_all_tasks()
    
    # Haetaan tehtävät kansion ID:n perusteella, kutsumalla Task luokan get_tasks_by_folder_id metodia
    def get_tasks_by_folder_id(self, folder_id):
        return SQLTask.get_tasks_by_folder_id(folder_id)

    # Poistetaan tehtävä tietokannasta, kutsumalla Task luokan delete_task metodia
    def delete_task(self, task_id):
        return SQLTask.delete_task(task_id)
    
    # Haetaan erääntyvät tehtävät
    def get_tasks_due_today(self):
        tasks = SQLTask.get_all_tasks() # Haetaan kaikki tehtävät
        today = datetime.now().date() # Haetaan tämän päivän päivämäärä
        due_today = [] # Luodaan lista, johon lisätään erääntyvät tehtävät

        # Käydään läpi kaikki tehtävät ja tarkistetaan, onko niiden deadline tänään
        for task in tasks:
            due_date = datetime.strptime(task[4], "%Y-%m-%d").date() # Muodonmuutos päivämäärästä string muotoon
            if due_date == today:
                # Lisätään tehtävä listaan, jos sen deadline on tänään
                due_today.append({
                    'title': task[2],
                    'due_date': task[4]
                }) 
        return due_today