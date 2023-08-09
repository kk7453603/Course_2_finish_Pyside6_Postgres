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
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.refresh()
        self.last_row=0
        self.ui.pushButton_3.clicked.connect(self.save)
        self.ui.pushButton.clicked.connect(self.add_row)
        self.ui.pushButton_2.clicked.connect(self.del_row)
        self.ui.tableWidget.itemChanged.connect(self.changed_item)

    def refresh(self):
            conn = psycopg2.connect(host=host, user=user, password=password, database=db_name)
            with conn.cursor() as curs:
                curs.execute("SELECT * FROM Films;")
                res = curs.fetchall()
                self.ui.tableWidget.setRowCount(len(res))
                for i in range(len(["FilmName","Genr","Year","Cost"])):
                    self.ui.tableWidget.insertColumn(i)
                self.ui.tableWidget.setHorizontalHeaderLabels(["FilmName","Genr","Year","Cost"])
                print(res)
                for row_number,row_data in enumerate(res):
                    self.last_row=row_number
                    print(row_number,row_data)
                    print()
                    #self.ui.tableWidget.insertRow(row_number)

                    #self.ui.tableWidget.insertColumn(1)
                    for column_number,data in enumerate(row_data[1:]):
                        self.ui.tableWidget.setItem(row_number,column_number,QTableWidgetItem(str(data)))

                        self.ui.tableWidget.resizeColumnsToContents()
                        #print(column_number,data)
                        #print("----------------------")

            if conn:
                conn.close()

    def add_row(self):
        rowPosition=self.ui.tableWidget.rowCount()
        self.ui.tableWidget.insertRow(rowPosition)


    def del_row(self):
        rowPosition=self.ui.tableWidget.rowCount()
        if rowPosition == 0:
            QMessageBox.warning(self,"Внимание","Нельзя удалять первую строку")
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
                curs.execute(f"DELETE FROM Films WHERE film_name='{self.ui.tableWidget.item(rowPosition-1, 0).text()}' AND genres='{self.ui.tableWidget.item(rowPosition-1, 1).text()}' AND year_of='{self.ui.tableWidget.item(rowPosition-1, 2).text()}'")
                conn.commit()
            self.ui.tableWidget.removeRow(rowPosition-1)

    def save(self):
        conn = psycopg2.connect(host=host, user=user, password=password, database=db_name)
        with conn.cursor() as curs:
            for row in range(self.ui.tableWidget.rowCount()):
                curs.execute(f"SELECT film_id FROM Films WHERE film_name='{self.ui.tableWidget.item(row, 0).text()}';")
                res = curs.fetchone()
                if res:
                    curs.execute(
                        f"UPDATE Films SET film_name='{self.ui.tableWidget.item(row, 0).text()}',genres='{self.ui.tableWidget.item(row, 1).text()}',year_of='{self.ui.tableWidget.item(row, 2).text()}', cost_for_watch='{self.ui.tableWidget.item(row, 3).text()}' WHERE film_id={res[0]};")
                    conn.commit()
                else:
                    curs.execute(
                        f"INSERT INTO Films (film_name,genres,year_of,cost_for_watch) VALUES ('{self.ui.tableWidget.item(row, 0).text()}','{self.ui.tableWidget.item(row, 1).text()}','{self.ui.tableWidget.item(row, 2).text()}','{self.ui.tableWidget.item(row, 3).text()}');")
                    conn.commit()

            #curs.execute("SELECT * FROM Users;")
            #res = curs.fetchall()
            #for row_number,row_data in enumerate(res):
            #    for column_number, data in enumerate(row_data[1:]):
            #        User_id = row_data[0]
            #        tbl_value=self.ui.tableWidget.item(row_number, column_number)
                    #if row_number<len(res): #id check
            #        info = tbl_value.text()
            #        if data==tbl_value.text() and tbl_value.text()!="":
            #            curs.execute(f"UPDATE Users SET first_name='{self.ui.tableWidget.item(row_number, 0).text()}',last_name='{self.ui.tableWidget.item(row_number, 1).text()}',email='{self.ui.tableWidget.item(row_number, 2).text()}', age='{self.ui.tableWidget.item(row_number, 3).text()}' WHERE id={User_id};")
            #            conn.commit()
            #        else:
             #           curs.execute(f"INSERT INTO Users (first_name,last_name,email,age) VALUES ('{self.ui.tableWidget.item(row_number, 0).text()}','{self.ui.tableWidget.item(row_number, 1).text()}','{self.ui.tableWidget.item(row_number, 2).text()}','{self.ui.tableWidget.item(row_number, 3).text()}');")
             #           conn.commit()






            #QTableWidgetItem.setText()

    def changed_item(self,item):
        print(item.text(),item.column())
        txt=item.text()
        col=item.column()
        if (col==3) and not (txt.isdigit()):
            item.setText("20")

if __name__ == '__main__':
    app=QApplication(sys.argv)
    window = TableEdit()
    window.show()
    app.exec()