from src.custom_widgets import CheckableComboBox, StackedWidget
from PyQt5.QtWidgets import QMainWindow, QWidget, QApplication, QGridLayout, QPushButton, QLineEdit, QLabel, QVBoxLayout, QCalendarWidget, QHBoxLayout

class View(QMainWindow):

    def __init__(self):
        super().__init__()
        self.lstack_settings = QVBoxLayout()
        self.lgrid_main = QGridLayout()
        self.lpage = StackedWidget()
        self.setUI()

    def setUI(self):
        self.setGeometry(600, 800, 800, 600)
        self.setWindowTitle("Math Question Generator [MQG]")
        # l stand for layout -> stack settings layout

        select_box_description = QLabel('Choose operations')
        select_box_description.setMaximumSize(select_box_description.sizeHint())
        self.lstack_settings.addWidget(select_box_description)

        type_select_box = CheckableComboBox()
        type_select_box.addItems(["+", "-", "*", "/"])
        self.lstack_settings.addWidget(type_select_box)

        self.qustion_count_input = self.add_form_input("Questions count")
        self.seperate_input = self.add_form_input("Seperate by")
        self.min_number_input = self.add_form_input("Min number")
        self.max_number_input = self.add_form_input("Max number")

        # define layout for Generate & export[word, pdf] Generate & do now
        self.generate_task_button = QPushButton('Generate')
        self.lstack_settings.addWidget(self.generate_task_button)

        self.lgrid_main.addLayout(self.lstack_settings, 0, 0, 1, 2)
        # TODO seperate App(QMainWindow) and QWidget classes
        window = QWidget()
        window.setLayout(self.lgrid_main)
        self.setCentralWidget(window)

    def add_form_input(self, label_text):
        widget_description = QLabel(label_text)
        widget_description.setMaximumSize(widget_description.sizeHint())

        self.lstack_settings.addWidget(widget_description)

        form_input = QLineEdit()
        # Restrict input
        # validator = QIntValidator()
        # form_input.setValidator(QIntValidator())
        self.lstack_settings.addWidget(form_input)
        return form_input
