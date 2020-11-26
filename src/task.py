from docx import Document
from src.logger.logger import Log
from math import ceil
from random import choice, randint

from src.file_manager import open_file, documents_path


class Example:
    def __init__(self, *args, result):
        self._params = args
        # 1 + 2 = 3 args = [1, '+', 2] result = 3
        self._result = result
    
    def docx_format(self, with_answer=False):
        params = ' '.join(map(str, self._params)) + ' = ' + str(self._result) if with_answer else ' '
        return params

    def __str__(self):
        return ' '.join(map(str, self._params)) + ' = ' + str(self._result)

    def __repr__(self):
        return self.__str__()


class Task:
    def __init__(self, expressions_count, columns_num, operations, num_range: tuple):
        self._field = []
        self.expressions_count = expressions_count
        self.columns_num = columns_num
        self.operations = operations
        self.num_range = num_range

        self.ex_generator = ExampleGenerator(self)
        self.ex_generator.generate_final()

    def add_item(self, item: Example):
        if len(self._field) >= self.expressions_count:
            return IndexError
        self._field.append(item)

    def get_field(self):
        return self._field

    def to_sqlite_format(self):
        return [','.join(self.operations), self.expressions_count, self.columns_num, self.num_range[0], self.num_range[1]]

    @staticmethod
    def from_sqlite_format(sqlite_response):
        # sqlite_response example: ('+,-', 17, 3, 10, 49)
        return Task(sqlite_response[1], sqlite_response[2], sqlite_response[0], (sqlite_response[3], sqlite_response[4]))
    
    def iterate_field(self):
        for ex in self._field:
            yield ex
    
    def save(self, file_name, with_answers=False):
        eo = ExportOutput(self)
        eo.fill_table(with_answers)
        eo.save(file_name)


class ExampleGenerator:
    def __init__(self, task: Task):
        self._task = task
        self._operations = task.operations
        self._from_num, self._to_num = task.num_range

    def generate_example(self):
        op = choice(self._operations)
        a = randint(self._from_num, self._to_num)
        b = randint(self._from_num, self._to_num)
        try:
            Log.log('d', "data: ", a, op, b)
            ret = eval(str(a) + op + str(b))
            Log.log('d', ret)
            ex = Example(a, op, b, result=ret)
            return ex
        except Exception:
            return Exception

    def generate_final(self):
        errors = False
        for _ in range(self._task.expressions_count):
            ex = self.generate_example()
            if not ex:
                errors = True
                Log.log('d', 'Cannot generate Example')
                Log.log('d', ex)
                continue
            self._task.add_item(ex)
        if errors:
            Log.log('er', "Table is incomplete")



class ExportOutput:
    def __init__(self, task: Task):
        self.task = task
        document = Document()
        self.doc = document
        self.rows = ceil(task.expressions_count / task.columns_num)
        self.cols = task.columns_num
        # create table
        self.table = document.add_table(rows=self.rows, cols=self.cols)

    def fill_table(self, with_answers=False):
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

    def save(self, file_name):
        self.doc.add_page_break()
        name = open_file(documents_path() + '/' + file_name)
        Log.log('d', 'name: ', name)
        if name[0] == '':
            return
        self.doc.save(name[0])
