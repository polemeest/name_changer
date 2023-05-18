import typing
from PyQt6 import QtCore
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel
from PyQt6.QtGui import QFont
import sys


class MainWindow(QWidget):
    def __init__(self) -> None:
        super().__init__()
        # Set title
        self.setWindowTitle("Temporary Name")
        self.setMinimumSize(800, 600)

        # layout
        self.setLayout(QVBoxLayout())

        # label
        test_label = QLabel('Rename all of this')
        test_label.setFont(QFont('Helvetica', 24))
        self.layout().addWidget(test_label)


        # Turn on
        self.show()


app = QApplication(sys.argv)
mw = MainWindow()

app.exec()