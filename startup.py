from PyQt5.QtWidgets import QMainWindow, QApplication
import sys

from src.main import App
from src.logger.logger import Log

if __name__ == '__main__':
    # initialize Log class
    log = Log()
    
    qApp = QApplication(sys.argv)

    app = App()
    exit_code = qApp.exec_()
    app.quit()
    sys.exit(exit_code)



