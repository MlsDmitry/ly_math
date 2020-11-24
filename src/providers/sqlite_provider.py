import sqlite3
from src.file_manager import app_path, documents_path


class DBManager:
    def __init__(self):
        self.conn = sqlite3.connect('projectmath.db')
        self.cursor = self.conn.cursor()

    def init_tables(self):
        self.cursor.execute(
            f"CREATE table if not exists preferences ( \
                default_path TEXT default '{documents_path()}' \
                \
                )")
        self.cursor.execute(
            f"CREATE table if not exists history ( \
                id INTEGER PRIMARY KEY, \
                snapshot_name TEXT NOT NULL UNIQUE, \
                operations TEXT NOT NULL, \
                question_count TEXT NOT NULL, \
                seperate_by_num INTEGER NOT NULL, \
                min_num INTEGER NOT NULL, \
                max_num INTEGER NOT NULL \
                )")

    def save(self):
        self.conn.commit()

    def close(self):
        self.conn.close()


class PreferencesModel:
    def __init__(self):
        conn = sqlite3.connect('projectmath.db')
        self.cursor = conn

    def write_default_path(self):
        self.cursor.execute('')

class HistoryModel:
    def __init__(self):
        conn = sqlite3.connect('projectmath.db')
        self.cursor = conn

    def get_snapshot_names(self):
        names = self.cursor.execute('SELECT snapshot_name from history')
        return names.fetchone()
    
    def add_snaptshot(self, params):
        self.cursor.execute(f"INSERT into history \
            (snapshot_name, operations, question_count, seperate_by_num, min_num, max_num)\
            values (?,?,?,?,?,?)", 
            params)
    
    


# class Model:
#     def __init__(self):
