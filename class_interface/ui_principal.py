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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QLabel, QLayout, QLineEdit, QListView,
    QPushButton, QSizePolicy, QSpacerItem, QStackedWidget,
    QVBoxLayout, QWidget)

class Ui_Home(object):
    def setupUi(self, Home):
        if not Home.objectName():
            Home.setObjectName(u"Home")
        Home.setWindowModality(Qt.WindowModality.WindowModal)
        Home.setEnabled(True)
        Home.resize(1119, 881)
        Home.setWindowTitle(u"SysMar")
        Home.setStyleSheet(u"background-color: grey;")
        self.gridLayout_2 = QGridLayout(Home)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setSizeConstraint(QLayout.SizeConstraint.SetNoConstraint)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 1)
        self.stacked_principal = QStackedWidget(Home)
        self.stacked_principal.setObjectName(u"stacked_principal")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.pushButton = QPushButton(self.page)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(100, 40, 89, 25))
        self.stacked_principal.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.gridLayout_3 = QGridLayout(self.page_2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.verticalSpacer_4 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)

        self.gridLayout_3.addItem(self.verticalSpacer_4, 7, 0, 1, 1)

        self.cadastro_endereco_lineEdit = QLineEdit(self.page_2)
        self.cadastro_endereco_lineEdit.setObjectName(u"cadastro_endereco_lineEdit")
        self.cadastro_endereco_lineEdit.setStyleSheet(u"color: white;")

        self.gridLayout_3.addWidget(self.cadastro_endereco_lineEdit, 6, 0, 1, 1)

        self.gridLayout_7 = QGridLayout()
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.cadastro_nascimento_lineEdit = QLineEdit(self.page_2)
        self.cadastro_nascimento_lineEdit.setObjectName(u"cadastro_nascimento_lineEdit")
        self.cadastro_nascimento_lineEdit.setMaximumSize(QSize(100, 16777215))

        self.gridLayout_7.addWidget(self.cadastro_nascimento_lineEdit, 0, 0, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_7.addItem(self.horizontalSpacer_2, 0, 1, 1, 1)


        self.gridLayout_3.addLayout(self.gridLayout_7, 9, 0, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)

        self.gridLayout_3.addItem(self.verticalSpacer_3, 4, 0, 1, 1)

        self.cadastro_cpf_lineEdit = QLineEdit(self.page_2)
        self.cadastro_cpf_lineEdit.setObjectName(u"cadastro_cpf_lineEdit")
        self.cadastro_cpf_lineEdit.setStyleSheet(u"color: white;")

        self.gridLayout_3.addWidget(self.cadastro_cpf_lineEdit, 3, 1, 1, 1)

        self.label_11 = QLabel(self.page_2)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout_3.addWidget(self.label_11, 8, 1, 1, 1)

        self.label_2 = QLabel(self.page_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(85, 113))
        self.label_2.setMaximumSize(QSize(85, 113))
        self.label_2.setStyleSheet(u"background-color: rgb(153, 193, 241);")
        self.label_2.setTextFormat(Qt.TextFormat.AutoText)
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_3.addWidget(self.label_2, 1, 0, 1, 1)

        self.cadastro_bairro_lineEdit = QLineEdit(self.page_2)
        self.cadastro_bairro_lineEdit.setObjectName(u"cadastro_bairro_lineEdit")
        self.cadastro_bairro_lineEdit.setStyleSheet(u"color: white;")

        self.gridLayout_3.addWidget(self.cadastro_bairro_lineEdit, 6, 2, 1, 1)

        self.label_12 = QLabel(self.page_2)
        self.label_12.setObjectName(u"label_12")

        self.gridLayout_3.addWidget(self.label_12, 8, 2, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer_2, 14, 0, 1, 1)

        self.cadastro_sexo_comboBox = QComboBox(self.page_2)
        self.cadastro_sexo_comboBox.addItem("")
        self.cadastro_sexo_comboBox.addItem("")
        self.cadastro_sexo_comboBox.addItem("")
        self.cadastro_sexo_comboBox.addItem("")
        self.cadastro_sexo_comboBox.setObjectName(u"cadastro_sexo_comboBox")
        self.cadastro_sexo_comboBox.setMaximumSize(QSize(110, 16777215))
        self.cadastro_sexo_comboBox.setStyleSheet(u"color: white;")

        self.gridLayout_3.addWidget(self.cadastro_sexo_comboBox, 3, 2, 1, 1)

        self.verticalSpacer_5 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)

        self.gridLayout_3.addItem(self.verticalSpacer_5, 11, 1, 1, 1)

        self.cadastro_telefone_lineEdit = QLineEdit(self.page_2)
        self.cadastro_telefone_lineEdit.setObjectName(u"cadastro_telefone_lineEdit")
        self.cadastro_telefone_lineEdit.setStyleSheet(u"color: white;")

        self.gridLayout_3.addWidget(self.cadastro_telefone_lineEdit, 9, 2, 1, 1)

        self.label_7 = QLabel(self.page_2)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_3.addWidget(self.label_7, 2, 1, 1, 1)

        self.label_4 = QLabel(self.page_2)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_3.addWidget(self.label_4, 5, 0, 1, 1)

        self.cadastro_email_lineEdit = QLineEdit(self.page_2)
        self.cadastro_email_lineEdit.setObjectName(u"cadastro_email_lineEdit")
        self.cadastro_email_lineEdit.setStyleSheet(u"color: white;")

        self.gridLayout_3.addWidget(self.cadastro_email_lineEdit, 9, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer, 0, 1, 1, 1)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.cadastro_numero_lineEdit = QLineEdit(self.page_2)
        self.cadastro_numero_lineEdit.setObjectName(u"cadastro_numero_lineEdit")
        self.cadastro_numero_lineEdit.setMaximumSize(QSize(60, 16777215))

        self.gridLayout.addWidget(self.cadastro_numero_lineEdit, 0, 0, 1, 1)

        self.cadastro_complemento_lineEdit = QLineEdit(self.page_2)
        self.cadastro_complemento_lineEdit.setObjectName(u"cadastro_complemento_lineEdit")

        self.gridLayout.addWidget(self.cadastro_complemento_lineEdit, 0, 1, 1, 1)


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

        self.cadastro_nome_lineEdit = QLineEdit(self.page_2)
        self.cadastro_nome_lineEdit.setObjectName(u"cadastro_nome_lineEdit")
        self.cadastro_nome_lineEdit.setStyleSheet(u"color: white;")

        self.gridLayout_3.addWidget(self.cadastro_nome_lineEdit, 3, 0, 1, 1)

        self.button_cadastrar_cliente = QPushButton(self.page_2)
        self.button_cadastrar_cliente.setObjectName(u"button_cadastrar_cliente")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_cadastrar_cliente.sizePolicy().hasHeightForWidth())
        self.button_cadastrar_cliente.setSizePolicy(sizePolicy)
        self.button_cadastrar_cliente.setMinimumSize(QSize(0, 40))
        self.button_cadastrar_cliente.setMaximumSize(QSize(200, 40))
        self.button_cadastrar_cliente.setStyleSheet(u"color: white;")

        self.gridLayout_3.addWidget(self.button_cadastrar_cliente, 12, 1, 1, 1)

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
        self.pushButton_3.setStyleSheet(u"background-color: rgb(192, 28, 40);")

        self.gridLayout_3.addWidget(self.pushButton_3, 13, 1, 1, 1)

        self.stacked_principal.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.gridLayout_6 = QGridLayout(self.page_3)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.horizontalSpacer_3 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.gridLayout_6.addItem(self.horizontalSpacer_3, 0, 1, 1, 1)

        self.label_14 = QLabel(self.page_3)
        self.label_14.setObjectName(u"label_14")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_14.sizePolicy().hasHeightForWidth())
        self.label_14.setSizePolicy(sizePolicy1)
        self.label_14.setMinimumSize(QSize(100, 0))
        self.label_14.setFont(font)

        self.gridLayout_6.addWidget(self.label_14, 0, 0, 1, 1)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_6.addItem(self.verticalSpacer_6, 3, 0, 1, 1)

        self.label_13 = QLabel(self.page_3)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setMinimumSize(QSize(85, 113))
        self.label_13.setMaximumSize(QSize(85, 113))
        self.label_13.setStyleSheet(u"background-color: rgb(153, 193, 241);")

        self.gridLayout_6.addWidget(self.label_13, 1, 0, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_6.addItem(self.horizontalSpacer_4, 2, 1, 1, 1)

        self.gridLayout_8 = QGridLayout()
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_9 = QGridLayout()
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.pushButton_4 = QPushButton(self.page_3)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.gridLayout_9.addWidget(self.pushButton_4, 0, 1, 1, 1)

        self.lineEdit_11 = QLineEdit(self.page_3)
        self.lineEdit_11.setObjectName(u"lineEdit_11")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.lineEdit_11.sizePolicy().hasHeightForWidth())
        self.lineEdit_11.setSizePolicy(sizePolicy2)

        self.gridLayout_9.addWidget(self.lineEdit_11, 0, 0, 1, 1)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_9.addItem(self.horizontalSpacer_5, 0, 3, 1, 1)

        self.pushButton_7 = QPushButton(self.page_3)
        self.pushButton_7.setObjectName(u"pushButton_7")

        self.gridLayout_9.addWidget(self.pushButton_7, 0, 2, 1, 1)


        self.gridLayout_8.addLayout(self.gridLayout_9, 1, 1, 1, 1)

        self.label_16 = QLabel(self.page_3)
        self.label_16.setObjectName(u"label_16")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.label_16.sizePolicy().hasHeightForWidth())
        self.label_16.setSizePolicy(sizePolicy3)
        self.label_16.setMaximumSize(QSize(16777215, 20))

        self.gridLayout_8.addWidget(self.label_16, 1, 0, 1, 1)

        self.gridLayout_10 = QGridLayout()
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_10.addItem(self.horizontalSpacer_6, 0, 3, 1, 1)

        self.lineEdit_10 = QLineEdit(self.page_3)
        self.lineEdit_10.setObjectName(u"lineEdit_10")
        sizePolicy2.setHeightForWidth(self.lineEdit_10.sizePolicy().hasHeightForWidth())
        self.lineEdit_10.setSizePolicy(sizePolicy2)
        self.lineEdit_10.setMinimumSize(QSize(400, 0))

        self.gridLayout_10.addWidget(self.lineEdit_10, 0, 0, 1, 1)

        self.pushButton_5 = QPushButton(self.page_3)
        self.pushButton_5.setObjectName(u"pushButton_5")
        sizePolicy2.setHeightForWidth(self.pushButton_5.sizePolicy().hasHeightForWidth())
        self.pushButton_5.setSizePolicy(sizePolicy2)

        self.gridLayout_10.addWidget(self.pushButton_5, 0, 1, 1, 1)

        self.pushButton_6 = QPushButton(self.page_3)
        self.pushButton_6.setObjectName(u"pushButton_6")

        self.gridLayout_10.addWidget(self.pushButton_6, 0, 2, 1, 1)

        self.listView = QListView(self.page_3)
        self.listView.setObjectName(u"listView")
        self.listView.setEnabled(True)
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Ignored)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.listView.sizePolicy().hasHeightForWidth())
        self.listView.setSizePolicy(sizePolicy4)
        self.listView.setMaximumSize(QSize(16777215, 200))
        self.listView.setSelectionRectVisible(False)

        self.gridLayout_10.addWidget(self.listView, 1, 0, 1, 2)


        self.gridLayout_8.addLayout(self.gridLayout_10, 0, 1, 1, 1)

        self.label_15 = QLabel(self.page_3)
        self.label_15.setObjectName(u"label_15")

        self.gridLayout_8.addWidget(self.label_15, 0, 0, 1, 1)


        self.gridLayout_6.addLayout(self.gridLayout_8, 1, 1, 1, 1)

        self.stacked_principal.addWidget(self.page_3)

        self.gridLayout_2.addWidget(self.stacked_principal, 0, 1, 6, 1)

        self.frame = QFrame(Home)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"background-color: rgb(94, 92, 100);")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_4 = QGridLayout(self.frame)
        self.gridLayout_4.setSpacing(0)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(1)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.verticalLayout_2.setContentsMargins(0, -1, -1, -1)
        self.button_bar_inicio = QPushButton(self.frame)
        self.button_bar_inicio.setObjectName(u"button_bar_inicio")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.button_bar_inicio.sizePolicy().hasHeightForWidth())
        self.button_bar_inicio.setSizePolicy(sizePolicy5)
        self.button_bar_inicio.setMinimumSize(QSize(0, 0))
        self.button_bar_inicio.setMaximumSize(QSize(500, 60))
        self.button_bar_inicio.setSizeIncrement(QSize(0, 0))
        self.button_bar_inicio.setStyleSheet(u"background-color: rgb(119, 118, 123);\n"
"border: none;\n"
"color: white;")
        self.button_bar_inicio.setCheckable(False)
        self.button_bar_inicio.setChecked(False)
        self.button_bar_inicio.setAutoRepeat(False)
        self.button_bar_inicio.setAutoExclusive(False)
        self.button_bar_inicio.setAutoDefault(False)
        self.button_bar_inicio.setFlat(False)

        self.verticalLayout_2.addWidget(self.button_bar_inicio)

        self.button_bar_cadastrar = QPushButton(self.frame)
        self.button_bar_cadastrar.setObjectName(u"button_bar_cadastrar")
        sizePolicy5.setHeightForWidth(self.button_bar_cadastrar.sizePolicy().hasHeightForWidth())
        self.button_bar_cadastrar.setSizePolicy(sizePolicy5)
        self.button_bar_cadastrar.setMinimumSize(QSize(0, 0))
        self.button_bar_cadastrar.setMaximumSize(QSize(500, 60))
        self.button_bar_cadastrar.setSizeIncrement(QSize(0, 0))
        self.button_bar_cadastrar.setStyleSheet(u"background-color: rgb(119, 118, 123);\n"
"border: none;\n"
"color: white;")

        self.verticalLayout_2.addWidget(self.button_bar_cadastrar)

        self.button_bar_financeiro = QPushButton(self.frame)
        self.button_bar_financeiro.setObjectName(u"button_bar_financeiro")
        sizePolicy5.setHeightForWidth(self.button_bar_financeiro.sizePolicy().hasHeightForWidth())
        self.button_bar_financeiro.setSizePolicy(sizePolicy5)
        self.button_bar_financeiro.setMinimumSize(QSize(0, 0))
        self.button_bar_financeiro.setMaximumSize(QSize(500, 60))
        self.button_bar_financeiro.setSizeIncrement(QSize(0, 0))
        self.button_bar_financeiro.setStyleSheet(u"background-color: rgb(119, 118, 123);\n"
"border: none;\n"
"color: white;")

        self.verticalLayout_2.addWidget(self.button_bar_financeiro)

        self.button_bar_configuracoes = QPushButton(self.frame)
        self.button_bar_configuracoes.setObjectName(u"button_bar_configuracoes")
        sizePolicy5.setHeightForWidth(self.button_bar_configuracoes.sizePolicy().hasHeightForWidth())
        self.button_bar_configuracoes.setSizePolicy(sizePolicy5)
        self.button_bar_configuracoes.setMinimumSize(QSize(0, 0))
        self.button_bar_configuracoes.setMaximumSize(QSize(500, 60))
        self.button_bar_configuracoes.setSizeIncrement(QSize(0, 0))
        self.button_bar_configuracoes.setStyleSheet(u"background-color: rgb(119, 118, 123);\n"
"border: none;\n"
"color: white;")

        self.verticalLayout_2.addWidget(self.button_bar_configuracoes)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)


        self.gridLayout_4.addLayout(self.verticalLayout_2, 0, 0, 1, 1)


        self.gridLayout_2.addWidget(self.frame, 0, 0, 1, 1)


        self.retranslateUi(Home)

        self.stacked_principal.setCurrentIndex(1)
        self.button_bar_inicio.setDefault(False)


        QMetaObject.connectSlotsByName(Home)
    # setupUi

    def retranslateUi(self, Home):
        self.pushButton.setText(QCoreApplication.translate("Home", u"1", None))
        self.cadastro_endereco_lineEdit.setText(QCoreApplication.translate("Home", u"Rua Oscar Pereira de Briro", None))
        self.cadastro_nascimento_lineEdit.setText(QCoreApplication.translate("Home", u"12/12/1993", None))
        self.cadastro_cpf_lineEdit.setText(QCoreApplication.translate("Home", u"888.888.888-11", None))
        self.label_11.setText(QCoreApplication.translate("Home", u"Email:", None))
        self.label_2.setText(QCoreApplication.translate("Home", u"Foto", None))
        self.cadastro_bairro_lineEdit.setText(QCoreApplication.translate("Home", u"S\u00e3o Bento", None))
        self.label_12.setText(QCoreApplication.translate("Home", u"Telefone:", None))
        self.cadastro_sexo_comboBox.setItemText(0, "")
        self.cadastro_sexo_comboBox.setItemText(1, QCoreApplication.translate("Home", u"Masculino", None))
        self.cadastro_sexo_comboBox.setItemText(2, QCoreApplication.translate("Home", u"Feminino", None))
        self.cadastro_sexo_comboBox.setItemText(3, QCoreApplication.translate("Home", u"Outro", None))

        self.cadastro_telefone_lineEdit.setText(QCoreApplication.translate("Home", u"(67) 9 96995588", None))
        self.label_7.setText(QCoreApplication.translate("Home", u"CPF:", None))
        self.label_4.setText(QCoreApplication.translate("Home", u"Endere\u00e7o:", None))
        self.cadastro_email_lineEdit.setText(QCoreApplication.translate("Home", u"email.escolhido@gmail.com", None))
        self.cadastro_numero_lineEdit.setText(QCoreApplication.translate("Home", u"223", None))
        self.cadastro_complemento_lineEdit.setText(QCoreApplication.translate("Home", u"Casa", None))
        self.label.setText(QCoreApplication.translate("Home", u"Cadastro de clientes:", None))
        self.label_8.setText(QCoreApplication.translate("Home", u"Sexo:", None))
        self.label_6.setText(QCoreApplication.translate("Home", u"Numero:", None))
        self.label_9.setText(QCoreApplication.translate("Home", u"Complemento:", None))
        self.label_5.setText(QCoreApplication.translate("Home", u"Bairro:", None))
        self.cadastro_nome_lineEdit.setText(QCoreApplication.translate("Home", u"Andre da Silva Duarte", None))
        self.button_cadastrar_cliente.setText(QCoreApplication.translate("Home", u"Cadastrar Cliente", None))
        self.label_3.setText(QCoreApplication.translate("Home", u"Nome:", None))
        self.label_10.setText(QCoreApplication.translate("Home", u"Data de Nascimento:", None))
        self.pushButton_3.setText(QCoreApplication.translate("Home", u"Limpar", None))
        self.label_14.setText(QCoreApplication.translate("Home", u"Pagamento:", None))
        self.label_13.setText(QCoreApplication.translate("Home", u" Foto", None))
        self.pushButton_4.setText(QCoreApplication.translate("Home", u"Pesquisar", None))
        self.pushButton_7.setText(QCoreApplication.translate("Home", u"Limpar", None))
        self.label_16.setText(QCoreApplication.translate("Home", u"Matricula:", None))
        self.pushButton_5.setText(QCoreApplication.translate("Home", u"Pesquisar", None))
        self.pushButton_6.setText(QCoreApplication.translate("Home", u"Limpar", None))
        self.label_15.setText(QCoreApplication.translate("Home", u"Nome:", None))
        self.button_bar_inicio.setText(QCoreApplication.translate("Home", u"Inicio", None))
        self.button_bar_cadastrar.setText(QCoreApplication.translate("Home", u"Cadastro", None))
        self.button_bar_financeiro.setText(QCoreApplication.translate("Home", u"Financeiro", None))
        self.button_bar_configuracoes.setText(QCoreApplication.translate("Home", u"Configura\u00e7\u00f5es", None))
        pass
    # retranslateUi

