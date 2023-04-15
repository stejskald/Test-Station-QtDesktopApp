from PyQt6.QtGui import QFont, QFontMetrics
from PyQt6.QtSql import QSqlDatabase, QSqlQuery, QSqlQueryModel
from PyQt6.QtWidgets import QWidget
from include.UIs.DatabaseTab_ui import Ui_DatabaseTab

# SELECT * FROM pg_catalog.pg_tables WHERE schemaname != 'pg_catalog' AND schemaname != 'information_schema'
# Use Promote to... in Qt Designer on the QCOmboBox

# class ComboTest : public QComboBox {
#   Q_OBJECT
#  public:
#   explicit ComboTest(QWidget* parent = nullptr);
#  public slots:
#  public:
#   virtual void showPopup() override {
#     clear();
#     for (int var = 0; var < 10000; ++var) {
#       addItem("TEST" + QString::number(var));
#     }
#     QComboBox::showPopup();
#   }
# };


# pyuic6 UIs/DatabaseTab.ui -o UIs/ui_DatabaseTab.py
class DatabaseTab(QWidget, Ui_DatabaseTab):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self._lineEditminWidth = self.lineEditUser.minimumWidth()

        self.btnLogin.clicked.connect(self.loginToDB)

        self.lineEditSelectColumns.textChanged.connect(self.lineEditContentChanged)
        self.lineEditSelectCondition.textChanged.connect(self.lineEditContentChanged)
        self.lineEditInsertColumns.textChanged.connect(self.lineEditContentChanged)
        self.lineEditInsertValues.textChanged.connect(self.lineEditContentChanged)
        self.lineEditUpdateColumns.textChanged.connect(self.lineEditContentChanged)
        self.lineEditUpdateValues.textChanged.connect(self.lineEditContentChanged)
        self.lineEditUpdateCondition.textChanged.connect(self.lineEditContentChanged)
        self.lineEditDeleteCondition.textChanged.connect(self.lineEditContentChanged)

        self.btnInsert.clicked.connect(self.insertIntoTable)
        self.btnSelect.clicked.connect(self.selectFromTable)
        self.btnUpdate.clicked.connect(self.updateTableRecords)
        self.btnDelete.clicked.connect(self.deleteTableRecords)

        # self.SQLQueryModel = SqlQueryModel()
        self.SQLQueryModel = QSqlQueryModel()
        self.SQLTableView.setModel(self.SQLQueryModel)

    def loginToDB(self):
        user = self.lineEditUser.text()
        password = self.lineEditPassword.text()
        databaseName = self.comboBoxDBName.currentText()

        self.devDB = QSqlDatabase.addDatabase("QPSQL")
        self.devDB.setHostName("localhost")
        self.devDB.setPort(5432)
        self.devDB.setDatabaseName(databaseName)
        self.devDB.setUserName(user)  # postgres is the default root username
        self.devDB.setPassword(password)  # add your password here

        if not self.devDB.open():
            self.textDBStatus.setText(
                "Database Error: {}".format(self.devDB.lastError().databaseText())
            )
        else:
            self.textDBStatus.setText("Connection to the DB was successful!")

    def insertIntoTable(self):
        table = self.comboBoxTableViewed.currentText()
        columns = self.lineEditInsertColumns.text()
        values = self.lineEditInsertValues.text()
        queryInsertCmd = "INSERT INTO "

        if not columns or not values:
            self.textDBStatus.setText(
                'Při vytváření záznamu nesmí být pole "Sloupce" a "Hodnoty" prázdné!'
            )
            return
        else:
            queryInsertCmd += '"{}" ({}) VALUES ({})'.format(table, columns, values)

        queryInsert = QSqlQuery(self.devDB)
        queryInsert.prepare(queryInsertCmd)
        if not queryInsert.exec():
            self.textDBStatus.setText(
                "{}".format(queryInsert.lastError().databaseText())
            )
        else:
            self.textDBStatus.setText(
                "Vložení nového záznamu do tabulky {} proběhlo úspěšně!".format(table)
            )

    def selectFromTable(self):
        columns = self.lineEditSelectColumns.text()
        table = self.comboBoxTableViewed.currentText()
        condition = self.lineEditSelectCondition.text()
        limit = self.lineEditSelectLimit.text()

        querySelectCmd = "SELECT "
        if not columns:
            querySelectCmd += '* FROM "{}"'.format(table)
        else:
            querySelectCmd += '{} FROM "{}"'.format(columns, table)
        if condition:
            querySelectCmd += " WHERE {}".format(condition)
        if limit:
            querySelectCmd += " LIMIT {}".format(limit)

        self.querySelect = QSqlQuery(self.devDB)
        self.querySelect.prepare(querySelectCmd)
        if not self.querySelect.exec():
            self.textDBStatus.setText(
                "{}".format(self.querySelect.lastError().databaseText())
            )
        else:
            self.textDBStatus.setText(
                "Výběr záznamů z tabulky {} proběhlo úspěšně!\n".format(table)
                + "Bylo vybráno {} záznamů.".format(self.querySelect.size())
            )

        self.SQLQueryModel.setQuery(self.querySelect)

    def updateTableRecords(self):
        queryUpdate = QSqlQuery(self.devDB)
        table = self.comboBoxTableViewed.currentText()
        columns = self.lineEditUpdateColumns.text()
        values = self.lineEditUpdateValues.text()
        condition = self.lineEditUpdateCondition.text()

        if not queryUpdate.exec(
            "UPDATE {} SET ({}) = ({}) WHERE {}".format(
                table, columns, values, condition
            )
        ):
            self.textDBStatus.setText(
                "{}".format(queryUpdate.lastError().databaseText())
            )
        else:
            self.textDBStatus.setText(
                "Aktualizace záznamů z tabulky {} proběhlo úspěšně!\n".format(table)
                + "Bylo aktualizováno {} záznamů.".format(queryUpdate.numRowsAffected())
            )

    def deleteTableRecords(self):
        queryDelete = QSqlQuery(self.devDB)
        table = self.comboBoxTableViewed.currentText()
        condition = self.lineEditDeleteCondition.text()

        if not queryDelete.exec("DELETE FROM {} WHERE {}".format(table, condition)):
            self.textDBStatus.setText(
                "{}".format(queryDelete.lastError().databaseText())
            )
        else:
            self.textDBStatus.setText(
                "Odstranění záznamů z tabulky {} proběhlo úspěšně!\n".format(table)
                + "Bylo odebráno {} záznamů.".format(queryDelete.numRowsAffected())
            )

    def lineEditContentChanged(self):
        sender = self.sender()
        font = QFont("", 0)
        fm = QFontMetrics(font)

        text = sender.text()
        newWidth = int(fm.boundingRect(text).width() * 0.8)
        if newWidth > self._lineEditminWidth:
            sender.setFixedWidth(newWidth)
        else:
            sender.setMinimumWidth(self._lineEditminWidth)
