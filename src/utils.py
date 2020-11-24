from PyQt5.QtWidgets import QLabel, QLineEdit, QVBoxLayout
from src.logger.logger import Log
from src.custom_widgets.custom import CheckableComboBox
from enum import Enum
    
class Warning(Enum):
    OPERATION = 1

class ValidateTask:
    WARNINGS = ['1' , '2', '3', '4', '5']
    def __init__(self, lstack_settings: QVBoxLayout):
        self.lstack_settings = lstack_settings
        self.warnings = {}
        self.data = {}

    
    def get_widget_by_id(self, id):
        return self.lstack_settings.itemAt(id).widget()
    
    def validate(self):
        warnings = {}

        for id in range(1, 10, 2):
            widget = self.get_widget_by_id(id)
            Log.log('d', f'id: {id}', f'widget: {widget}')
            if isinstance(widget, CheckableComboBox):
                data = widget.currentData()
            elif isinstance(widget, QLineEdit):
                data = widget.text()
            else:
                raise TypeError

            Log.log('d', 'data: ', data)
            index = int((id - 1) / 2)
            if len(data) == 0:
                warnings[index] = self.WARNINGS[index]
                widget.setStyleSheet("border: 1px solid red;")
            elif index == 2 and int(self.get_widget_by_id(3).text()) < int(data):
                # Log.log('d', f"data: {data}; widget_data: {int(self.get_widget_by_id(3).text())}; equation: {}")
                warnings[index] = self.WARNINGS[index]
                widget.setStyleSheet("border: 1px solid red;")
            elif index == 4 and int(data) <= int(self.get_widget_by_id(7).text()):
                warnings[index] = self.WARNINGS[index]
                widget.setStyleSheet("border: 1px solid red;")
            else:
                if index in warnings:
                    del warnings[index]
                widget.setStyleSheet("border: 1px solid green")

                if isinstance(widget, CheckableComboBox):
                    data = widget.currentData()
                elif isinstance(widget, QLineEdit):
                    data = int(widget.text())
                else:
                    raise TypeError
                self.data[index] = data

        # data = operations.currentData()
        # Log.log('d', data)
        # if len(data) == 0:
        #     warn = QLabel("Please specify at least one operation")
        #     warnings[0] = warn
        #     operations.setStyleSheet("border: 1px solid red;")
        # question_count = self.get_widget_by_id(3)
        # Log.log('d', question_count.text())
        # if question_count.text() == '':
        #     warn = QLabel("Please specify questions count")
        #     question_count.setStyleSheet("border: 1px solid red;")
        #     warnings[1] = warn 
        # seperate_by_num = self.get_widget_by_id(5)
        # Log.log('d', seperate_by_num.text())
        # if seperate_by_num.text() == '':
        #     warn = QLabel("Please specify rows count in tables")
        #     seperate_by_num.setStyleSheet("border: 1px solid red;")
        #     warnings[2] = warn 
        # from_num = self.get_widget_by_id(7)
        # Log.log('d', from_num.text())
        # if from_num.text() == '':
        #     warn = QLabel("Please specify minimum number")
        #     from_num.setStyleSheet("border: 1px solid red;")
        #     warnings[3] = warn 

        # to_num = self.get_widget_by_id(9)
        # Log.log('d', to_num.text())
        # if to_num.text() == '':
        #     warn = QLabel("Please specify maximum number")
        #     to_num.setStyleSheet("border: 1px solid red;")
        #     warnings[4] = warn 

        self.warnings = warnings
        # self.task = Task(question_count, seperate_by_num)
        # self.ex_generator = ExampleGenerator(self.task, operations, (from_num, to_num))
        # self.ex_generator.generate_final()


