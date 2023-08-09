# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Cost_calculate_widget.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QDialog,
    QFormLayout, QLabel, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(421, 342)
        self.verticalLayoutWidget_2 = QWidget(Dialog)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(60, 70, 331, 141))
        self.verticalLayout_2 = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.verticalLayoutWidget_2)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        self.user_box = QComboBox(self.verticalLayoutWidget_2)
        self.user_box.setObjectName(u"user_box")

        self.verticalLayout.addWidget(self.user_box)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.label_2 = QLabel(self.verticalLayoutWidget_2)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_2)

        self.dolg = QLabel(self.verticalLayoutWidget_2)
        self.dolg.setObjectName(u"dolg")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.dolg)

        self.label_4 = QLabel(self.verticalLayoutWidget_2)
        self.label_4.setObjectName(u"label_4")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_4)

        self.date_lost = QDateEdit(self.verticalLayoutWidget_2)
        self.date_lost.setObjectName(u"date_lost")
        self.date_lost.setEnabled(True)
        self.date_lost.setReadOnly(True)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.date_lost)

        self.label_5 = QLabel(self.verticalLayoutWidget_2)
        self.label_5.setObjectName(u"label_5")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_5)

        self.last_film = QLabel(self.verticalLayoutWidget_2)
        self.last_film.setObjectName(u"last_film")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.last_film)


        self.verticalLayout.addLayout(self.formLayout)


        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"\u041f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044c", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"\u0417\u0430\u0434\u043e\u043b\u0436\u0435\u043d\u043d\u043e\u0441\u0442\u044c", None))
        self.dolg.setText(QCoreApplication.translate("Dialog", u"0", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"\u0411\u043b\u0438\u0436\u0430\u0439\u0448\u0438\u0439 \u0441\u0440\u043e\u043a \u0441\u0434\u0430\u0447\u0438 \u0444\u0438\u043b\u044c\u043c\u0430", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"\u0424\u0438\u043b\u044c\u043c \u0441 \u0438\u0441\u0442\u0435\u043a\u0430\u044e\u0449\u0438\u043c \u0441\u0440\u043e\u043a\u043e\u043c \u0430\u0440\u0435\u043d\u0434\u044b", None))
        self.last_film.setText(QCoreApplication.translate("Dialog", u"\u041d\u0435\u0442", None))
    # retranslateUi

