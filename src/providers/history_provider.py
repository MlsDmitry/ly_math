import sqlite3
from src.managers.file_manager import app_path, documents_path
from src.logger.logger import Log


class HistoryProvider:
    def __init__(self):
        self.conn = sqlite3.connect('projectmath.db')
        self.cursor = self.conn.cursor()

    def get_snapshot_names(self):
        names = self.cursor.execute('SELECT snapshot_name from history')
        return [t[0] for t in names.fetchall()]
    
    def add_snaptshot(self, params):
        Log.log('d', f'add_snapshot params: {params}')
        self.cursor.execute(f"INSERT into history \
            (snapshot_name, operations, expressions_count, columns_num, min_num, max_num)\
            values (?,?,?,?,?,?)", 
            params)
        self.conn.commit()
    
    def get_snapshot(self, name):
        Log.log('d', f'name: {name}')
        snapshot = self.cursor.execute(f"SELECT \
            operations, expressions_count, columns_num, min_num, max_num \
            from history \
            where snapshot_name = '{name}'")
        return snapshot.fetchone()
    
    def delete_snapshot(self, name):
        Log.log('i', f'delete_snapshot(name): {name}')
        self.cursor.execute(f"DELETE from history where snapshot_name = '{name}'")
        self.conn.commit()
    