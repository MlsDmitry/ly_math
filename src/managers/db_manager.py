import sqlite3
from src.logger.logger import Log
from src.managers.file_manager import documents_path
from src.providers.history_provider import HistoryProvider

class DBManager:
    def __init__(self):
        self.conn = sqlite3.connect('projectmath.db')
        self.cursor = self.conn.cursor()
        self._init_tables()

    def _init_tables(self):
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
        self.conn.commit()

    def save(self):
        # self.conn.commit()
        pass

    def close(self):
        hp = HistoryProvider()
        Log.log('d', hp.get_snapshot_names())
        self.conn.close()