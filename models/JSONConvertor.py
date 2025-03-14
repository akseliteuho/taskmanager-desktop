import json
import csv

def create_csv_from_json(json_db_path, csv_file_path_tasks, csv_file_path_folders):
    print(json_db_path)
    # Avataan JSON tietokanta
    with open (json_db_path) as json_file:
        JSON_data = json.load(json_file)

    # Etsitään JSON tiedostosta folders ja tasks data
    folders_data = JSON_data.get("folders", [])
    tasks_data = JSON_data.get("tasks", [])

    # Write folders data to CSV
    if folders_data:
        with open(csv_file_path_folders, 'w', newline='') as data_file:
            csv_writer = csv.writer(data_file)
            header = folders_data[0].keys()
            csv_writer.writerow(header)
            for data in folders_data:
                csv_writer.writerow(data.values())

    # Write tasks data to CSV
    if tasks_data:
        with open(csv_file_path_tasks, 'w', newline='') as data_file:
            csv_writer = csv.writer(data_file)
            header = tasks_data[0].keys()
            csv_writer.writerow(header)
            for data in tasks_data:
                csv_writer.writerow(data.values())

create_csv_from_json('json.db', 'folders_data_file.csv', 'tasks_data_file.csv')