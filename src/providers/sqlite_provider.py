import sqlite3
from src.file_manager import app_path, documents_path
from src.logger.logger import Log


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
                expressions_count INTEGER NOT NULL, \
                columns_num INTEGER NOT NULL, \
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
        return [t[0] for t in names.fetchall()]
    
    def add_snaptshot(self, params):
        Log.log('d', f'add_snapshot params: {params}')
        self.cursor.execute(f"INSERT into history \
            (snapshot_name, operations, expressions_count, columns_num, min_num, max_num)\
            values (?,?,?,?,?,?)", 
            params)
    
    def get_snapshot(self, name):
        Log.log('d', f'name: {name}')
        snapshot = self.cursor.execute(f"SELECT \
            operations, expressions_count, columns_num, min_num, max_num \
            from history \
            where snapshot_name = '{name}'")
        return snapshot.fetchone()
    

    
    


# class Model:
#     def __init__(self):
