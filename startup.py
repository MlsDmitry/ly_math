from PyQt5.QtWidgets import QMainWindow, QApplication
import sys

from src import App



if __name__ == '__main__':
    qApp = QApplication(sys.argv)
    app = App()
    app.show()
    sys.exit(qApp.exec_())
