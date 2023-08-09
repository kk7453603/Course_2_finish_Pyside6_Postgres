import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import *
from PySide6 import QtSql, QtWidgets
from Cost_calculate_widget import Ui_Dialog
import psycopg2
host = "127.0.0.1"
user = "postgres"
password = "Maxim2007"
db_name = "test"

class Cost_calculate_widget(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.get_Users()
        self.ui.user_box.currentIndexChanged.connect(self.get_Users_info)

    def get_Users(self):
        conn = psycopg2.connect(host=host, user=user, password=password, database=db_name)
        with conn.cursor() as curs:
            curs.execute("SELECT DISTINCT first_name,last_name FROM full_purchase; ")
            res = curs.fetchall()
            self.ui.user_box.addItems([str(el[0])+" "+str(el[1]) for el in res])

    def get_Users_info(self, item_id):
        fn,ln = self.ui.user_box.itemText(item_id).split()
        conn = psycopg2.connect(host=host, user=user, password=password, database=db_name)
        with conn.cursor() as curs:
            curs.execute(f"SELECT ret_cost_for_user('{fn}','{ln}');")
            res = curs.fetchone()
            self.ui.dolg.setText(str(res[0]))
            print(res)
            curs.execute(f'''SELECT us.first_name,us.last_name,pr.purchase_status,MIN(od.date_of_return),fl.film_name FROM purchase pr JOIN Users us ON us.id=pr.userid JOIN order_details od ON pr.orderid=od.order_id JOIN Films fl ON pr.filmid=fl.film_id
WHERE first_name='{fn}' AND last_name='{ln}' GROUP BY us.first_name,us.last_name,pr.purchase_status,fl.film_name HAVING pr.purchase_status=false  ''')
            res = curs.fetchone()
            print(res)
            if res:
                self.ui.date_lost.setDate(res[3])
                self.ui.last_film.setText(res[4])
            else:
                self.ui.last_film.setText("Нет")


if __name__ == '__main__':
    app=QApplication(sys.argv)
    window = Cost_calculate_widget()
    window.show()
    app.exec()