from PyQt5.QtWidgets import QMainWindow, QWidget, QApplication, QGridLayout, QPushButton, QLineEdit, QLabel, QVBoxLayout, QCalendarWidget, QHBoxLayout
from PyQt5.QtGui import QIntValidator
import sys

from src.custom_widgets import CheckableComboBox, StackedWidget
from src.task import ExampleGenerator, Task
from src.utils import ValidateTask
from src.logger.logger import Log


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

        select_box_description = QLabel('Choose operations')
        select_box_description.setMaximumSize(select_box_description.sizeHint())
        self.lstack_settings.addWidget(select_box_description)

        type_select_box = CheckableComboBox()
        type_select_box.addItems(["+", "-", "*", "/"])
        self.lstack_settings.addWidget(type_select_box)

        self.add_form_input("Questions count")
        self.add_form_input("Seperate by")
        self.add_form_input("From num")
        self.add_form_input("To num")


        # define layout for Generate & export[word, pdf] Generate & do now
        generate_task_button = QPushButton('Generate')
        generate_task_button.clicked.connect(self.generate_task_action)
        self.lstack_settings.addWidget(generate_task_button)

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
        validator = QIntValidator()
        form_input.setValidator(QIntValidator())
        self.lstack_settings.addWidget(form_input)

    def display_error(self, error, row_input_pos):
        self.lstack_settings.itemAtPosition()


    def generate_task_action(self):

        validator = ValidateTask(self.lstack_settings)
        validator.validate()

        if validator.warnings:
            self.lstack_settings = validator.lstack_settings
            return

            # for row_num, error_lmessage in validator.warnings.items():
            #     widget = self.lstack_settings.itemAt(row_num).widget()
            #     Log.log('d', id(widget))


        operations = validator.data[0]
        # if len(operations) == 0:
        #     warn = QLabel("Please specify at least one operation")
        #     self.lstack_settings.addWidget(warn)
        #     return
        question_count = validator.data[1]
        seperate_by_num = validator.data[2]
        from_num = validator.data[3]
        to_num = validator.data[4]

        self.task = Task(question_count, seperate_by_num)
        self.ex_generator = ExampleGenerator(self.task, operations, (from_num, to_num))
        self.ex_generator.generate_final()


        
        # from pprint import pprint
        # pprint(self.task.return_field_seperated())



# if __name__ == '__main__':
#     preferences = QApplication()
#     app = App()
#     app.show()
#     sys.exit(app.exec_())
