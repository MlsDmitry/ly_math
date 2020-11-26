import os
import platform
import subprocess
from src.logger.logger import Log
from PyQt5.QtWidgets import QFileDialog, QDialog


def open_file(path):
    return QFileDialog.getSaveFileName(None, 'Save File', path)
    
def app_path():
    return os.path.dirname(os.path.abspath(__file__))

def documents_path():
    home = os.path.expanduser("~")
    documents_path = os.path.join(home, 'Documents')
    Log.log('d', 'doc path: ', documents_path)
    return documents_path