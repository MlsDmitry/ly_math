from src.logger.logger import Log
from math import ceil
from random import choice, randint

from src.models.expression import ExpressionModel
from src.models.task import TaskModel


class ExampleGeneratorService:
    def __init__(self, task: TaskModel):
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
            ex = ExpressionModel(a, op, b, result=ret)
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



