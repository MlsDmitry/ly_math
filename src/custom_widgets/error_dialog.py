from PyQt5.QtCore import Qt
from src.logger.logger import Log
from PyQt5.QtWidgets import QDialogButtonBox, QDialog, QGridLayout, QInputDialog, QLabel, QVBoxLayout

class ErrorDialog(QDialog):
    
    def __init__(self, *args, **kwargs):
        super(ErrorDialog, self).__init__(*args, **kwargs)

        self.setWindowTitle("Error")

        buttons = QDialogButtonBox.Ok | QDialogButtonBox.Cancel

        self.layout = QVBoxLayout()

        self.buttonBox = QDialogButtonBox(buttons)
        self.label = QLabel("Error")
        self.label.setAlignment(Qt.AlignCenter)
        
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

        self.layout.addWidget(self.label)
        self.layout.addWidget(self.buttonBox)

        self.setLayout(self.layout)