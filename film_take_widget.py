import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import *
from PySide6 import QtSql, QtWidgets
from film_take import Ui_Dialog
import psycopg2
host = "127.0.0.1"
user = "postgres"
password = "Maxim2007"
db_name = "test"

class Film_take_widget(QDialog):
    def __init__(self):
        super().__init__()
        self.ui=Ui_Dialog()
        self.ui.setupUi(self)
        self.get_clients()
        self.ui.deal_btn.clicked.connect(self.close_deal)

    def get_clients(self):
        self.ui.client_name_line.clear()
        self.ui.film_change.clear()
        conn = psycopg2.connect(host=host, user=user, password=password, database=db_name)
        with conn.cursor() as curs:
            curs.execute("SELECT first_name,last_name,film_name FROM full_purchase WHERE purchase_status = False; ")
            res = curs.fetchall()
            print(res)
            user_names=[(el[0]+" "+el[1]) for el in res]
            film_names=[el[2] for el in res]
            self.ui.client_name_line.addItems(user_names)
            self.ui.film_change.addItems(film_names)

    def close_deal(self):
        fn,ln=self.ui.client_name_line.currentText().split()
        film=self.ui.film_change.currentText()
        conn = psycopg2.connect(host=host, user=user, password=password, database=db_name)
        with conn.cursor() as curs:
            curs.execute(f"UPDATE full_purchase SET purchase_status=true WHERE first_name='{fn}' AND last_name='{ln}' AND film_name='{film}'");
            conn.commit()
        self.get_clients()


if __name__ == '__main__':
    app=QApplication(sys.argv)
    window = Film_take_widget()
    window.show()
    app.exec()