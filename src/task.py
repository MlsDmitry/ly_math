from random import choice, randint


class Example:
    def __init__(self, *args, result):
        self._params = args
        # 1 + 2 = 3 args = [1, '+', 2] result = 3
        self._result = result

    def __str__(self):
        return ' '.join(map(str, self._params)) + '= ' + str(self._result)

    def __repr__(self):
        return self.__str__()

class Task:
    def __init__(self, num_items, separate_by_num, operations, num_range: tuple):
        self._field = []
        self.num_items = num_items
        self.separate_by_num = separate_by_num
        self.operations = operations
        self.num_range = num_range

        self.ex_generator = ExampleGenerator(self)

    def add_item(self, item: Example):
        if len(self._field) >= self.num_items:
            return IndexError
        self._field.append(item)

    def get_field(self):
        return self._field
    
    def to_sqlite_format(self):
        return [','.join(self.operations), self.num_items, self.separate_by_num, self.num_range[0], self.num_range[1]]
    
    @staticmethod
    def from_sqlite_format(sqlite_response):
        # sqlite_response example: ('+,-', 17, 3, 10, 49)
        return Task(sqlite_response[1], sqlite_response[2], sqlite_response[0], (sqlite_response[3], sqlite_response[4]))
        
    


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
            print("data: ", a, op, b)
            ret = eval(str(a) + op + str(b))
            print(ret)
            ex = Example((a, op, b), result=ret)
            return ex
        except Exception:
            return Exception


    def generate_final(self):
        errors = False
        for _ in range(self._task.num_items):
            ex = self.generate_example()
            if not ex:
                errors = True
                print('Cannot generate Example')
                print(ex)
                continue
            self._task.add_item(ex)
        if errors:
            print("Table is incomplete")
    
    def iterate_field(self, func):
        for ex in self._task.get_field():
            func(ex)


class ExportOutput:
    pass