from src.modules.expression.expression_model import Config
from src.custom_widgets import CheckableComboBox, StackedWidget
from PyQt5.QtWidgets import QHBoxLayout, QHeaderView, QMainWindow, QTableWidget, QTableWidgetItem, QWidget, QGridLayout, QPushButton, QLineEdit, QLabel, \
    QVBoxLayout, QAbstractItemView
from PyQt5.QtGui import QIntValidator
from PyQt5.QtCore import Qt

from src.logger.logger import Log


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
        select_box_description.setMaximumSize(
            select_box_description.sizeHint())
        self.lstack_settings.addWidget(select_box_description)

        self.operation_checkbox = CheckableComboBox()
        self.operation_checkbox.addItems(["+", "-", "*", "/"])
        self.lstack_settings.addWidget(self.operation_checkbox)

        self.expressions_count_input = self.add_form_input("Questions count")
        self.columns_input = self.add_form_input("Columns")
        self.min_number_input = self.add_form_input("Min number")
        self.max_number_input = self.add_form_input("Max number")

        # sidebar 
        self.create_sidebar()

        layout = QHBoxLayout()
        self.save_snapshot_button = QPushButton("save")
        self.delete_snapshot_button = QPushButton("delete")

        layout.addWidget(self.save_snapshot_button)
        layout.addWidget(self.delete_snapshot_button)
        self.lgrid_main.addLayout(layout, 1, 1, 1, 4)

        # define layout for Generate & export[word, pdf] Generate & do now
        self.generate_task_button = QPushButton('Generate')
        self.generate_task_with_answers_button = QPushButton('Generate with answers')

        self.lgrid_main.addLayout(self.lstack_settings, 0, 0, 1, 1)
        layout = QHBoxLayout()
        layout.addWidget(self.generate_task_button)
        layout.addWidget(self.generate_task_with_answers_button)
        self.lgrid_main.addLayout(layout, 1, 0)

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
            widget.setStyleSheet("border: 1px solid green;")
        else:
            widget.setStyleSheet("border: 1px solid red;")

    def create_sidebar(self):
        self.table = QTableWidget()
        self.table.setColumnCount(1)
        self.table.setRowCount(1)
        self.table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.table.setHorizontalHeaderLabels(['Snapshots'])
        # self.table.horizontalHeader().hide()
        self.table.verticalHeader().hide()

        # self.table.setFixedHeight(400)

        self.lgrid_main.addWidget(self.table, 0, 1, 1, 4)

    def add_snapshot_entry(self, name):
        Log.log('i', 'Param name: ', name)
        snapshot_item = QTableWidgetItem(name)

        row = self.table.rowCount() - 1
        self.table.setItem(row, 0, snapshot_item)
        self.table.setRowCount(self.table.rowCount() + 1)

    def clear_snapshot_table(self):
        for _ in range(self.table.rowCount()):
            self.table.removeRow(0)

    def load_snapshot(self, config: Config):
        Log.log('i', 'Config: ', config.__dict__)
        self.operation_checkbox.set_checked(config.operations)
        self.expressions_count_input.setText(str(config.expressions_count))
        self.columns_input.setText(str(config.columns))
        self.min_number_input.setText(str(config.min_number))
        self.max_number_input.setText(str(config.max_number))