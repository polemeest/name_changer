# Form implementation generated from reading ui file 'renamer3.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.

import os
import time
from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.container = 0
        self.flag = False
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 430)
        MainWindow.setMinimumSize(QtCore.QSize(400, 430))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(8)
        MainWindow.setFont(font)
        icon = QtGui.QIcon.fromTheme("document-properties")
        MainWindow.setWindowIcon(icon)
        MainWindow.setWindowOpacity(1.0)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(parent=self.centralwidget, clicked=lambda: self.click())
        self.pushButton.setGeometry(QtCore.QRect(280, 80, 110, 40))
        self.pushButton.setObjectName("pushButton")
        self.progressBar = QtWidgets.QProgressBar(parent=self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(10, 340, 371, 31))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setMinimum(0)

        self.progressBar.setObjectName("progressBar")
        self.pushButton_2 = QtWidgets.QPushButton(parent=self.centralwidget, clicked=lambda: self.rename())
        self.pushButton_2.setGeometry(QtCore.QRect(280, 130, 110, 40))
        self.pushButton_2.setObjectName("pushButton_2")
        self.prefix = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.prefix.setGeometry(QtCore.QRect(280, 20, 113, 22))
        self.prefix.setObjectName("prefix")
        self.prefix_2 = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.prefix_2.setGeometry(QtCore.QRect(280, 50, 113, 22))
        self.prefix_2.setObjectName("prefix_2")
        self.listWidget = QtWidgets.QListWidget(parent=self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(10, 20, 256, 192))
        self.listWidget.setObjectName("listWidget")

        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 230, 340, 20))
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 400, 18))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)



    def click(self):
        fname, _ = QtWidgets.QFileDialog.getOpenFileNames(self.pushButton, 'Open file', '../test_txts', 'All files (*)')
        self.container = len(fname)
        if fname:
            for item in fname:
                self.listWidget.addItem(item.split('/')[-1])
            self.label.setText('/'.join(fname[0].split('/')[:-1]))
            self.progressBar.setValue(0)
            self.label.setText('Ready to go')
        else:
            self.label.setText('0 files have been chosen. Something went wrong...')

    def rename(self):
        path = self.label.text()
        pre, suf = max(self.prefix.text(), '0'), max(self.prefix_2.text(), '0')
        self.progressBar.setMaximum(self.container)
        if not self.flag:
            start = time.time()
            for item in range(self.listWidget.count()):
                try:
                    form = self.listWidget.item(item).text().split('.')[-1]
                    os.rename(f"{path}/{self.listWidget.item(item).text()}", f"{path}/{pre}-{str(int(suf) + item)}.{form}")
                    self.progressBar.setValue(self.progressBar.value() + 1)
                except FileExistsError:
                    self.progressBar.setValue(self.progressBar.value() + 1)
                    continue
            self.listWidget.clear()
            self.label.setText('Completed succesfully!')
            print(time.time() - start)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "RenameMe"))
        self.pushButton.setText(_translate("MainWindow", "Выбрать файлы"))
        self.pushButton_2.setText(_translate("MainWindow", "Выполнить"))
        self.label.setText(_translate("MainWindow", "Path : None"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
