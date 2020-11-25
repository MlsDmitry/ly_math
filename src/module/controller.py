from src.module.view import View
from src.task import ExampleGenerator, Task
from src.module.model import Config
from src.module.model import Model


class Controller:
    def __init__(self):
        self.view = View()
        self.model = Model()

    def show_view(self):
        self.view.show()
        self.view.generate_task_button.clicked.connect(
            self.generate_task_action)

    def generate_task_action(self):

        config = Config()
        config.operations = self.view.operation_checkbox.currentData()
        config.expressions_count = self.view.expressions_count_input.text()
        config.columns = self.view.columns_input.text()
        config.min_number = self.view.min_number_input.text()
        config.max_number = self.view.max_number_input.text()

        is_valid_operation_data = Model.validate_operation(config)
        self.view.show_error_if_needed(
            is_valid_operation_data, self.view.operation_checkbox)

        is_valid_min_max_data = Model.validate_min_max_number(config)
        self.view.show_error_if_needed(
            is_valid_min_max_data, self.view.min_number_input)
        self.view.show_error_if_needed(
            is_valid_min_max_data, self.view.max_number_input)
        is_valid_expressions_count = Model.validate_expressions_count(config)
        self.view.show_error_if_needed(
            is_valid_expressions_count, self.view.expressions_count_input
        )
        is_valid_columns_num = Model.validate_columns(config)
        self.view.show_error_if_needed(
            is_valid_columns_num, self.view.columns_input
        )
        if all(
            (
            is_valid_operation_data,
            is_valid_min_max_data,
            is_valid_expressions_count,
            is_valid_columns_num
            )
        ):
            return
