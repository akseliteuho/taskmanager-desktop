from models.task import Task

class TaskController:
    def create_task(self, title, description, due_date, folder_id):
        task = Task(title, description, due_date, folder_id)
        task.save()

    def get_tasks(self):
        return Task.get_all_tasks()
