from src.modules.expression.expression_controller import Controller

class App:
    def __init__(self):
        self.controller = Controller()
        self.controller.show_view()
