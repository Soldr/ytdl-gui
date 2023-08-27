from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QSizePolicy

styles = """
.all:nth-child(even) {
    background-color: #ff0000
}
"""

class All(QWidget):
    def __init__(self):
        super(QWidget, self).__init__()
        
        # create layout for the "row" view
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        layout.addStretch()

        self.layout = layout
        # list of rows
        self.rows = []

        self.addRow()
        self.addRow()
        self.addRow()
        self.addRow()
        self.addRow()


        

    def addRow(self):
        row = QWidget()

        # create layout
        layout = QHBoxLayout(row)
        layout.addWidget(QLabel(text="test"))
        layout.addWidget(QPushButton(text="btn"))

        # remove the horrid margins
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        self.rows.append(row)
        self.layout.insertWidget(0, row)
        

        