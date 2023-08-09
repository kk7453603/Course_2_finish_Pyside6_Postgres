import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import *
from PySide6 import QtSql, QtWidgets
import psycopg2
host = "127.0.0.1"
user = "postgres"
password = "Maxim2007"
db_name = "test"


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

    #def add_Combo(self):


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w=MainWindow()
    combo = QComboBox()
    conn = psycopg2.connect(host=host, user=user, password=password, database=db_name)
    with conn.cursor() as curs:
        curs.execute("SELECT first_name FROM Users")
        res = curs.fetchall()
        ms=[i[0] for i in res]
        print(res, ms)
    combo.addItems(ms)
    w.setCentralWidget(combo)
    w.show()
    app.exec()

