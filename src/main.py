from src.module.controller import Controller

class App:
    def __init__(self):
        self.controller = Controller()
        self.controller.show_view()
