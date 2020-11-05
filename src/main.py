from PyQt5.QtWidgets import QWidget, QApplication, QGridLayout, QPushButton, QLineEdit, QLabel
from PyQt5.QtGui import QIntValidator
import sys

from src.custom_widgets import CheckableComboBox
from src.task import ExampleGenerator, Task


class App (QWidget):
    def __init__(self):
        super().__init__()
        self.setUI()

    def setUI(self):
        self.setGeometry(600, 800, 800, 600)
        self.setWindowTitle("Math Question Generator [MQG]")

        self.grid_layout = QGridLayout()
        self.grid_layout.setSpacing(0)

        type_select_box = CheckableComboBox()
        type_select_box.addItems(["+", "-", "*", "/"])
        self.grid_layout.addWidget(type_select_box, 0, 0)

        # Add Label "How many cols?"
        per_row_label = QLabel("How many cols?")
        self.grid_layout.addWidget(per_row_label, 1, 0)
        per_row_num_input = QLineEdit()
        # Restrict input
        validator = QIntValidator()
        per_row_num_input.setValidator(validator)
        self.grid_layout.addWidget(per_row_num_input, 2, 0)

        # Add Label "How many rows?"
        per_col_label = QLabel("How many rows?")
        self.grid_layout.addWidget(per_col_label, 1, 1)
        per_col_num_input = QLineEdit()
        # Restrict input
        validator = QIntValidator()
        per_col_num_input.setValidator(QIntValidator())
        self.grid_layout.addWidget(per_col_num_input, 2, 1)

        # Add Label "From num: "
        per_col_label = QLabel("From num: ")
        self.grid_layout.addWidget(per_col_label, 3, 0)
        per_col_num_input = QLineEdit()
        # Restrict input
        validator = QIntValidator()
        per_col_num_input.setValidator(QIntValidator())
        self.grid_layout.addWidget(per_col_num_input, 4, 0)

        # Add Label "To num: "
        per_col_label = QLabel("To num: ")
        self.grid_layout.addWidget(per_col_label, 3, 1)
        per_col_num_input = QLineEdit()
        # Restrict input
        validator = QIntValidator()
        per_col_num_input.setValidator(QIntValidator())
        self.grid_layout.addWidget(per_col_num_input, 4, 1)

        generate_task_button = QPushButton('Generate')
        generate_task_button.clicked.connect(self.generate_task_action)
        self.grid_layout.addWidget(generate_task_button)

    
        self.setLayout(self.grid_layout)

    def generate_task_action(self):
        operations = self.grid_layout.itemAtPosition(0, 0).widget().currentData()
        if len(operations) == 0:
            warn = QLabel("Please specify at least one operation")
            self.grid_layout.addWidget(warn)
            return
        print(operations)
        size_of_table = int(self.grid_layout.itemAtPosition(2, 0).widget().text())
        size_of_sub_table = int(self.grid_layout.itemAtPosition(2, 1).widget().text())
        from_num = int(self.grid_layout.itemAtPosition(4, 0).widget().text())
        to_num = int(self.grid_layout.itemAtPosition(4, 1).widget().text())

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
