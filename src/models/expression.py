class ExpressionModel:
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