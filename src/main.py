from src.logger.logger import Log
from src.modules.expression.expression_controller import Controller

class App:
    def __init__(self):
        self.controller = Controller()
        self.controller.show_view()
    
    def quit(self):
        Log.log('d', 'quit')
        self.controller.dbm.save()
        self.controller.dbm.close()
