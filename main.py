import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import *
from Main_w import Ui_MainWindow
from conn import Ui_Dialog
from add_purchase import Ui_Form
from Users_widget import Ui_Form as f2
from test_table_view_Users import TableEdit as UserEdit
from test_table_view_films import TableEdit as FilmEdit
from test_table_view_Purchase import TableEdit as PurchaseEdit
from film_take_widget import Film_take_widget
from Cost_calculate_widget_View import Cost_calculate_widget
from test_table_view_Order_Details import TableEdit as OrderDetEdit
import psycopg2
login = None
passwd = None
host = "127.0.0.1"
user = "bd_admin"
password = "main_user"
db_name = "test"

class Change_Users(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = f2()
        self.ui.setupUi(self)
        # self.ui.tableView.


class AddPurchase(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.accept_btn.clicked.connect(self.add_film_in_purch)
        self.ui.ch_film.currentIndexChanged.connect(self.get_cost)
        self.get_users()

    def add_film_in_purch(self):
        try:
            conn = psycopg2.connect(host="127.0.0.1", user="postgres", password="Maxim2007", database="test")
            with conn.cursor() as curs:
                # curs.execute("INSERT INTO order_details (date_of_issue,date_of_return) VALUES (current_date, current_date+7);")
                # conn.commit()
                # curs.execute("SELECT order_id FROM order_details WHERE date_of_issue=current_date AND date_of_return=(current_date+7);")
                # order_id = curs.fetchone()[0]
                fn, ln = self.ui.ch_user.currentText().split()
                curs.execute(f"SELECT id FROM Users WHERE first_name='{fn}' AND last_name='{ln}';")
                user_id = curs.fetchone()[0]
                curs.execute(f"SELECT film_id FROM Films WHERE film_name='{self.ui.ch_film.currentText()}'")
                film_id = curs.fetchone()[0]
                curs.execute(
                    f"INSERT INTO purchase (userid,orderid,filmid,purchase_status) VALUES ({user_id},{1},{film_id},{False});")
                conn.commit()
        except Exception as ex:
            print(ex)
        finally:
            print()
            if conn:
                conn.close()

    def get_cost(self, index):
        cmb_value = self.ui.ch_film.itemText(index)
        try:
            conn = psycopg2.connect(host="127.0.0.1", user="bd_admin", password="main_user", database="test")
            with conn.cursor() as curs:
                curs.execute(f"SELECT cost_for_watch FROM Films WHERE film_name='{cmb_value}'")

                res = curs.fetchone()
                print(res)
                self.ui.price_for_film.setText(str(res[0]))
        except Exception as ex:
            print(ex)
        finally:
            print()
            if conn:
                conn.close()

    def get_users(self):
        try:
            conn = psycopg2.connect(host="127.0.0.1", user="bd_admin", password="main_user", database="test")
            with conn.cursor() as curs:
                curs.execute("SELECT first_name,last_name FROM Users")

                res = curs.fetchall()
                for el in res:
                    self.ui.ch_user.addItem(el[0] + ' ' + el[1])
        except Exception as ex:
            print(ex)
        finally:
            print()
            if conn:
                conn.close()


class ConnDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.collect_info)
        self.conn_status = False
        #self.login = None
        #self.paswd = None

    def collect_info(self):
        global login,passwd
        #self.login = self.ui.lineEdit_3.text()
        #self.paswd = self.ui.lineEdit_4.text()
        login = self.ui.lineEdit_3.text()
        passwd = self.ui.lineEdit_4.text()
        self.conn_db()

    def conn_db(self):
        try:
            conn = psycopg2.connect(host="127.0.0.1", user=login, password=passwd, database='test')
            with conn.cursor() as curs:
                curs.execute("Select version();")
                print(curs.fetchone())
        except Exception as ex:
            print(ex)
        finally:
            if conn:
                conn.close()
                print("closed")
                self.close()
                self.conn_status = True


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.cd = None
        self.purchase_windows = None
        self.user_window = None
        self.purchase_window = None
        self.film_window = None
        self.close_purch_window = None
        self.cost_calculate_window = None
        self.order_details_window = None
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.connect_2.triggered.connect(self.open_dia)
        self.ui.action.triggered.connect(self.check_conn_data)
        self.ui.give_film_btn.clicked.connect(self.open_AddPurchase)
        self.ui.user_ank.triggered.connect(self.open_Users_View)
        self.ui.film_ank.triggered.connect(self.open_Films_View)
        self.ui.purchase_ank.triggered.connect(self.open_Purchase_View)
        self.ui.take_film_btn.clicked.connect(self.open_Film_Take_View)
        self.ui.cost_calc_btn.clicked.connect(self.open_Cost_Calculate_View)
        self.ui.order_det_ank.triggered.connect(self.open_Order_Details_View)

    def open_dia(self):
        if self.cd is None:
            self.cd = ConnDialog()
        self.cd.show()

    def check_conn_data(self):
        print(self.cd.address)  # данные подключения

    def open_AddPurchase(self):
        if self.purchase_windows is None:
            self.purchase_windows = AddPurchase()
            conn = None
            try:
                conn = psycopg2.connect(host="127.0.0.1", user=login, password=password,
                                        database=db_name)
                with conn.cursor() as curs:
                    curs.execute("SELECT film_name FROM Films;")
                    res = curs.fetchall()
                    print(res)
                    self.purchase_windows.film_names = [i[0] for i in res]
            except Exception as ex:
                print(ex)
            finally:
                if conn:
                    conn.close()
                    print("closed")
                    self.conn_status = True
                    self.purchase_windows.ui.ch_film.addItems([i[0] for i in res])
        self.purchase_windows.show()

    def open_Users_View(self):
        if self.user_window is None:
            self.user_window = UserEdit()
        self.user_window.show()

    def open_Films_View(self):
        if self.film_window is None:
            self.film_window = FilmEdit()
        self.film_window.show()

    def open_Purchase_View(self):
        if self.purchase_window is None:
            self.purchase_window = PurchaseEdit()
        self.purchase_window.show()

    def open_Film_Take_View(self):
        if self.close_purch_window is None:
            self.close_purch_window = Film_take_widget()
        self.close_purch_window.show()

    def open_Cost_Calculate_View(self):
        if self.cost_calculate_window is None:
            self.cost_calculate_window = Cost_calculate_widget()
        self.cost_calculate_window.show()

    def open_Order_Details_View(self):
        if self.order_details_window is None:
            self.order_details_window = OrderDetEdit()
        self.order_details_window.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()

    app.exec()
