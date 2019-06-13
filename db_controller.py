from PyQt5 import QtSql


class dbController:
    def __init__(self, date):
        self.db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        self.db.setDatabaseName('ToDo.db')
        self.db.open()
        self.date = date
        self.query = QtSql.QSqlQuery()
        self.info = []

    def addInTable(self, text):
        self.query.prepare('insert into ToDo values(null, ?, ?, ?)')
        self.query.addBindValue(self.date)
        self.query.addBindValue(text)
        self.query.addBindValue('active')
        self.query.exec_()

    def selectByDate(self):
        self.query.prepare('select * from ToDo where date=(?)')
        self.query.addBindValue(self.date)
        self.query.exec_()

    def selectByTag(self, tag):
        self.query.prepare('select * from ToDo where date=(?) and tag=(?)')
        self.query.addBindValue(self.date)
        self.query.addBindValue(tag)
        self.query.exec_()

    def getInfo(self, tag='all'):
        if tag == 'all':
            self.selectByDate()
        else:
            self.selectByTag(tag)
        self.query.first()
        while self.query.isValid():
            self.info.append(
                (
                    self.query.value('text'),
                    self.query.value('tag'),
                    self.query.value('id')
                )
            )
            self.query.next()
        self.query.finish()
        return self.info

    def clear(self):
        self.info = []

    def delItem(self, text):
        self.query.prepare('delete from ToDo where id=(?) and date=(?)')
        self.query.addBindValue(text)
        self.query.addBindValue(self.date)
        self.query.exec_()
        self.query.finish()

    def updateText(self, id, text):
        self.query.prepare('update ToDo set text=(?) where id=(?)')
        self.query.addBindValue(text)
        self.query.addBindValue(id)
        self.query.exec_()
        self.query.finish()

    def updateTag(self, id, tag):
        self.query.prepare('update ToDo set tag=(?) where id=(?)')
        self.query.addBindValue(tag)
        self.query.addBindValue(id)
        self.query.exec_()
        self.query.finish()
