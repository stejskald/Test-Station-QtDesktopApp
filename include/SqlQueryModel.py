from PyQt6.QtSql import QSqlQueryModel


class SqlQueryModel(QSqlQueryModel):
    def __init__(self):
        super(SqlQueryModel, self).__init__()
        
        self._data = self.data()

    # def rowCount(self):
    #     # returns the length of the outer list - number of rows
    #     return len(self._data)

    # def columnCount(self):
    #     # takes the longest row from data and returns the length - number of columns
    #     return len(max(self._data, key=len))
