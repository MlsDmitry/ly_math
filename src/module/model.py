

class Model:

    @staticmethod
    def validate_operation(config):
        return len(config.operations) > 0

    @staticmethod
    def validate_min_max_number(config):
        print(len(config.min_number))
        return len(config.min_number) > 0


class Config:

    def __init__(self):
        self.operations = []
        self.expressions_count = ""
        self.columns = ""
        self.min_number = ""
        self.max_number = ""



