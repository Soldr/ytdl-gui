from PyQt5.QtWidgets import QWidget, QTabWidget, QVBoxLayout
from . import tabs

class TabWidget(QWidget):
    def __init__(self, parent):
        super(QWidget, self).__init__(parent)
        # Init tabs
        self.tabs = QTabWidget()
        self.tab_all = tabs.All()
        self.tab_inprogress = QWidget()
        self.tab_done = QWidget()
        self.tabs.resize(512, 512)

        # add tabs in
        self.tabs.addTab(self.tab_all, "All")
        self.tabs.addTab(self.tab_inprogress, "In Progress")
        self.tabs.addTab(self.tab_done, "Done")

        # create layout
        layout = QVBoxLayout(self)
        layout.setContentsMargins(4, 4, 4, 4)

        layout.addWidget(self.tabs)
        self.setLayout(layout)
