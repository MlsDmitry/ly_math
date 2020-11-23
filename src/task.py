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
    def __init__(self, num_items, seperate_by_num):
        self._field = []
        self.num_items = num_items
        self.seperate_by_num = seperate_by_num

    def add_item(self, item: Example):
        if len(self._field) >= self.num_items:
            return IndexError
        self._field.append(item)

    def get_field(self):
        return self._field
        
    


class ExampleGenerator:
    def __init__(self, task: Task, operations, num_range: tuple):
        self._task = task
        self._operations = operations
        self._from_num, self._to_num = num_range

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
