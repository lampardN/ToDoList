from PyQt5 import QtWidgets, QtCore


class top_line:
    def __init__(self):
        self.box = QtWidgets.QHBoxLayout()

        self.line = QtWidgets.QTextEdit()
        self.line.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        self.line.setFixedHeight(30)

        self.calendar = QtWidgets.QDateEdit()
        self.calendar.setCalendarPopup(True)
        self.calendar.setDate(QtCore.QDate().currentDate())
        self.calendar.setFixedSize(100, 25)
        self.calendar.dateChanged.connect(self.chDate)

        self.date = '{}.{}.{}'.format(self.calendar.date().day(),
                                      self.calendar.date().month(),
                                      self.calendar.date().year())

        self.button = QtWidgets.QPushButton()
        self.button.setFixedSize(25, 25)
        self.button.setText(u"\u270E")

        self.status = QtWidgets.QComboBox()
        self.status.addItems(('all', 'active', 'complete'))

        self.box.addWidget(self.line)
        self.box.addWidget(self.calendar)
        self.box.addWidget(self.status)
        self.box.addWidget(self.button)

    def getText(self):
        text = self.line.toPlainText()
        self.line.clear()
        return text

    def chDate(self):
        self.date = '{}.{}.{}'.format(self.calendar.date().day(),
                                      self.calendar.date().month(),
                                      self.calendar.date().year())

    def getDate(self):
        return self.date
