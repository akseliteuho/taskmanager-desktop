import tkinter as tk
from tkinter import messagebox
from tkcalendar import DateEntry
from controllers.task_controller import TaskController
from controllers.folder_controller import FolderController

class MainView:
    def __init__(self, root):
        self.root = root
        self.root.title("Task Manager")

        self.task_controller = TaskController()
        self.folder_controller = FolderController()

        self.create_widgets()

    def create_widgets(self):
        self.title_entry = tk.Entry(self.root)
        self.title_entry.pack()

        self.description_entry = tk.Entry(self.root)
        self.description_entry.pack()

        self.due_date_entry = DateEntry(self.root)
        self.due_date_entry.pack()

        self.create_task_button = tk.Button(self.root, text="Create Task", command=self.create_task)
        self.create_task_button.pack()

        self.create_folder_button = tk.Button(self.root, text="Create Folder", command=self.create_folder)
        self.create_folder_button.pack()

        self.tasks_listbox = tk.Listbox(self.root)
        self.tasks_listbox.pack()

        self.folders_listbox = tk.Listbox(self.root)
        self.folders_listbox.pack()

        self.refresh_tasks()
        self.refresh_folders()

    def create_task(self):
        title = self.title_entry.get()
        description = self.description_entry.get()
        due_date = self.due_date_entry.get_date()
        folder_id = None  # Update this to select a folder
        self.task_controller.create_task(title, description, due_date, folder_id)
        self.refresh_tasks()

    def create_folder(self):
        name = "New Folder"
        self.folder_controller.create_folder(name)
        self.refresh_folders()

    def refresh_tasks(self):
        self.tasks_listbox.delete(0, tk.END)
        tasks = self.task_controller.get_tasks()
        for task in tasks:
            self.tasks_listbox.insert(tk.END, task[1])

    def refresh_folders(self):
        self.folders_listbox.delete(0, tk.END)
        folders = self.folder_controller.get_folders()
        for folder in folders:
            self.folders_listbox.insert(tk.END, folder[1])
