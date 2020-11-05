from PyQt5.QtWidgets import QWidget, QStackedWidget
from PyQt5.QtGui import QPixmap, QPainter
from PyQt5.QtCore import QTimeLine

class FaderWidget(QWidget):
    
    def __init__(self, old_widget, new_widget):

        QWidget.__init__(self, new_widget)
        
        self.old_pixmap = QPixmap(new_widget.size())
        old_widget.render(self.old_pixmap)

        self.pixmap_opacity = None
        self.timeline = QTimeLine(333, self)
        self.timeline.valueChanged.connect(self.animate)
        self.timeline.finished.connect(self.close)
        
        self.resize(new_widget.size())
        self.show()
    
    def start(self, old_widget, new_widget):
        self.pixmap_opacity = 1.0
        self.old_pixmap = QPixmap(new_widget.size())
        old_widget.render(self.old_pixmap)

        self.timeline.start()

        self.resize(new_widget.size())
        self.show()
    
    def animate(self, value):
    
        self.pixmap_opacity = 1.0 - value
        self.repaint()

    def paintEvent(self, event):
        if self.pixmap_opacity:
            QWidget.paintEvent(self, event)
            painter = QPainter(self)
            painter.setOpacity(self.pixmap_opacity)
            painter.drawPixmap(0, 0, self.old_pixmap)

class StackedWidget(QStackedWidget):

    def __init__(self, parent = None):
        QStackedWidget.__init__(self, parent)
    
    def setCurrentIndex(self, index):
        self.fader_widget = FaderWidget(self.currentWidget(), self.widget(index))
        QStackedWidget.setCurrentIndex(self, index)
    
    def set_page_n(self, n):
        self.setCurrentIndex(n)
    
    