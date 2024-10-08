from models.task import Task

class TaskController:
    # Luodaan uusi tehtävä ja tallennetaan se tietokantaan
    def create_task(self, title, description, due_date, folder_id):
        task = Task(title, description, due_date, folder_id)
        task.save()

    # Haetaan kaikki tehtävät tietokannasta, kutsumalla Task luokan get_all_tasks metodia
    def get_tasks(self):
        return Task.get_all_tasks()
    
    # Haetaan tehtävät kansion ID:n perusteella, kutsumalla Task luokan get_tasks_by_folder_id metodia
    def get_tasks_by_folder_id(self, folder_id):
        return Task.get_tasks_by_folder_id(folder_id)

    # Poistetaan tehtävä tietokannasta, kutsumalla Task luokan delete_task metodia
    def delete_task(self, task_id):
        return Task.delete_task(task_id)