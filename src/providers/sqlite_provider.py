import sqlite3
from src.file_manager import app_path, documents_path


class DBManager:
    def __init__(self):
        self.conn = sqlite3.connect('projectmath.db')
        self.cursor = self.conn.cursor
        print(documents_path)

    def init_tables(self):
        self.cursor.execute(f"create table if not exists preferences ( default_path TEXT default {documents_path()} previous_path)")


class PreferencesModel:
    def __init__(self):
        conn = sqlite3.connect('projectmath.db')
        self.cursor = conn


    def write_default_path(self):
        self.cursor.execute('')

# class Model:
#     def __init__(self):
