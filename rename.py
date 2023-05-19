import typing
from PyQt6 import QtCore
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QComboBox, QSpinBox, QTextEdit
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

        # text
        test_text = QTextEdit(self, lineWrapMode=QTextEdit.LineWrapMode.FixedColumnWidth,
                              lineWrapColumnOrWidth=50, acceptRichText=True,
                              placeholderText='Print Somehting',
                              readOnly=False)
        self.layout().addWidget(test_text)

        # label
        test_label = QLabel('Rename all of this')
        test_label.setFont(QFont('Helvetica', 24))
        self.layout().addWidget(test_label)

        # Button
        combo_button = QPushButton('Set label', clicked=lambda: fu_combo_button())
        self.layout().addWidget(combo_button)

        spin_button = QPushButton('Add value', clicked=lambda: fu_spin_button())
        self.layout().addWidget(spin_button)

        text_button = QPushButton('Change text', clicked=lambda: fu_text_button())
        self.layout().addWidget(text_button)


        # Combobox
        test_Cbox = QComboBox()
        test_Cbox.addItems(things)
        self.layout().addWidget(test_Cbox)

        # Spinbox
        test_Sbox = QSpinBox(self, value=10, maximum=100, minimum=0, singleStep=10, prefix='number ', suffix=' xoxo')
        test_Sbox.setFont(QFont('Helvetica', 24))
        self.layout().addWidget(test_Sbox)



        # funcs
        def fu_combo_button():
            test_label.setText(f'You picked {test_Cbox.currentText()}')

        def fu_spin_button():
            test_label.setText(f'{test_label.text()} {test_Sbox.prefix()}{test_Sbox.value()}{test_Sbox.suffix()}')

        def fu_text_button():
            test_label.setText(f'{test_text.toPlainText()}')
            test_text.setPlainText('')
            test_text.setPlaceholderText('Print Something again')

        # Turn on
        self.show()


app = QApplication(sys.argv)
mw = MainWindow()

app.exec()