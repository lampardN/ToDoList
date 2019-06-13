from PyQt5 import QtWidgets


class Item:
    def __init__(self):
        self.object = object
        self.id = None
        self.tagCh = False
        self.textCh = False
        self.box = QtWidgets.QHBoxLayout()

        self.line = QtWidgets.QTextEdit()
        self.line.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        self.line.setFixedHeight(30)

        self.update_button = QtWidgets.QPushButton()
        self.update_button.setText(u"\u270E")
        self.update_button.clicked.connect(self.updateText)

        self.del_button = QtWidgets.QPushButton()
        self.del_button.setText('X')
        self.del_button.clicked.connect(self.__del__)

        self.status = QtWidgets.QComboBox()
        self.status.addItems(('active', 'complete'))
        self.status.currentIndexChanged.connect(self.updateTag)

        self.box.addWidget(self.line)
        self.box.addWidget(self.update_button)
        self.box.addWidget(self.status)
        self.box.addWidget(self.del_button)

    def __del__(self):
        try:
            self.line.deleteLater()
            self.update_button.deleteLater()
            self.status.deleteLater()
            self.del_button.deleteLater()
            self.box.deleteLater()
        except:
            pass
        self.object = None

    def setTag(self, tag):
        self.status.setCurrentText(tag)

    def setText(self, text):
        self.line.setText(text)

    def updateTag(self):
        if self.tagCh:
            self.tagCh = False
        else:
            self.tagCh = True

    def updateText(self):
        if self.textCh:
            self.textCh = False
        else:
            self.textCh = True