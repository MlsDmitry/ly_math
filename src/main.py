from PyQt5.QtWidgets import QMainWindow, QWidget, QApplication, QGridLayout, QPushButton, QLineEdit, QLabel, QVBoxLayout, QCalendarWidget, QHBoxLayout
from PyQt5.QtGui import QIntValidator
import sys

from src.custom_widgets import CheckableComboBox, StackedWidget
from src.logger.logger import Log
from src.module.controller import Controller

class App:
    def __init__(self):
        self.controller = Controller()
        self.controller.show_view()
