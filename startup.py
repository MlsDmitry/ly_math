from PyQt5.QtWidgets import QMainWindow, QApplication
import sys

from src import App
from src.logger.logger import Log



if __name__ == '__main__':
    # initialize Log class
    log = Log()
    
    qApp = QApplication(sys.argv)
    app = App()
    app.show()
    sys.exit(qApp.exec_())
