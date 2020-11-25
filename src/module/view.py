from src.custom_widgets import CheckableComboBox, StackedWidget
from PyQt5.QtWidgets import QMainWindow, QWidget, QApplication, QGridLayout, QPushButton, QLineEdit, QLabel, \
    QVBoxLayout, QCalendarWidget, QHBoxLayout
from PyQt5.QtGui import QIntValidator


class View(QMainWindow):

    def __init__(self):
        super().__init__()
        self.lstack_settings = QVBoxLayout()
        self.lgrid_main = QGridLayout()
        self.lpage = StackedWidget()
        self.setUI()

    def setUI(self):
        self.setGeometry(400, 800, 800, 400)
        self.setWindowTitle("Math Question Generator [MQG]")
        # l stand for layout -> stack settings layout

        select_box_description = QLabel('Choose operations')
        select_box_description.setMaximumSize(select_box_description.sizeHint())
        self.lstack_settings.addWidget(select_box_description)

        self.operation_checkbox = CheckableComboBox()
        self.operation_checkbox.addItems(["+", "-", "*", "/"])
        self.lstack_settings.addWidget(self.operation_checkbox)

        self.expressions_count_input = self.add_form_input("Questions count")
        self.columns_input = self.add_form_input("Columns")
        self.min_number_input = self.add_form_input("Min number")
        self.max_number_input = self.add_form_input("Max number")

        # define layout for Generate & export[word, pdf] Generate & do now
        self.generate_task_button = QPushButton('Generate')
        self.lstack_settings.addWidget(self.generate_task_button)

        self.lgrid_main.addLayout(self.lstack_settings, 0, 0)
        # TODO separate App(QMainWindow) and QWidget classes
        window = QWidget()
        window.setLayout(self.lgrid_main)
        self.setCentralWidget(window)

    def add_form_input(self, label_text):
        widget_description = QLabel(label_text)
        widget_description.setMaximumSize(widget_description.sizeHint())

        self.lstack_settings.addWidget(widget_description)

        form_input = QLineEdit()
        # Restrict input
        validator = QIntValidator()
        form_input.setValidator(QIntValidator())
        self.lstack_settings.addWidget(form_input)
        return form_input

    def show_error_if_needed(self, is_valid, widget):
        if is_valid:
            widget.setStyleSheet("border: 1px solid green")
        else:
            widget.setStyleSheet("border: 1px solid red;")
