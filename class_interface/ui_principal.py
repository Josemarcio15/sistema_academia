# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'principal.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QLabel,
    QLayout, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QStackedWidget, QWidget)

class Ui_Home(object):
    def setupUi(self, Home):
        if not Home.objectName():
            Home.setObjectName(u"Home")
        Home.setWindowModality(Qt.WindowModal)
        Home.setEnabled(True)
        Home.resize(1119, 881)
        Home.setWindowTitle(u"SysMar")
        self.gridLayout_2 = QGridLayout(Home)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setSizeConstraint(QLayout.SetNoConstraint)
        self.gridLayout_2.setContentsMargins(9, -1, -1, -1)
        self.stackedWidget = QStackedWidget(Home)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.pushButton = QPushButton(self.page)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(100, 40, 89, 25))
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.gridLayout_3 = QGridLayout(self.page_2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.verticalSpacer_4 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)

        self.gridLayout_3.addItem(self.verticalSpacer_4, 7, 0, 1, 1)

        self.lineEdit_2 = QLineEdit(self.page_2)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.gridLayout_3.addWidget(self.lineEdit_2, 6, 0, 1, 1)

        self.gridLayout_7 = QGridLayout()
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.lineEdit_7 = QLineEdit(self.page_2)
        self.lineEdit_7.setObjectName(u"lineEdit_7")
        self.lineEdit_7.setMaximumSize(QSize(100, 16777215))

        self.gridLayout_7.addWidget(self.lineEdit_7, 0, 0, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_7.addItem(self.horizontalSpacer_2, 0, 1, 1, 1)


        self.gridLayout_3.addLayout(self.gridLayout_7, 9, 0, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)

        self.gridLayout_3.addItem(self.verticalSpacer_3, 4, 0, 1, 1)

        self.lineEdit_3 = QLineEdit(self.page_2)
        self.lineEdit_3.setObjectName(u"lineEdit_3")

        self.gridLayout_3.addWidget(self.lineEdit_3, 3, 1, 1, 1)

        self.label_11 = QLabel(self.page_2)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout_3.addWidget(self.label_11, 8, 1, 1, 1)

        self.label_2 = QLabel(self.page_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(85, 113))
        self.label_2.setMaximumSize(QSize(85, 113))
        self.label_2.setStyleSheet(u"background-color: rgb(153, 193, 241);")
        self.label_2.setTextFormat(Qt.AutoText)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.label_2, 1, 0, 1, 1)

        self.lineEdit_5 = QLineEdit(self.page_2)
        self.lineEdit_5.setObjectName(u"lineEdit_5")

        self.gridLayout_3.addWidget(self.lineEdit_5, 6, 2, 1, 1)

        self.label_12 = QLabel(self.page_2)
        self.label_12.setObjectName(u"label_12")

        self.gridLayout_3.addWidget(self.label_12, 8, 2, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer_2, 14, 0, 1, 1)

        self.comboBox = QComboBox(self.page_2)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setMaximumSize(QSize(110, 16777215))

        self.gridLayout_3.addWidget(self.comboBox, 3, 2, 1, 1)

        self.verticalSpacer_5 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)

        self.gridLayout_3.addItem(self.verticalSpacer_5, 11, 1, 1, 1)

        self.lineEdit_9 = QLineEdit(self.page_2)
        self.lineEdit_9.setObjectName(u"lineEdit_9")

        self.gridLayout_3.addWidget(self.lineEdit_9, 9, 2, 1, 1)

        self.label_7 = QLabel(self.page_2)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_3.addWidget(self.label_7, 2, 1, 1, 1)

        self.label_4 = QLabel(self.page_2)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_3.addWidget(self.label_4, 5, 0, 1, 1)

        self.lineEdit_8 = QLineEdit(self.page_2)
        self.lineEdit_8.setObjectName(u"lineEdit_8")

        self.gridLayout_3.addWidget(self.lineEdit_8, 9, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer, 0, 1, 1, 1)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.lineEdit_4 = QLineEdit(self.page_2)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setMaximumSize(QSize(60, 16777215))

        self.gridLayout.addWidget(self.lineEdit_4, 0, 0, 1, 1)

        self.lineEdit_6 = QLineEdit(self.page_2)
        self.lineEdit_6.setObjectName(u"lineEdit_6")

        self.gridLayout.addWidget(self.lineEdit_6, 0, 1, 1, 1)


        self.gridLayout_3.addLayout(self.gridLayout, 6, 1, 1, 1)

        self.label = QLabel(self.page_2)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(20)
        self.label.setFont(font)

        self.gridLayout_3.addWidget(self.label, 0, 0, 1, 1)

        self.label_8 = QLabel(self.page_2)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_3.addWidget(self.label_8, 2, 2, 1, 1)

        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.label_6 = QLabel(self.page_2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMaximumSize(QSize(60, 16777215))

        self.gridLayout_5.addWidget(self.label_6, 0, 0, 1, 1)

        self.label_9 = QLabel(self.page_2)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout_5.addWidget(self.label_9, 0, 1, 1, 1)


        self.gridLayout_3.addLayout(self.gridLayout_5, 5, 1, 1, 1)

        self.label_5 = QLabel(self.page_2)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_3.addWidget(self.label_5, 5, 2, 1, 1)

        self.lineEdit = QLineEdit(self.page_2)
        self.lineEdit.setObjectName(u"lineEdit")

        self.gridLayout_3.addWidget(self.lineEdit, 3, 0, 1, 1)

        self.pushButton_2 = QPushButton(self.page_2)
        self.pushButton_2.setObjectName(u"pushButton_2")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        self.pushButton_2.setMinimumSize(QSize(0, 40))
        self.pushButton_2.setMaximumSize(QSize(200, 40))

        self.gridLayout_3.addWidget(self.pushButton_2, 12, 1, 1, 1)

        self.label_3 = QLabel(self.page_2)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_3.addWidget(self.label_3, 2, 0, 1, 1)

        self.label_10 = QLabel(self.page_2)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout_3.addWidget(self.label_10, 8, 0, 1, 1)

        self.pushButton_3 = QPushButton(self.page_2)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setMinimumSize(QSize(0, 40))
        self.pushButton_3.setMaximumSize(QSize(200, 16777215))

        self.gridLayout_3.addWidget(self.pushButton_3, 13, 1, 1, 1)

        self.stackedWidget.addWidget(self.page_2)

        self.gridLayout_2.addWidget(self.stackedWidget, 0, 1, 6, 1)

        self.button_bar_configuracoes = QPushButton(Home)
        self.button_bar_configuracoes.setObjectName(u"button_bar_configuracoes")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.button_bar_configuracoes.sizePolicy().hasHeightForWidth())
        self.button_bar_configuracoes.setSizePolicy(sizePolicy1)
        self.button_bar_configuracoes.setMinimumSize(QSize(0, 0))
        self.button_bar_configuracoes.setMaximumSize(QSize(500, 100))
        self.button_bar_configuracoes.setSizeIncrement(QSize(0, 0))

        self.gridLayout_2.addWidget(self.button_bar_configuracoes, 4, 0, 1, 1)

        self.button_bar_inicio = QPushButton(Home)
        self.button_bar_inicio.setObjectName(u"button_bar_inicio")
        sizePolicy1.setHeightForWidth(self.button_bar_inicio.sizePolicy().hasHeightForWidth())
        self.button_bar_inicio.setSizePolicy(sizePolicy1)
        self.button_bar_inicio.setMinimumSize(QSize(0, 0))
        self.button_bar_inicio.setMaximumSize(QSize(500, 100))
        self.button_bar_inicio.setSizeIncrement(QSize(0, 0))

        self.gridLayout_2.addWidget(self.button_bar_inicio, 0, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer, 5, 0, 1, 1)

        self.button_bar_cadastrar = QPushButton(Home)
        self.button_bar_cadastrar.setObjectName(u"button_bar_cadastrar")
        sizePolicy1.setHeightForWidth(self.button_bar_cadastrar.sizePolicy().hasHeightForWidth())
        self.button_bar_cadastrar.setSizePolicy(sizePolicy1)
        self.button_bar_cadastrar.setMinimumSize(QSize(0, 0))
        self.button_bar_cadastrar.setMaximumSize(QSize(500, 100))
        self.button_bar_cadastrar.setSizeIncrement(QSize(0, 0))

        self.gridLayout_2.addWidget(self.button_bar_cadastrar, 1, 0, 1, 1)

        self.button_bar_cobranca = QPushButton(Home)
        self.button_bar_cobranca.setObjectName(u"button_bar_cobranca")
        sizePolicy1.setHeightForWidth(self.button_bar_cobranca.sizePolicy().hasHeightForWidth())
        self.button_bar_cobranca.setSizePolicy(sizePolicy1)
        self.button_bar_cobranca.setMinimumSize(QSize(0, 0))
        self.button_bar_cobranca.setMaximumSize(QSize(500, 100))
        self.button_bar_cobranca.setSizeIncrement(QSize(0, 0))

        self.gridLayout_2.addWidget(self.button_bar_cobranca, 3, 0, 1, 1)

        self.pushButton_4 = QPushButton(Home)
        self.pushButton_4.setObjectName(u"pushButton_4")
        sizePolicy1.setHeightForWidth(self.pushButton_4.sizePolicy().hasHeightForWidth())
        self.pushButton_4.setSizePolicy(sizePolicy1)
        self.pushButton_4.setMaximumSize(QSize(500, 100))
        self.pushButton_4.setSizeIncrement(QSize(500, 100))

        self.gridLayout_2.addWidget(self.pushButton_4, 2, 0, 1, 1)


        self.retranslateUi(Home)

        self.stackedWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(Home)
    # setupUi

    def retranslateUi(self, Home):
        self.pushButton.setText(QCoreApplication.translate("Home", u"inicio", None))
        self.lineEdit_2.setText(QCoreApplication.translate("Home", u"Rua Oscar Pereira de Briro", None))
        self.lineEdit_7.setText(QCoreApplication.translate("Home", u"dd/mm/aaaa", None))
        self.lineEdit_3.setText(QCoreApplication.translate("Home", u"095.813.439-11", None))
        self.label_11.setText(QCoreApplication.translate("Home", u"Email:", None))
        self.label_2.setText(QCoreApplication.translate("Home", u"Foto", None))
        self.lineEdit_5.setText(QCoreApplication.translate("Home", u"S\u00e3o Bento", None))
        self.label_12.setText(QCoreApplication.translate("Home", u"Telefone:", None))
        self.comboBox.setItemText(0, "")
        self.comboBox.setItemText(1, QCoreApplication.translate("Home", u"Masculino", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("Home", u"Feminino", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("Home", u"Outro", None))

        self.lineEdit_9.setText(QCoreApplication.translate("Home", u"(67) 9 ", None))
        self.label_7.setText(QCoreApplication.translate("Home", u"CPF:", None))
        self.label_4.setText(QCoreApplication.translate("Home", u"Endere\u00e7o:", None))
        self.lineEdit_8.setText(QCoreApplication.translate("Home", u"josemarcio0araujo@gmail.com", None))
        self.lineEdit_4.setText(QCoreApplication.translate("Home", u"123456", None))
        self.label.setText(QCoreApplication.translate("Home", u"Cadastro de clientes:", None))
        self.label_8.setText(QCoreApplication.translate("Home", u"Sexo:", None))
        self.label_6.setText(QCoreApplication.translate("Home", u"Numero:", None))
        self.label_9.setText(QCoreApplication.translate("Home", u"Complemento:", None))
        self.label_5.setText(QCoreApplication.translate("Home", u"Bairro:", None))
        self.lineEdit.setText(QCoreApplication.translate("Home", u"Eliane Aparecida Rodrigueiro Ramos de Abreu", None))
        self.pushButton_2.setText(QCoreApplication.translate("Home", u"Cadastrar Cliente", None))
        self.label_3.setText(QCoreApplication.translate("Home", u"Nome:", None))
        self.label_10.setText(QCoreApplication.translate("Home", u"Data de Nascimento:", None))
        self.pushButton_3.setText(QCoreApplication.translate("Home", u"Limpar", None))
        self.button_bar_configuracoes.setText(QCoreApplication.translate("Home", u"Configura\u00e7\u00f5es", None))
        self.button_bar_inicio.setText(QCoreApplication.translate("Home", u"Inicio", None))
        self.button_bar_cadastrar.setText(QCoreApplication.translate("Home", u"Cadastrar Cliente", None))
        self.button_bar_cobranca.setText(QCoreApplication.translate("Home", u"Pagamento", None))
        self.pushButton_4.setText(QCoreApplication.translate("Home", u"Gerenciar Exercicios", None))
        pass
    # retranslateUi

