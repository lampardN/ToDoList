from PyQt5 import QtWidgets
from top_line import top_line
from item_line import Item
from db_controller import dbController


class Main(QtWidgets.QScrollArea):
    def __init__(self, parent=None):

        '''Initialization'''
        super().__init__(parent)
        self.setWidgetResizable(True)
        self.gb = QtWidgets.QGroupBox()
        self.line = top_line()
        self.layout = QtWidgets.QFormLayout()
        self.db = dbController(self.line.getDate())
        self.items = []
        self.setFixedSize(920, 640)

        '''Connections'''
        self.line.button.clicked.connect(self.addItem)
        self.line.calendar.dateChanged.connect(self.showTable)
        self.line.status.currentIndexChanged.connect(self.showTable)

        '''Windowed'''
        self.layout.addRow(self.line.box)
        self.gb.setLayout(self.layout)
        self.setWidget(self.gb)
        self.showTable()

    def addItem(self):
        self.items.append(Item())
        self.items[-1].setText(self.line.getText())
        self.layout.addRow(self.items[-1].box)
        self.db.addInTable(self.items[-1].line.toPlainText())
        self.showTable()

    def showTable(self):
        self.clearItems()
        self.db.date = self.line.getDate()
        for element in self.db.getInfo(self.line.status.currentText()):
            self.items.append(Item())
            self.items[-1].setText(element[0])
            self.items[-1].setTag(element[1])
            self.items[-1].id = element[2]
            self.items[-1].update_button.clicked.connect(self.updateText)
            self.items[-1].status.currentIndexChanged.connect(self.updateTag)
            self.items[-1].del_button.clicked.connect(self.delInTable)
            self.layout.addRow(self.items[-1].box)
        self.db.clear()

    def clearItems(self):
        for item in self.items:
            item.__del__()
        self.items = []

    def delInTable(self):
        for i in range(len(self.items)):
            if self.items[i].object == None:
                self.db.delItem(self.items[i].id)
                self.showTable()
                break


    def updateText(self):
        for i in range(len(self.items)):
            if self.items[i].textCh:
                self.db.updateText(self.items[i].id,
                                   self.items[i].line.toPlainText())
                self.items[i].updateText()
                self.showTable()
                break


    def updateTag(self):
        for i in range(len(self.items)):
            if self.items[i].tagCh:
                self.db.updateTag(self.items[i].id,
                                  self.items[i].status.currentText())
                self.items[i].updateTag()
                print(self.items[i].tagCh)
                self.showTable()
                break


if __name__ == '__main__':
    from sys import *
    app = QtWidgets.QApplication(argv)
    window = Main()
    window.show()
    exit(app.exec_())
