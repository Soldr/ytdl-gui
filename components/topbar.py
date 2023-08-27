from PyQt5.QtWidgets import QWidget, QPushButton, QLabel, QHBoxLayout
from PyQt5.QtGui import QPalette

class TopBar(QWidget):
    def __init__(self, parent):
        super(QWidget, self).__init__(parent)
        
        # set self class
        self.setObjectName("topbar")

        # appearance
        self.setStyleSheet("""
.topbar {
    background-color: #000000
}
""")        
        self.btn_pastelink = QPushButton(parent=self, text="Paste Link")
        
        
        # layout creation
        layout = QHBoxLayout()
        # layout spacing
        layout.setContentsMargins(4, 4, 4, 0)

        # add widgets
        layout.addWidget(self.btn_pastelink) 
        
        self.setLayout(layout)

