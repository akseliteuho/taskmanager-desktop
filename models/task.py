from .database import Database

class Task:
    def __init__(self, title, description='', due_date=None, folder_id=None):
        self.db = Database()
        self.title = title
        self.description = description
        self.due_date = due_date
        self.folder_id = folder_id

    def save(self):
        with self.db.conn:
            self.db.conn.execute(
                "INSERT INTO tasks (folder_id, title, description, due_date) VALUES (?, ?, ?, ?)",
                (self.folder_id, self.title, self.description, self.due_date)
            )

    @staticmethod
    def get_all_tasks():
        db = Database()
        cursor = db.conn.execute("SELECT * FROM tasks")
        return cursor.fetchall()
