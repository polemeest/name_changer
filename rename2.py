import typing
from PyQt6 import QtCore
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QComboBox, QSpinBox, QTextEdit, QFormLayout, QLineEdit
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
        form_layout = QFormLayout()
        self.setLayout(form_layout)

        # label
        test_label = QLabel('Rename all of this')
        test_label.setFont(QFont('Helvetica', 24))

        # Entries
        prefix = QLineEdit(self)
        suffix = QLineEdit(self)

        # Button
        combo_button = QPushButton('Set label', clicked=lambda: fu_combo_button())

        # setting the layout
        form_layout.addRow(test_label)
        form_layout.addRow('prefix', prefix)
        form_layout.addRow('suffix', suffix)
        form_layout.addRow(combo_button)

        # funcs
        def fu_combo_button():
            test_label.setText(f"Renaming objects to {prefix.text()}-{suffix.text()}")

        # Turn on
        self.show()


app = QApplication(sys.argv)
mw = MainWindow()

app.exec()