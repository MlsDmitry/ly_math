import os
import subprocess
from src.logger.logger import Log

def open_file(path):
    if os.platform.system() == "Windows":
        os.startfile(path)
    elif os.platform.system() == "Darwin":
        subprocess.Popen(["open", path])
    elif os.platform.system() == 'Linux':
        subprocess.Popen(["xdg-open", path])
    
def app_path():
    return os.path.dirname(os.path.abspath(__file__))

def documents_path():
    home = os.path.expanduser("~")
    documents_path = os.path.join(home, 'Documents')
    Log.log('d', 'doc path: ', documents_path)
    return documents_path