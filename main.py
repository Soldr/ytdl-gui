import typing, sys
from PyQt5 import QtCore
from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QTabWidget, QMainWindow, QVBoxLayout, QApplication, QDesktopWidget
from PyQt5.QtCore import pyqtSlot

# components
from components import TopBar, TabWidget

class App(QMainWindow):
    def __init__(self):
        super().__init__()

        self.title = "YTDL v1.0"
        
        # top, left, width, height
        self.setGeometry(0, 0, 512, 512)

        self.setWindowTitle(self.title)
        
        self.main_window = MainWindow(self)

        self.setCentralWidget(self.main_window)

        # Center the window
        qtRectangle = self.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center()
        qtRectangle.moveCenter(centerPoint)
        self.move(qtRectangle.topLeft())

        self.show()

class MainWindow(QWidget):
    def __init__(self, parent):
        super(QWidget, self).__init__(parent)
        # create the top bar
        self.top_bar = TopBar(self)

        # Create the tabbed view
        self.tab_widget = TabWidget(self)
        
        # create layout
        layout = QVBoxLayout()

        # layout spacingg
        layout.setSpacing(0)
        layout.setContentsMargins(0, 0, 0, 0)

        layout.addWidget(self.top_bar)
        layout.addWidget(self.tab_widget)

        # actually set the layout to the parent
        self.setLayout(layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = App()
    window.show()
    sys.exit(app.exec_())