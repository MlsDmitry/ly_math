from src.models.expression import ExpressionModel
from src.services.example_generator_service import ExampleGeneratorService


class TaskModel:
    def __init__(self, expressions_count, columns_num, operations, num_range: tuple):
        self._field = []
        self.expressions_count = expressions_count
        self.columns_num = columns_num
        self.operations = operations
        self.num_range = num_range

        self.ex_generator = ExampleGeneratorService(self)
        self.ex_generator.generate_final()

    def add_item(self, item: ExpressionModel):
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
        return TaskModel(sqlite_response[1], sqlite_response[2], sqlite_response[0], (sqlite_response[3], sqlite_response[4]))
    