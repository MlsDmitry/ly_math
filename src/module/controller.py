from src.module.view import View
from src.utils import ValidateTask
from src.task import ExampleGenerator, Task


class Controller:
    def __init__(self):
        self.view = View()

    def show_view(self):
        self.view.show()
        self.view.generate_task_button.clicked.connect(self.generate_task_action)

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
        separate_by_num = validator.data[2]
        from_num = validator.data[3]
        to_num = validator.data[4]

        self.task = Task(question_count, separate_by_num)
        self.ex_generator = ExampleGenerator(self.task, operations, (from_num, to_num))
        self.ex_generator.generate_final()

    def display_error(self, error, row_input_pos):
        self.lstack_settings.itemAtPosition()
