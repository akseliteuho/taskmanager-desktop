import json
import os
from .database import Database

# Periytetään Database luokka JSONDatabase luokasta
class JSONDatabase(Database):
    def __init__(self, json_file="tasks.json"):
        self.json_file = json_file
        self.data = self.load_data()

    # Haetaan kaikki tehtävät tietokannasta ja palautetaan ne listana
    def load_data(self):
        if os.path.exists(self.json_file):
            with open(self.json_file, "r") as f:
                return json.load(f)
        else:
            return {"folders": [], "tasks": []}

    # Tallennetaan tietokanta JSON tiedostoon
    def save_data(self):
        with open(self.json_file, "w") as f:
            json.dump(self.data, f, indent=4)

    # Haetaan kaikki tehtävät tietokannasta ja palautetaan ne listana
    def get_tasks(self):
        return self.data["tasks"]

    # Lisätään tehtävä tietokantaan
    def create_task(self, title, description, due_date, folder_id):
        task_id = len(self.data["tasks"]) + 1
        new_task = {
            "id": task_id, 
            "folder_id": folder_id, 
            "title": title, 
            "description": description, 
            "due_date": due_date
        }
        self.data["tasks"].append(new_task)
        self.save_data()

    # Haetaan tehtävät kansion ID:n perusteella
    def get_tasks_by_folder(self, folder_id):
        return [task for task in self.data["tasks"] if task["folder_id"] == folder_id]

    # Poistetaan tehtävä tietokannasta tehtävän ID:n perusteella
    def delete_task(self, task_id):
        self.data["tasks"] = [task for task in self.data["tasks"] if task["id"] != task_id]
        self.save_data()

    # Haetaan kaikki kansiot tietokannasta ja palautetaan ne listana
    def get_folders(self):
        return self.data["folders"]

    # Lisätään kansio tietokantaan
    def create_folder(self, name):
        folder_id = len(self.data["folders"]) + 1
        new_folder = {"id": folder_id, "name": name}
        self.data["folders"].append(new_folder)
        self.save_data()

    # Haetaan kansio kansion ID:n perusteella
    def get_folder_by_id(self, folder_id):
        return next((folder for folder in self.data["folders"] if folder["id"] == folder_id), None)

    # Poistetaan kansio tietokannasta kansion ID:n perusteella
    def delete_folder(self, folder_id):
        self.data["folders"] = [folder for folder in self.data["folders"] if folder["id"] != folder_id]
        self.save_data()