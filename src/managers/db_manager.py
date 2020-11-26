import sqlite3
from src.managers.file_manager import documents_path

class DBManager:
    def __init__(self):
        self.conn = sqlite3.connect('projectmath.db')
        self.cursor = self.conn.cursor()

    def init_tables(self):
        self.cursor.execute(
            f"CREATE table if not exists preferences ( \
                default_path TEXT DEFAULT '{documents_path()}' \
                )")
        self.cursor.execute(
            f"CREATE table if not exists history ( \
                id INTEGER PRIMARY KEY, \
                snapshot_name TEXT NOT NULL UNIQUE, \
                operations TEXT NOT NULL, \
                expressions_count INTEGER NOT NULL, \
                columns_num INTEGER NOT NULL, \
                min_num INTEGER NOT NULL, \
                max_num INTEGER NOT NULL \
                )")

    def save(self):
        self.conn.commit()

    def close(self):
        self.conn.close()