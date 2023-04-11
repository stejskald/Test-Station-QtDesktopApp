from PyQt6.QtCore import Qt
from PyQt6.QtSql import QSqlQueryModel


class SqlQueryModel(QSqlQueryModel):
    def __init__(self):
        super(SqlQueryModel, self).__init__()

    def data(self, index, role=Qt.ItemDataRole.DisplayRole):
        if role == Qt.ItemDataRole.DisplayRole:
            try:
                return self.query.result()[index.row()][index.column()]
            except IndexError:
                return ""

        # # Entire cell content will NOT disappear if double clicked for editting
        # if role == Qt.ItemDataRole.EditRole:
        #     return self.query.result()[index.row()][index.column()]

        # # Tooltip message will be shown when hovering over a cell
        # if role == Qt.ItemDataRole.ToolTipRole:
        #     return "row: {}, col: {}".format(index.row(), index.column())

    def rowCount(self):
        # returns the length of the outer list - number of rows
        return self.query().size()

    def columnCount(self):
        # takes the first row of query result and returns its length - number of columns
        return len(self.query().result().data(0))
