from PyQt5.QtWidgets import QMainWindow, QWidget, QApplication, QGridLayout, QPushButton, QLineEdit, QLabel, QVBoxLayout, QCalendarWidget
from PyQt5.QtGui import QIntValidator
import sys

from src.custom_widgets import CheckableComboBox
from src.task import ExampleGenerator, Task
from src.custom_widgets import StackedWidget


class App (QMainWindow):
    def __init__(self):
        super().__init__()
        self.setUI()

    def setUI(self):
        self.setGeometry(600, 800, 800, 600)
        self.setWindowTitle("Math Question Generator [MQG]")
        # l stand for layout -> stack settings layout
        self.lstack_settings = QVBoxLayout()
        self.lgrid_main = QGridLayout()
        self.lpage = StackedWidget()

        type_select_box = CheckableComboBox()
        type_select_box.addItems(["+", "-", "*", "/"])
        self.lstack_settings.addWidget(type_select_box)

        # Add Label "How many cols?"
        per_row_label = QLabel("How many cols?")
        self.lstack_settings.addWidget(per_row_label)
        per_row_num_input = QLineEdit()
        # Restrict input
        validator = QIntValidator()
        per_row_num_input.setValidator(validator)
        self.lstack_settings.addWidget(per_row_num_input)

        # Add Label "How many rows?"
        per_col_label = QLabel("How many rows?")
        self.lstack_settings.addWidget(per_col_label)
        per_col_num_input = QLineEdit()
        # Restrict input
        validator = QIntValidator()
        per_col_num_input.setValidator(QIntValidator())
        self.lstack_settings.addWidget(per_col_num_input)

        # Add Label "From num: "
        per_col_label = QLabel("From num: ")
        self.lstack_settings.addWidget(per_col_label)
        per_col_num_input = QLineEdit()
        # Restrict input
        validator = QIntValidator()
        per_col_num_input.setValidator(QIntValidator())
        self.lstack_settings.addWidget(per_col_num_input)

        # Add Label "To num: "
        per_col_label = QLabel("To num: ")
        self.lstack_settings.addWidget(per_col_label)
        per_col_num_input = QLineEdit()
        # Restrict input
        validator = QIntValidator()
        per_col_num_input.setValidator(QIntValidator())
        self.lstack_settings.addWidget(per_col_num_input)

        generate_task_button = QPushButton('Generate')
        generate_task_button.clicked.connect(self.generate_task_action)
        self.lstack_settings.addWidget(generate_task_button)

        page1 = QWidget()
        page1.setLayout(self.lstack_settings)
        page2 = QCalendarWidget()

        self.lpage.addWidget(page1)
        self.lpage.addWidget(page2)
        self.lgrid_main.addWidget(self.lpage, 0, 0, 1, 2) # 2 -> fill 2 columns
        back_button = QPushButton("<")
        back_button.clicked.connect(lambda: self.lpage.setCurrentIndex(0))
        self.lgrid_main.addWidget(back_button, 1, 0, 1, 1) # 1 -> fill 1 column
        forward_button = QPushButton(">")
        forward_button.clicked.connect(lambda: self.lpage.setCurrentIndex(1))
        self.lgrid_main.addWidget(forward_button, 1, 1, 1, 1)

        # self.lgrid_main.addLayout(self.lstack_settings, 0, 0)
        # TODO seperate App(QMainWindow) and QWidget classes
        window = QWidget()
        window.setLayout(self.lgrid_main)
        self.setCentralWidget(window)

    def generate_task_action(self):
        # TODO add validation input for negative numbers
        operations = self.lstack_settings.itemAt(0).widget().currentData()
        if len(operations) == 0:
            warn = QLabel("Please specify at least one operation")
            self.lstack_settings.addWidget(warn)
            return
        size_of_table = int(self.lstack_settings.itemAt(2).widget().text())
        size_of_sub_table = int(self.lstack_settings.itemAt(2).widget().text())
        from_num = int(self.lstack_settings.itemAt(4).widget().text())
        to_num = int(self.lstack_settings.itemAt(4).widget().text())

        self.task = Task(size_of_table, size_of_sub_table)
        ex_generator = ExampleGenerator(self.task, operations, (from_num, to_num))
        ex_generator.generate_final()
        from pprint import pprint
        pprint(self.task.return_field_seperated())



# if __name__ == '__main__':
#     preferences = QApplication()
#     app = App()
#     app.show()
#     sys.exit(app.exec_())
