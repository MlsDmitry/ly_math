from PyQt5.QtWidgets import QLabel, QLineEdit, QVBoxLayout
from logging import log, warning
import coloredlogs, logging
from src.custom_widgets.custom import CheckableComboBox


from src.config import LOG_LEVEL

logger = logging.getLogger(__name__)

class Log:

    def __init__(self):
        coloredlogs.install(level=LOG_LEVEL, logger=logger)

    @staticmethod
    def log(*args, **kwargs):
        if not LOG_LEVEL:
            return
        
        log_func = logger
        if args[0] == 'i':
            log_func = log_func.info
        elif args[0] == 'd':
            log_func = log_func.debug
        elif args[0] == 'w':
            log_func = log_func.warning
        elif args[0] == 'er':
            log_func = log_func.error
        elif args[0] == 'c':
            log_func = log_func.critical
        elif args[0] == 'ex':
            log_func = log_func.exception

        if 'pp' in kwargs:
            from pprint import pprint
            pprint(*args, **kwargs)
        elif 'p' in kwargs:
            print(*args, **kwargs)
        else:
            if args[1:] is not None:
                format = (len(args) - 1) * "%s "
                log_func(format, *list(map(str, args[1:])), **kwargs)    
    

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
        operations = self.get_widget_by_id(1)

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
                # TODO ADD WARNINGS
                warnings[index] = self.WARNINGS[index]
                widget.setStyleSheet("border: 1px solid red;")
            else:
                # TODO delete warnings
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
