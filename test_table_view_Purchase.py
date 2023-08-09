import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import *
from PySide6 import QtSql, QtWidgets
from PySide6.QtSql import QSqlDatabase
from Users_widget import Ui_Form
import psycopg2

host = "127.0.0.1"
user = "postgres"
password = "Maxim2007"
db_name = "test"


class TableEdit(QDialog):
    def __init__(self):
        super(TableEdit, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.refresh()
        self.last_row = 0
        self.User_names = []
        self.Order_dates = []
        self.Film_names = []
        self.User_names_sl = {}
        self.Order_dates_sl = {}
        self.Film_names_sl = {}
        self.ui.pushButton_3.clicked.connect(self.save)
        self.ui.pushButton.clicked.connect(self.add_row)
        self.ui.pushButton_2.clicked.connect(self.del_row)
        self.ui.tableWidget.itemChanged.connect(self.changed_item)

    def prepare_table(self):
        conn = psycopg2.connect(host=host, user=user, password=password, database=db_name)
        with conn.cursor() as curs:
            curs.execute("SELECT id,first_name,last_name FROM Users")
            res = curs.fetchall()
            self.User_names = []
            self.User_names_sl={}
            for el in res:
                self.User_names.append([(el[1] + el[2]), el[0]])
                self.User_names_sl.update({(el[1] + el[2]):el[0]})
            curs.execute("SELECT order_id,date_of_return FROM Order_details")
            res = curs.fetchall()
            self.Order_dates = []
            self.Order_dates_sl={}
            for el in res:
                self.Order_dates.append([str(el[1]), el[0]])
                self.Order_dates_sl.update({str(el[1]):el[0]})
            curs.execute("SELECT film_name,film_id FROM Films")
            res = curs.fetchall()
            self.Film_names = []
            self.Film_names_sl={}
            for el in res:
                self.Film_names.append([el[0], el[1]])
                self.Film_names_sl.update({el[0]:el[1]})
            print(self.Film_names_sl)
            print(self.Order_dates_sl)

    def refresh(self):
        self.prepare_table()
        conn = psycopg2.connect(host=host, user=user, password=password, database=db_name)
        with conn.cursor() as curs:
            curs.execute("SELECT * FROM Purchase;")
            res = curs.fetchall()
            self.ui.tableWidget.setRowCount(len(res))
            for i in range(len(["User", "Order", "Film", "Status"])):
                self.ui.tableWidget.insertColumn(i)
            self.ui.tableWidget.setHorizontalHeaderLabels(["User", "Order", "Film", "Status"])
            print(res)
            for row_number, row_data in enumerate(res):
                self.last_row = row_number
                print(row_number, row_data)
                print()
                # self.ui.tableWidget.insertRow(row_number)

                # self.ui.tableWidget.insertColumn(1)
                for column_number, data in enumerate(row_data[1:]):
                    cmb = QComboBox()
                    if column_number == 0:
                        cmb.addItems([i[0] for i in self.User_names])
                    elif column_number == 1:
                        cmb.addItems([i[0] for i in self.Order_dates])
                    elif column_number == 2:
                        cmb.addItems([i[0] for i in self.Film_names])
                    elif column_number == 3:
                        cmb.addItems(['0', '1'])
                    self.ui.tableWidget.setCellWidget(row_number, column_number, cmb)

                    self.ui.tableWidget.resizeColumnsToContents()
                    # print(column_number,data)
                    # print("----------------------")

        if conn:
            conn.close()

    def add_row(self):
        self.prepare_table()
        rowPosition = self.ui.tableWidget.rowCount()
        self.ui.tableWidget.insertRow(rowPosition)
        for i in range(self.ui.tableWidget.columnCount()):
            cmb = QComboBox()
            if i == 0:
                cmb.addItems([i[0] for i in self.User_names])
            elif i == 1:
                cmb.addItems([i[0] for i in self.Order_dates])
            elif i == 2:
                cmb.addItems([i[0] for i in self.Film_names])
            elif i == 3:
                cmb.addItems(['0', '1'])

            print(self.User_names)
            self.ui.tableWidget.setCellWidget(rowPosition, i, cmb)


    def del_row(self):
        rowPosition = self.ui.tableWidget.rowCount()
        if rowPosition == 0:
            QMessageBox.warning(self, "Внимание", "Нельзя удалять первую строку")
            return
        elif rowPosition == -1:
            msg = QMessageBox.question(
                self,
                'Message',
                "Выберите строку, которую вы хотите удалить.",
                QMessageBox.Ok
            )
            return
        else:
            msg = QMessageBox.question(
                self,
                "Внимание подтвердите удаление строки!",
                "Вы действительно хотите удалить "
                f"строку <b style='color: red;'>{rowPosition}</b> ?",
                QMessageBox.Ok | QMessageBox.Cancel
            )
            if msg == QtWidgets.QMessageBox.Cancel:
                return

            conn = psycopg2.connect(host=host, user=user, password=password, database=db_name)
            with conn.cursor() as curs:
                curs.execute(
                    f"DELETE FROM Purchase WHERE userid='{self.User_names_sl[self.ui.tableWidget.cellWidget(rowPosition - 1, 0).currentText()]}' AND orderid='{self.Order_dates_sl[self.ui.tableWidget.cellWidget(rowPosition - 1, 1).currentText()]}' AND filmid='{self.Film_names_sl[self.ui.tableWidget.cellWidget(rowPosition - 1, 2).currentText()]}'")
                conn.commit()
            self.ui.tableWidget.removeRow(rowPosition - 1)

    def save(self):
        conn = psycopg2.connect(host=host, user=user, password=password, database=db_name)
        with conn.cursor() as curs:
            for row in range(self.ui.tableWidget.rowCount()):
                curs.execute(
                    f"SELECT purchase_id FROM Purchase WHERE userid='{self.User_names_sl[self.ui.tableWidget.cellWidget(row, 0).currentText()]}' AND orderid='{self.Order_dates_sl[self.ui.tableWidget.cellWidget(row, 1).currentText()]}' AND filmid='{self.Film_names_sl[self.ui.tableWidget.cellWidget(row, 2).currentText()]}';")
                res = curs.fetchone()
                if res:
                    curs.execute(
                        f"UPDATE Purchase SET userid='{self.User_names_sl[self.ui.tableWidget.cellWidget(row, 0).currentText()]}',orderid='{self.Order_dates_sl[self.ui.tableWidget.cellWidget(row, 1).currentText()]}',filmid='{self.Film_names_sl[self.ui.tableWidget.cellWidget(row, 2).currentText()]}' WHERE purchase_id='{res[0]}';")
                    conn.commit()
                else:
                    curs.execute(
                        f"INSERT INTO Purchase (userid,orderid,filmid) VALUES ('{self.User_names_sl[self.ui.tableWidget.cellWidget(row, 0).currentText()]}','{self.Order_dates_sl[self.ui.tableWidget.cellWidget(row, 1).currentText()]}','{self.Film_names_sl[self.ui.tableWidget.cellWidget(row, 2).currentText()]}');")
                    conn.commit()

            # curs.execute("SELECT * FROM Users;")
            # res = curs.fetchall()
            # for row_number,row_data in enumerate(res):
            #    for column_number, data in enumerate(row_data[1:]):
            #        User_id = row_data[0]
            #        tbl_value=self.ui.tableWidget.item(row_number, column_number)
            # if row_number<len(res): #id check
            #        info = tbl_value.text()
            #        if data==tbl_value.text() and tbl_value.text()!="":
            #            curs.execute(f"UPDATE Users SET first_name='{self.ui.tableWidget.item(row_number, 0).text()}',last_name='{self.ui.tableWidget.item(row_number, 1).text()}',email='{self.ui.tableWidget.item(row_number, 2).text()}', age='{self.ui.tableWidget.item(row_number, 3).text()}' WHERE id={User_id};")
            #            conn.commit()
            #        else:
            #           curs.execute(f"INSERT INTO Users (first_name,last_name,email,age) VALUES ('{self.ui.tableWidget.item(row_number, 0).text()}','{self.ui.tableWidget.item(row_number, 1).text()}','{self.ui.tableWidget.item(row_number, 2).text()}','{self.ui.tableWidget.item(row_number, 3).text()}');")
            #           conn.commit()

            # QTableWidgetItem.setText()

    def changed_item(self, item):
        print(item.text(), item.column())
        # txt=item.text()
        # col=item.column()
        # if (col==3) and not (txt.isdigit()):
        # item.setText("20")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = TableEdit()
    window.show()
    app.exec()
