from src.managers.export_manager import ExportManager
from PyQt5.QtWidgets import QDial, QDialog, QInputDialog
from PyQt5.QtCore import QModelIndex
from random import choice
from string import ascii_letters

from .expression_view import View
from .expression_model import Config
from .expression_model import Model

from src.models.task import TaskModel
from src.logger.logger import Log

from src.managers.db_manager import DBManager
from src.providers.history_provider import HistoryProvider
from src.providers.preferences_provider import PreferencesProvider

from src.custom_widgets.error_dialog import ErrorDialog


from random import randint, choices


class Controller:
    def __init__(self):
        self.view = View()
        self.model = Model()
        # create db/tables before working with them
        self.dbm = DBManager()

        self.preferences_provider = PreferencesProvider()
        self.history_provider = HistoryProvider()
        # for _ in range(10):
        #     task = TaskModel(randint(2, 20), randint(3, 8), choices(
        #         ['+', '-', '*', '/'], k=3), (randint(0, 40), randint(40, 80)))
        #     name = ''.join([choice(ascii_letters) for _ in range(10)])
        #     self.history_provider.add_snaptshot(
        #         [name, *task.to_sqlite_format()])

    def show_view(self):
        Log.log('i', 'show_view')
        self.view.show()
        self.view.generate_task_button.clicked.connect(
            self.generate_task_action)

        self.view.generate_task_with_answers_button.clicked.connect(
            lambda: self.generate_task_action(True))

        self.view.table.clicked.connect(self.snapshot_entry_clicked)
        self.view.save_snapshot_button.clicked.connect(self.save_snapshot)
        self.view.delete_snapshot_button.clicked.connect(self.delete_snapshot)
        self.update_snapshot_table()

    def validate_task_config(self):
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
            return config
        else:
            return False

    def generate_task_action(self, with_answers=False):
        config = self.validate_task_config()
        Log.log('i', 'with answers: ', with_answers)
        if config:
            task = TaskModel(int(config.expressions_count), int(config.columns),
                        config.operations, (int(config.min_number), int(config.max_number)))
            em = ExportManager(task)
            em.save('Math 1.docx', with_answers)

    def update_snapshot_table(self):
        Log.log('i', 'Snapshots: ', self.history_provider.get_snapshot_names())
        self.view.clear_snapshot_table()
        for name in self.history_provider.get_snapshot_names():
            self.view.add_snapshot_entry(name)

    # @pyqtSlot(QModelIndex)
    def snapshot_entry_clicked(self, index: QModelIndex):
        config = Config()
        Log.log('i', 'Clicked snaphost entry')
        snapshot = self.history_provider.get_snapshot(index.data())
        Log.log('i', 'Snapshot name: ', index.data())
        if not snapshot:
            return
        config.operations = snapshot[0]
        config.expressions_count = snapshot[1]
        config.columns = snapshot[2]
        config.min_number = snapshot[3]
        config.max_number = snapshot[4]
        self.view.load_snapshot(config)

    def save_snapshot(self):
        config = self.validate_task_config()
        if not config:
            return

        name, is_pressed = QInputDialog.getText(
            self.view, "Save Snapshot", "Enter name")
        if is_pressed:
            if self.history_provider.get_snapshot(name):
                dialog = ErrorDialog(self.view)
                dialog.exec_()
                return
            task = TaskModel(int(config.expressions_count), int(config.columns),
                        config.operations, (int(config.min_number), int(config.max_number)))
            self.history_provider.add_snaptshot(
                [name, *task.to_sqlite_format()])
            self.view.add_snapshot_entry(name)
            self.dbm.save()
        else:
            return

    def delete_snapshot(self):
        name, is_pressed = QInputDialog.getText(
            self.view, "Delete Snapshot", "Enter name")
        if is_pressed:
            Log.log('d', self.history_provider.get_snapshot(name))
            if self.history_provider.get_snapshot(name):
                self.history_provider.delete_snapshot(name)
                self.update_snapshot_table()
                self.dbm.save()
            else:
                dialog = ErrorDialog(self.view)
                dialog.exec_()
        else:
            return
