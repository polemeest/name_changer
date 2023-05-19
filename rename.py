import typing
from PyQt6 import QtCore
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QComboBox
from PyQt6.QtGui import QFont
import sys

things = [
        'First thing',
        'Second thing',
        'Third thing',
        'What? Are you kidding me?'
    ]


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

        # Button
        test_button = QPushButton('Set label', clicked=lambda: fu_test_button())
        self.layout().addWidget(test_button)

        # Combobox
        test_Cbox = QComboBox()
        test_Cbox.addItems(things)
        self.layout().addWidget(test_Cbox)

        # funcs
        def fu_test_button():
            test_label.setText(f'You picked {test_Cbox.currentText()}')

        # Turn on
        self.show()


app = QApplication(sys.argv)
mw = MainWindow()

app.exec()