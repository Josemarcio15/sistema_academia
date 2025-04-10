# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
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
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(562, 600)
        self.button_login = QPushButton(Widget)
        self.button_login.setObjectName(u"button_login")
        self.button_login.setGeometry(QRect(210, 310, 141, 25))
        self.campo_password = QLineEdit(Widget)
        self.campo_password.setObjectName(u"campo_password")
        self.campo_password.setGeometry(QRect(210, 270, 142, 25))
        self.label_2 = QLabel(Widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(150, 270, 46, 17))
        self.campo_id = QLineEdit(Widget)
        self.campo_id.setObjectName(u"campo_id")
        self.campo_id.setGeometry(QRect(210, 230, 142, 25))
        self.label = QLabel(Widget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(140, 230, 56, 17))

        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Widget", None))
        self.button_login.setText(QCoreApplication.translate("Widget", u"Login", None))
        self.label_2.setText(QCoreApplication.translate("Widget", u"Senha:", None))
        self.label.setText(QCoreApplication.translate("Widget", u"Usuario:", None))
    # retranslateUi

