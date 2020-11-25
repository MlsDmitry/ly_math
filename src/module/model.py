class Config:

    def __init__(self):
        self.operations = []
        self.expressions_count = ""
        self.columns = ""
        self.min_number = ""
        self.max_number = ""


class Model:

    @staticmethod
    def validate_operation(config):
        return len(config.operations) > 0

    @staticmethod
    def validate_min_max_number(config):
        return len(config.min_number) > 0 and \
            len(config.max_number) > 0 and \
            int(config.min_number) < int(config.max_number)

    def validate_expressions_count(config):
        return len(config.expressions_count) > 0

    def validate_columns(config):
        return len(config.columns) > 0
