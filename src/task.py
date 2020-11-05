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
    def __init__(self, num_items_row, num_items_col):
        self._field = []
        self.num_items = num_items_row * num_items_col
        self.num_items_row = num_items_row
        self.num_items_col = num_items_col

    def add_item(self, item: Example):
        if len(self._field) >= self.num_items:
            return IndexError
        self._field.append(item)

    def return_field_seperated(self):
        sub_table = 0
        table = [[] for _ in range(self.num_items_col)]
        for current_element_index, ex in enumerate(self._field):
            if (current_element_index % self.num_items_row) == 0 and current_element_index != 0:
                sub_table += 1
            print(sub_table, current_element_index)
            print(table[sub_table])
            table[sub_table].append(self._field[current_element_index])
        return table
    


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
