from .database import Database

class Folder:
    def __init__(self, name):
        self.db = Database()
        self.name = name

    def save(self):
        with self.db.conn:
            self.db.conn.execute("INSERT INTO folders (name) VALUES (?)", (self.name,))

    @staticmethod
    def get_all_folders():
        db = Database()
        cursor = db.conn.execute("SELECT * FROM folders")
        return cursor.fetchall()
