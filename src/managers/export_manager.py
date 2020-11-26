from docx import Document
from src.logger.logger import Log
from src.models.task import TaskModel
from math import ceil
from src.managers.file_manager import open_file, documents_path



class ExportManager:
    def __init__(self, task: TaskModel):
        self.task = task
        document = Document()
        self.doc = document
        self.rows = ceil(task.expressions_count / task.columns_num)
        self.cols = task.columns_num
        # create table
        self.table = document.add_table(rows=self.rows, cols=self.cols)

    def _fill_table(self, with_answers=False):
        expression_index = 0
        
        for col_index in range(self.cols):
            for row_index in range(self.rows):
                if expression_index >= self.task.expressions_count:
                    return
                cell = self.table.rows[row_index].cells[col_index]
                expression = self.task.get_field()[expression_index]
                Log.log('d', 'Expression: ', expression.docx_format())
                cell.text = expression.docx_format(with_answers)
                expression_index += 1

    def save(self, file_name, with_answers=False):
        self._fill_table(with_answers)
        self.doc.add_page_break()

        name = open_file(documents_path() + '/' + file_name)
        Log.log('d', 'name: ', name)
        if name[0] == '':
            return
        self.doc.save(name[0])