# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'film_take.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QFormLayout,
    QLabel, QPushButton, QSizePolicy, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(458, 379)
        self.formLayoutWidget = QWidget(Dialog)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(140, 100, 231, 81))
        self.formLayout = QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.formLayoutWidget)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.label_2 = QLabel(self.formLayoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.film_change = QComboBox(self.formLayoutWidget)
        self.film_change.setObjectName(u"film_change")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.film_change)

        self.deal_btn = QPushButton(self.formLayoutWidget)
        self.deal_btn.setObjectName(u"deal_btn")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.deal_btn)

        self.Cancel_btn = QPushButton(self.formLayoutWidget)
        self.Cancel_btn.setObjectName(u"Cancel_btn")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.Cancel_btn)

        self.client_name_line = QComboBox(self.formLayoutWidget)
        self.client_name_line.setObjectName(u"client_name_line")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.client_name_line)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"\u041a\u043b\u0438\u0435\u043d\u0442", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"\u0424\u0438\u043b\u044c\u043c", None))
        self.deal_btn.setText(QCoreApplication.translate("Dialog", u"\u0417\u0430\u043a\u0440\u044b\u0442\u044c \u0441\u0434\u0435\u043b\u043a\u0443", None))
        self.Cancel_btn.setText(QCoreApplication.translate("Dialog", u"\u041e\u0442\u043c\u0435\u043d\u0430", None))
    # retranslateUi

