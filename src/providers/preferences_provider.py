import sqlite3

class PreferencesProvider:
    def __init__(self):
        conn = sqlite3.connect('projectmath.db')
        self.cursor = conn

    def write_default_path(self, path):
        self.cursor.execute(f'INSERT into preferences (default_path) values ("{path}")')
    
    def get_path(self):
        path = self.cursor.execute('SELECT * FROM preferences')
        # Log.log('d', path.fetchone())
        return path.fetchone()[0]
    