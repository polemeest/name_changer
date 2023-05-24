import time, os
from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):


    def setupUi(self, MainWindow):
        self.container = 0
        self.flag = False
        self.last_chosen_path = 'C:/'
        self.dirs = []
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(300, 410)

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(300, 410))
        MainWindow.setMaximumSize(QtCore.QSize(300, 440))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(8)
        font.setBold(False)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")

        self.listWidget = QtWidgets.QListWidget(parent=self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(10, 10, 161, 192))
        self.listWidget.setObjectName("listWidget")

        self.file_pushButton = QtWidgets.QPushButton(parent=self.centralwidget,  clicked=lambda: self.choose_file(False))
        self.file_pushButton.setGeometry(QtCore.QRect(180, 10, 111, 31))
        self.file_pushButton.setFont(font)
        self.file_pushButton.setObjectName("file_pushButton")

        self.folder_pushButton = QtWidgets.QPushButton(parent=self.centralwidget,  clicked=lambda: self.choose_file(True))
        self.folder_pushButton.setGeometry(QtCore.QRect(180, 50, 111, 31))
        self.folder_pushButton.setFont(font)
        self.folder_pushButton.setObjectName("folder_pushButton")

        self.delete_pushButton = QtWidgets.QPushButton(parent=self.centralwidget, clicked=lambda: self.delete())
        self.delete_pushButton.setGeometry(QtCore.QRect(180, 100, 111, 31))
        self.delete_pushButton.setFont(font)
        self.delete_pushButton.setObjectName("delete_pushButton")

        self.exec_pushButton = QtWidgets.QPushButton(parent=self.centralwidget,  clicked=lambda: self.rename())
        self.exec_pushButton.setGeometry(QtCore.QRect(180, 150, 111, 51))
        self.exec_pushButton.setFont(font)
        self.exec_pushButton.setObjectName("exec_pushButton")

        self.progressBar = QtWidgets.QProgressBar(parent=self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(10, 360, 291, 23))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")

        self.frame = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(10, 210, 281, 141))
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")

        self.verticalLayoutWidget = QtWidgets.QWidget(parent=self.frame)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 769, 135))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")

        self.label = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        self.label.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QtCore.QSize(270, 0))
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)

        self.prefix = QtWidgets.QLineEdit(parent=self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.prefix.sizePolicy().hasHeightForWidth())
        self.prefix.setSizePolicy(sizePolicy)
        self.prefix.setMinimumSize(QtCore.QSize(270, 0))
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(12)
        font.setBold(False)
        self.prefix.setFont(font)
        self.prefix.setInputMask("")
        self.prefix.setText("")
        self.prefix.setFrame(True)
        self.prefix.setObjectName("prefix")
        self.verticalLayout.addWidget(self.prefix)

        self.suffix = QtWidgets.QLineEdit(parent=self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.suffix.sizePolicy().hasHeightForWidth())
        self.suffix.setSizePolicy(sizePolicy)
        self.suffix.setMinimumSize(QtCore.QSize(270, 0))
        self.suffix.setFont(font)
        self.suffix.setObjectName("suffix")
        self.verticalLayout.addWidget(self.suffix)

        self.separator = QtWidgets.QLineEdit(parent=self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.separator.sizePolicy().hasHeightForWidth())
        self.separator.setSizePolicy(sizePolicy)
        self.separator.setMinimumSize(QtCore.QSize(270, 0))
        self.separator.setFont(font)
        self.separator.setObjectName("separator")
        self.verticalLayout.addWidget(self.separator)
        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 300, 25))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def fnamed(self, fname):
        for item in fname:
            self.listWidget.addItem(item.split('/')[-1])
        self.last_chosen_path = '/'.join(fname[0].split('/')[:-1])
        self.label.setText('Ready to go')
        self.container = len(fname)


    def dirnamed(self, dirname):
        self.listWidget.addItem(dirname)
        self.container += len(os.listdir(dirname))
        self.dirs.append(dirname)
        self.last_chosen_path = dirname
        self.label.setText('Ready to go')



    def choose_file(self, flag=False):
        self.progressBar.setValue(0)
        self.flag = flag
        fname = dirname = ''
        if not flag:
            fname, _ = QtWidgets.QFileDialog.getOpenFileNames(self.file_pushButton, 'Open file', self.last_chosen_path, 'All files (*)')
        elif flag:
            dirname = QtWidgets.QFileDialog.getExistingDirectory(self.folder_pushButton, 'Select folder', self.last_chosen_path)
        #
        if fname:
            self.fnamed(fname)
        elif dirname:
            self.dirnamed(dirname)
        else:
            self.label.setText('<font color="red">0 files have been chosen. Something went wrong...</font>')


    def flagged(self, path, pre, suf, sep):
        for item in range(self.listWidget.count()):
            try:
                form = self.listWidget.item(item).text().split('.')[-1]
                os.rename(f"{path}/{self.listWidget.item(item).text()}", f"{path}/{pre}{sep}{str(int(suf) + item)}.{form}")
                self.progressBar.setValue(self.progressBar.value() + 1)
            except FileExistsError:
                self.progressBar.setValue(self.progressBar.value() + 1)
                continue


    def unflagged(self, pre, suf, sep):
        for directory in self.dirs:
            try:
                for index, item in enumerate(os.listdir(directory)):
                    form = item.split('.')[-1]
                    os.rename(f'{directory}/{item}', f'{directory}/{pre}{sep}{str(int(suf) + index)}.{form}')
                    self.progressBar.setValue(self.progressBar.value() + 1)
            except FileExistsError:
                self.progressBar.setValue(self.progressBar.value() + 1)
                continue
        self.dirs.clear()


    def rename(self):
        path = self.last_chosen_path
        pre, suf, sep = max(self.prefix.text(), '0'), max(self.suffix.text(), '0'), ( '-', self.separator.text())[bool(self.separator.text())]
        self.progressBar.setMaximum(self.container)
        try:
            if not self.flag:
                start = time.time()
                self.flagged(path, pre, suf, sep)
            else:
                start = time.time()
                self.unflagged(pre, suf, sep)
            self.listWidget.clear()
            self.label.setText(f'<font color="green">Completed succesfully!</font> In {round(time.time() - start, 2)} seconds')
            self.progressBar.setValue(100)
            self.flag = False
        except Exception:
            self.label.setText(f'<font color="red">Critical Error</font>')
            self.flag = False

    def delete(self):
        try:
            chosen = self.listWidget.currentRow()
            self.listWidget.takeItem(chosen)
        except AttributeError:
            self.label.setText('<font color="red">Something in code went wrong.</font>')

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Renamer v 0.9"))
        icon = QtGui.QIcon('icon.jpg')
        MainWindow.setWindowIcon(icon)
        self.file_pushButton.setText(_translate("MainWindow", "Выбрать файлы"))
        self.folder_pushButton.setText(_translate("MainWindow", "Выбрать папку"))
        self.delete_pushButton.setText(_translate("MainWindow", "Убрать из списка"))
        self.exec_pushButton.setText(_translate("MainWindow", "Переименовать"))
        self.label.setText(_translate("MainWindow", "Please, choose files and enter prefix to proceed"))
        self.prefix.setPlaceholderText(_translate("MainWindow", "Enter prefix"))
        self.suffix.setPlaceholderText(_translate("MainWindow", "Enter suffix"))
        self.separator.setPlaceholderText(_translate("MainWindow", "Enter separator"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
