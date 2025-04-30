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
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QDateTimeEdit,
    QFrame, QGridLayout, QLabel, QLayout,
    QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
    QStackedWidget, QTabWidget, QVBoxLayout, QWidget)

class Ui_Home(object):
    def setupUi(self, Home):
        if not Home.objectName():
            Home.setObjectName(u"Home")
        Home.setWindowModality(Qt.WindowModality.WindowModal)
        Home.setEnabled(True)
        Home.resize(1121, 881)
        Home.setWindowTitle(u"SysMar")
        Home.setStyleSheet(u"background-color: grey;")
        self.gridLayout_2 = QGridLayout(Home)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setSizeConstraint(QLayout.SizeConstraint.SetNoConstraint)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 1)
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
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_bar_inicio.sizePolicy().hasHeightForWidth())
        self.button_bar_inicio.setSizePolicy(sizePolicy)
        self.button_bar_inicio.setMinimumSize(QSize(0, 0))
        self.button_bar_inicio.setMaximumSize(QSize(500, 60))
        self.button_bar_inicio.setSizeIncrement(QSize(0, 0))
        self.button_bar_inicio.setStyleSheet(u"background-color: rgb(26, 95, 180);\n"
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
        sizePolicy.setHeightForWidth(self.button_bar_cadastrar.sizePolicy().hasHeightForWidth())
        self.button_bar_cadastrar.setSizePolicy(sizePolicy)
        self.button_bar_cadastrar.setMinimumSize(QSize(0, 0))
        self.button_bar_cadastrar.setMaximumSize(QSize(500, 60))
        self.button_bar_cadastrar.setSizeIncrement(QSize(0, 0))
        self.button_bar_cadastrar.setStyleSheet(u"background-color: rgb(26, 95, 180);\n"
"border: none;\n"
"color: white;")

        self.verticalLayout_2.addWidget(self.button_bar_cadastrar)

        self.button_bar_financeiro = QPushButton(self.frame)
        self.button_bar_financeiro.setObjectName(u"button_bar_financeiro")
        sizePolicy.setHeightForWidth(self.button_bar_financeiro.sizePolicy().hasHeightForWidth())
        self.button_bar_financeiro.setSizePolicy(sizePolicy)
        self.button_bar_financeiro.setMinimumSize(QSize(0, 0))
        self.button_bar_financeiro.setMaximumSize(QSize(500, 60))
        self.button_bar_financeiro.setSizeIncrement(QSize(0, 0))
        self.button_bar_financeiro.setStyleSheet(u"background-color: rgb(26, 95, 180);\n"
"border: none;\n"
"color: white;")

        self.verticalLayout_2.addWidget(self.button_bar_financeiro)

        self.button_bar_aluno = QPushButton(self.frame)
        self.button_bar_aluno.setObjectName(u"button_bar_aluno")
        sizePolicy.setHeightForWidth(self.button_bar_aluno.sizePolicy().hasHeightForWidth())
        self.button_bar_aluno.setSizePolicy(sizePolicy)
        self.button_bar_aluno.setMinimumSize(QSize(0, 0))
        self.button_bar_aluno.setMaximumSize(QSize(500, 60))
        self.button_bar_aluno.setSizeIncrement(QSize(0, 0))
        self.button_bar_aluno.setStyleSheet(u"background-color: rgb(26, 95, 180);\n"
"border: none;\n"
"color: white;")

        self.verticalLayout_2.addWidget(self.button_bar_aluno)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)


        self.gridLayout_4.addLayout(self.verticalLayout_2, 0, 0, 1, 1)


        self.gridLayout_2.addWidget(self.frame, 0, 0, 1, 1)

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
        self.label_4 = QLabel(self.page_2)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_3.addWidget(self.label_4, 4, 0, 1, 1)

        self.cadastro_nome_lineEdit = QLineEdit(self.page_2)
        self.cadastro_nome_lineEdit.setObjectName(u"cadastro_nome_lineEdit")
        self.cadastro_nome_lineEdit.setStyleSheet(u"color: white;")

        self.gridLayout_3.addWidget(self.cadastro_nome_lineEdit, 2, 0, 1, 1)

        self.pushButton_3 = QPushButton(self.page_2)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setMinimumSize(QSize(0, 40))
        self.pushButton_3.setMaximumSize(QSize(200, 16777215))
        self.pushButton_3.setStyleSheet(u"background-color: rgb(192, 28, 40);")

        self.gridLayout_3.addWidget(self.pushButton_3, 12, 1, 1, 1)

        self.cadastro_endereco_lineEdit = QLineEdit(self.page_2)
        self.cadastro_endereco_lineEdit.setObjectName(u"cadastro_endereco_lineEdit")
        self.cadastro_endereco_lineEdit.setStyleSheet(u"color: white;")

        self.gridLayout_3.addWidget(self.cadastro_endereco_lineEdit, 5, 0, 1, 1)

        self.cadastro_cpf_lineEdit = QLineEdit(self.page_2)
        self.cadastro_cpf_lineEdit.setObjectName(u"cadastro_cpf_lineEdit")
        self.cadastro_cpf_lineEdit.setStyleSheet(u"color: white;")

        self.gridLayout_3.addWidget(self.cadastro_cpf_lineEdit, 2, 1, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer_2, 13, 0, 1, 1)

        self.label_8 = QLabel(self.page_2)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_3.addWidget(self.label_8, 1, 2, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)

        self.gridLayout_3.addItem(self.verticalSpacer_4, 6, 0, 1, 1)

        self.verticalSpacer_5 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)

        self.gridLayout_3.addItem(self.verticalSpacer_5, 10, 1, 1, 1)

        self.cadastro_sexo_comboBox = QComboBox(self.page_2)
        self.cadastro_sexo_comboBox.addItem("")
        self.cadastro_sexo_comboBox.addItem("")
        self.cadastro_sexo_comboBox.addItem("")
        self.cadastro_sexo_comboBox.addItem("")
        self.cadastro_sexo_comboBox.setObjectName(u"cadastro_sexo_comboBox")
        self.cadastro_sexo_comboBox.setMaximumSize(QSize(110, 16777215))
        self.cadastro_sexo_comboBox.setStyleSheet(u"color: white;")

        self.gridLayout_3.addWidget(self.cadastro_sexo_comboBox, 2, 2, 1, 1)

        self.button_cadastrar_cliente = QPushButton(self.page_2)
        self.button_cadastrar_cliente.setObjectName(u"button_cadastrar_cliente")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.button_cadastrar_cliente.sizePolicy().hasHeightForWidth())
        self.button_cadastrar_cliente.setSizePolicy(sizePolicy1)
        self.button_cadastrar_cliente.setMinimumSize(QSize(0, 40))
        self.button_cadastrar_cliente.setMaximumSize(QSize(200, 40))
        self.button_cadastrar_cliente.setStyleSheet(u"color: white;\n"
"background-color: rgb(26, 95, 180);")

        self.gridLayout_3.addWidget(self.button_cadastrar_cliente, 11, 1, 1, 1)

        self.gridLayout_7 = QGridLayout()
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.cadastro_nascimento_lineEdit = QLineEdit(self.page_2)
        self.cadastro_nascimento_lineEdit.setObjectName(u"cadastro_nascimento_lineEdit")
        self.cadastro_nascimento_lineEdit.setMaximumSize(QSize(100, 16777215))

        self.gridLayout_7.addWidget(self.cadastro_nascimento_lineEdit, 0, 0, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_7.addItem(self.horizontalSpacer_2, 0, 1, 1, 1)


        self.gridLayout_3.addLayout(self.gridLayout_7, 8, 0, 1, 1)

        self.cadastro_email_lineEdit = QLineEdit(self.page_2)
        self.cadastro_email_lineEdit.setObjectName(u"cadastro_email_lineEdit")
        self.cadastro_email_lineEdit.setStyleSheet(u"color: white;")

        self.gridLayout_3.addWidget(self.cadastro_email_lineEdit, 8, 1, 1, 1)

        self.label = QLabel(self.page_2)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(20)
        self.label.setFont(font)

        self.gridLayout_3.addWidget(self.label, 0, 0, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer, 0, 1, 1, 1)

        self.label_10 = QLabel(self.page_2)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout_3.addWidget(self.label_10, 7, 0, 1, 1)

        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.label_6 = QLabel(self.page_2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMaximumSize(QSize(60, 16777215))

        self.gridLayout_5.addWidget(self.label_6, 0, 0, 1, 1)

        self.label_9 = QLabel(self.page_2)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout_5.addWidget(self.label_9, 0, 1, 1, 1)


        self.gridLayout_3.addLayout(self.gridLayout_5, 4, 1, 1, 1)

        self.label_3 = QLabel(self.page_2)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_3.addWidget(self.label_3, 1, 0, 1, 1)

        self.label_11 = QLabel(self.page_2)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout_3.addWidget(self.label_11, 7, 1, 1, 1)

        self.cadastro_telefone_lineEdit = QLineEdit(self.page_2)
        self.cadastro_telefone_lineEdit.setObjectName(u"cadastro_telefone_lineEdit")
        self.cadastro_telefone_lineEdit.setStyleSheet(u"color: white;")

        self.gridLayout_3.addWidget(self.cadastro_telefone_lineEdit, 8, 2, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)

        self.gridLayout_3.addItem(self.verticalSpacer_3, 3, 0, 1, 1)

        self.label_7 = QLabel(self.page_2)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_3.addWidget(self.label_7, 1, 1, 1, 1)

        self.cadastro_bairro_lineEdit = QLineEdit(self.page_2)
        self.cadastro_bairro_lineEdit.setObjectName(u"cadastro_bairro_lineEdit")
        self.cadastro_bairro_lineEdit.setStyleSheet(u"color: white;")

        self.gridLayout_3.addWidget(self.cadastro_bairro_lineEdit, 5, 2, 1, 1)

        self.label_12 = QLabel(self.page_2)
        self.label_12.setObjectName(u"label_12")

        self.gridLayout_3.addWidget(self.label_12, 7, 2, 1, 1)

        self.label_5 = QLabel(self.page_2)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_3.addWidget(self.label_5, 4, 2, 1, 1)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.cadastro_numero_lineEdit = QLineEdit(self.page_2)
        self.cadastro_numero_lineEdit.setObjectName(u"cadastro_numero_lineEdit")
        self.cadastro_numero_lineEdit.setMaximumSize(QSize(60, 16777215))

        self.gridLayout.addWidget(self.cadastro_numero_lineEdit, 0, 0, 1, 1)

        self.cadastro_complemento_lineEdit = QLineEdit(self.page_2)
        self.cadastro_complemento_lineEdit.setObjectName(u"cadastro_complemento_lineEdit")

        self.gridLayout.addWidget(self.cadastro_complemento_lineEdit, 0, 1, 1, 1)


        self.gridLayout_3.addLayout(self.gridLayout, 5, 1, 1, 1)

        self.stacked_principal.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.gridLayout_6 = QGridLayout(self.page_3)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.verticalSpacer_8 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_6.addItem(self.verticalSpacer_8, 3, 1, 1, 1)

        self.label_13 = QLabel(self.page_3)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setMinimumSize(QSize(85, 113))
        self.label_13.setMaximumSize(QSize(85, 113))
        self.label_13.setStyleSheet(u"background-color: rgb(153, 193, 241);")
        self.label_13.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_6.addWidget(self.label_13, 1, 0, 1, 1)

        self.label_14 = QLabel(self.page_3)
        self.label_14.setObjectName(u"label_14")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_14.sizePolicy().hasHeightForWidth())
        self.label_14.setSizePolicy(sizePolicy2)
        self.label_14.setMinimumSize(QSize(100, 0))
        self.label_14.setFont(font)

        self.gridLayout_6.addWidget(self.label_14, 0, 0, 1, 1)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_6.addItem(self.verticalSpacer_6, 5, 0, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_6.addItem(self.horizontalSpacer_4, 4, 1, 1, 1)

        self.gridLayout_11 = QGridLayout()
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.label_21 = QLabel(self.page_3)
        self.label_21.setObjectName(u"label_21")

        self.gridLayout_11.addWidget(self.label_21, 4, 0, 1, 1)

        self.pushButton_2 = QPushButton(self.page_3)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setStyleSheet(u"color: white;\n"
"background-color: rgb(26, 95, 180);")

        self.gridLayout_11.addWidget(self.pushButton_2, 5, 2, 1, 1)

        self.lineEdit_3 = QLineEdit(self.page_3)
        self.lineEdit_3.setObjectName(u"lineEdit_3")

        self.gridLayout_11.addWidget(self.lineEdit_3, 4, 1, 1, 1)

        self.label_18 = QLabel(self.page_3)
        self.label_18.setObjectName(u"label_18")

        self.gridLayout_11.addWidget(self.label_18, 0, 2, 1, 1)

        self.label_20 = QLabel(self.page_3)
        self.label_20.setObjectName(u"label_20")

        self.gridLayout_11.addWidget(self.label_20, 2, 2, 1, 1)

        self.lineEdit_4 = QLineEdit(self.page_3)
        self.lineEdit_4.setObjectName(u"lineEdit_4")

        self.gridLayout_11.addWidget(self.lineEdit_4, 0, 3, 1, 1)

        self.comboBox = QComboBox(self.page_3)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")

        self.gridLayout_11.addWidget(self.comboBox, 2, 1, 1, 1)

        self.label_17 = QLabel(self.page_3)
        self.label_17.setObjectName(u"label_17")

        self.gridLayout_11.addWidget(self.label_17, 0, 0, 1, 1)

        self.lineEdit = QLineEdit(self.page_3)
        self.lineEdit.setObjectName(u"lineEdit")

        self.gridLayout_11.addWidget(self.lineEdit, 0, 1, 1, 1)

        self.label_19 = QLabel(self.page_3)
        self.label_19.setObjectName(u"label_19")

        self.gridLayout_11.addWidget(self.label_19, 2, 0, 1, 1)

        self.comboBox_2 = QComboBox(self.page_3)
        self.comboBox_2.setObjectName(u"comboBox_2")

        self.gridLayout_11.addWidget(self.comboBox_2, 2, 3, 1, 1)

        self.label_24 = QLabel(self.page_3)
        self.label_24.setObjectName(u"label_24")

        self.gridLayout_11.addWidget(self.label_24, 4, 2, 1, 1)

        self.lineEdit_6 = QLineEdit(self.page_3)
        self.lineEdit_6.setObjectName(u"lineEdit_6")

        self.gridLayout_11.addWidget(self.lineEdit_6, 4, 3, 1, 1)


        self.gridLayout_6.addLayout(self.gridLayout_11, 2, 1, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.gridLayout_6.addItem(self.horizontalSpacer_3, 0, 1, 1, 1)

        self.gridLayout_8 = QGridLayout()
        self.gridLayout_8.setSpacing(0)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_10 = QGridLayout()
        self.gridLayout_10.setSpacing(0)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.label_15 = QLabel(self.page_3)
        self.label_15.setObjectName(u"label_15")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.label_15.sizePolicy().hasHeightForWidth())
        self.label_15.setSizePolicy(sizePolicy3)
        self.label_15.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_10.addWidget(self.label_15, 0, 0, 1, 1)


        self.gridLayout_8.addLayout(self.gridLayout_10, 0, 0, 1, 1)

        self.gridLayout_nome = QGridLayout()
        self.gridLayout_nome.setSpacing(0)
        self.gridLayout_nome.setObjectName(u"gridLayout_nome")
        self.gridLayout_nome.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_nome.addItem(self.horizontalSpacer_6, 0, 3, 1, 1)

        self.lineEdit_pesquisa_cliente = QLineEdit(self.page_3)
        self.lineEdit_pesquisa_cliente.setObjectName(u"lineEdit_pesquisa_cliente")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.lineEdit_pesquisa_cliente.sizePolicy().hasHeightForWidth())
        self.lineEdit_pesquisa_cliente.setSizePolicy(sizePolicy4)
        self.lineEdit_pesquisa_cliente.setMinimumSize(QSize(400, 0))

        self.gridLayout_nome.addWidget(self.lineEdit_pesquisa_cliente, 0, 0, 1, 1)

        self.pushButton_6 = QPushButton(self.page_3)
        self.pushButton_6.setObjectName(u"pushButton_6")

        self.gridLayout_nome.addWidget(self.pushButton_6, 0, 2, 1, 1)

        self.button_financeiro_pesquisar = QPushButton(self.page_3)
        self.button_financeiro_pesquisar.setObjectName(u"button_financeiro_pesquisar")
        sizePolicy4.setHeightForWidth(self.button_financeiro_pesquisar.sizePolicy().hasHeightForWidth())
        self.button_financeiro_pesquisar.setSizePolicy(sizePolicy4)
        self.button_financeiro_pesquisar.setStyleSheet(u"color: white;\n"
"background-color: rgb(26, 95, 180);")

        self.gridLayout_nome.addWidget(self.button_financeiro_pesquisar, 0, 1, 1, 1)


        self.gridLayout_8.addLayout(self.gridLayout_nome, 0, 1, 1, 1)

        self.gridLayout_9 = QGridLayout()
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.pushButton_7 = QPushButton(self.page_3)
        self.pushButton_7.setObjectName(u"pushButton_7")

        self.gridLayout_9.addWidget(self.pushButton_7, 0, 2, 1, 1)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_9.addItem(self.horizontalSpacer_5, 0, 3, 1, 1)

        self.pushButton_4 = QPushButton(self.page_3)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setStyleSheet(u"color: white;\n"
"background-color: rgb(26, 95, 180);")

        self.gridLayout_9.addWidget(self.pushButton_4, 0, 1, 1, 1)

        self.lineEdit_pesquisa_id = QLineEdit(self.page_3)
        self.lineEdit_pesquisa_id.setObjectName(u"lineEdit_pesquisa_id")
        sizePolicy4.setHeightForWidth(self.lineEdit_pesquisa_id.sizePolicy().hasHeightForWidth())
        self.lineEdit_pesquisa_id.setSizePolicy(sizePolicy4)

        self.gridLayout_9.addWidget(self.lineEdit_pesquisa_id, 0, 0, 1, 1)


        self.gridLayout_8.addLayout(self.gridLayout_9, 1, 1, 1, 1)

        self.label_16 = QLabel(self.page_3)
        self.label_16.setObjectName(u"label_16")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.label_16.sizePolicy().hasHeightForWidth())
        self.label_16.setSizePolicy(sizePolicy5)
        self.label_16.setMaximumSize(QSize(16777215, 20))

        self.gridLayout_8.addWidget(self.label_16, 1, 0, 1, 1)


        self.gridLayout_6.addLayout(self.gridLayout_8, 1, 1, 1, 1)

        self.stacked_principal.addWidget(self.page_3)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.gridLayout_13 = QGridLayout(self.page_4)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.gridLayout_12 = QGridLayout()
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.gridLayout_14 = QGridLayout()
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.lineEdit_aluno_pesquisa_nome = QLineEdit(self.page_4)
        self.lineEdit_aluno_pesquisa_nome.setObjectName(u"lineEdit_aluno_pesquisa_nome")

        self.gridLayout_14.addWidget(self.lineEdit_aluno_pesquisa_nome, 0, 1, 1, 1)

        self.btn_aluno_pesquisa = QPushButton(self.page_4)
        self.btn_aluno_pesquisa.setObjectName(u"btn_aluno_pesquisa")
        sizePolicy4.setHeightForWidth(self.btn_aluno_pesquisa.sizePolicy().hasHeightForWidth())
        self.btn_aluno_pesquisa.setSizePolicy(sizePolicy4)
        self.btn_aluno_pesquisa.setStyleSheet(u"color: white;\n"
"background-color: rgb(26, 95, 180);")

        self.gridLayout_14.addWidget(self.btn_aluno_pesquisa, 1, 1, 1, 1)

        self.label_23 = QLabel(self.page_4)
        self.label_23.setObjectName(u"label_23")

        self.gridLayout_14.addWidget(self.label_23, 2, 0, 1, 1)

        self.lineEdit_5 = QLineEdit(self.page_4)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setMaximumSize(QSize(200, 16777215))

        self.gridLayout_14.addWidget(self.lineEdit_5, 2, 1, 1, 1)

        self.label_22 = QLabel(self.page_4)
        self.label_22.setObjectName(u"label_22")

        self.gridLayout_14.addWidget(self.label_22, 0, 0, 1, 1)

        self.pushButton_8 = QPushButton(self.page_4)
        self.pushButton_8.setObjectName(u"pushButton_8")
        sizePolicy4.setHeightForWidth(self.pushButton_8.sizePolicy().hasHeightForWidth())
        self.pushButton_8.setSizePolicy(sizePolicy4)
        self.pushButton_8.setStyleSheet(u"color: white;\n"
"background-color: rgb(26, 95, 180);")

        self.gridLayout_14.addWidget(self.pushButton_8, 3, 1, 1, 1)


        self.gridLayout_12.addLayout(self.gridLayout_14, 0, 0, 1, 1)


        self.gridLayout_13.addLayout(self.gridLayout_12, 0, 0, 1, 1)

        self.tabWidget = QTabWidget(self.page_4)
        self.tabWidget.setObjectName(u"tabWidget")
        self.Perfil_tab = QWidget()
        self.Perfil_tab.setObjectName(u"Perfil_tab")
        self.gridLayout_16 = QGridLayout(self.Perfil_tab)
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        self.gridLayout_18 = QGridLayout()
        self.gridLayout_18.setObjectName(u"gridLayout_18")
        self.btn_aluno_salvar = QPushButton(self.Perfil_tab)
        self.btn_aluno_salvar.setObjectName(u"btn_aluno_salvar")
        sizePolicy4.setHeightForWidth(self.btn_aluno_salvar.sizePolicy().hasHeightForWidth())
        self.btn_aluno_salvar.setSizePolicy(sizePolicy4)
        self.btn_aluno_salvar.setStyleSheet(u"color: white;\n"
"background-color: rgb(26, 95, 180);")

        self.gridLayout_18.addWidget(self.btn_aluno_salvar, 0, 1, 1, 1)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_18.addItem(self.horizontalSpacer_8, 0, 0, 1, 1)

        self.pushButton_12 = QPushButton(self.Perfil_tab)
        self.pushButton_12.setObjectName(u"pushButton_12")
        sizePolicy4.setHeightForWidth(self.pushButton_12.sizePolicy().hasHeightForWidth())
        self.pushButton_12.setSizePolicy(sizePolicy4)

        self.gridLayout_18.addWidget(self.pushButton_12, 0, 2, 1, 1)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_18.addItem(self.horizontalSpacer_9, 0, 3, 1, 1)


        self.gridLayout_16.addLayout(self.gridLayout_18, 2, 0, 1, 1)

        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_16.addItem(self.verticalSpacer_7, 3, 0, 1, 1)

        self.gridLayout_15 = QGridLayout()
        self.gridLayout_15.setSpacing(0)
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.gridLayout_15.setSizeConstraint(QLayout.SizeConstraint.SetFixedSize)
        self.label_25 = QLabel(self.Perfil_tab)
        self.label_25.setObjectName(u"label_25")
        sizePolicy4.setHeightForWidth(self.label_25.sizePolicy().hasHeightForWidth())
        self.label_25.setSizePolicy(sizePolicy4)
        self.label_25.setMinimumSize(QSize(100, 120))
        self.label_25.setMaximumSize(QSize(100, 120))
        self.label_25.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_15.addWidget(self.label_25, 0, 0, 1, 1)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_15.addItem(self.horizontalSpacer_7, 0, 2, 1, 1)

        self.pushButton_10 = QPushButton(self.Perfil_tab)
        self.pushButton_10.setObjectName(u"pushButton_10")
        self.pushButton_10.setStyleSheet(u"color: white;\n"
"background-color: rgb(26, 95, 180);")

        self.gridLayout_15.addWidget(self.pushButton_10, 1, 0, 1, 1)

        self.pushButton_11 = QPushButton(self.Perfil_tab)
        self.pushButton_11.setObjectName(u"pushButton_11")

        self.gridLayout_15.addWidget(self.pushButton_11, 1, 1, 1, 1)


        self.gridLayout_16.addLayout(self.gridLayout_15, 0, 0, 1, 1)

        self.gridLayout_17 = QGridLayout()
        self.gridLayout_17.setObjectName(u"gridLayout_17")
        self.lineEdit_aluno_nome = QLineEdit(self.Perfil_tab)
        self.lineEdit_aluno_nome.setObjectName(u"lineEdit_aluno_nome")

        self.gridLayout_17.addWidget(self.lineEdit_aluno_nome, 1, 1, 1, 1)

        self.label_29 = QLabel(self.Perfil_tab)
        self.label_29.setObjectName(u"label_29")

        self.gridLayout_17.addWidget(self.label_29, 4, 0, 1, 1)

        self.lineEdit_aluno_endereco = QLineEdit(self.Perfil_tab)
        self.lineEdit_aluno_endereco.setObjectName(u"lineEdit_aluno_endereco")

        self.gridLayout_17.addWidget(self.lineEdit_aluno_endereco, 6, 1, 1, 1)

        self.label_27 = QLabel(self.Perfil_tab)
        self.label_27.setObjectName(u"label_27")

        self.gridLayout_17.addWidget(self.label_27, 2, 0, 1, 1)

        self.lineEdit_aluno_sexo = QLineEdit(self.Perfil_tab)
        self.lineEdit_aluno_sexo.setObjectName(u"lineEdit_aluno_sexo")

        self.gridLayout_17.addWidget(self.lineEdit_aluno_sexo, 10, 1, 1, 1)

        self.label_28 = QLabel(self.Perfil_tab)
        self.label_28.setObjectName(u"label_28")

        self.gridLayout_17.addWidget(self.label_28, 3, 0, 1, 1)

        self.lineEdit_aluno_nascimento = QLineEdit(self.Perfil_tab)
        self.lineEdit_aluno_nascimento.setObjectName(u"lineEdit_aluno_nascimento")

        self.gridLayout_17.addWidget(self.lineEdit_aluno_nascimento, 3, 1, 1, 1)

        self.label_32 = QLabel(self.Perfil_tab)
        self.label_32.setObjectName(u"label_32")

        self.gridLayout_17.addWidget(self.label_32, 9, 0, 1, 1)

        self.lineEdit_aluno_email = QLineEdit(self.Perfil_tab)
        self.lineEdit_aluno_email.setObjectName(u"lineEdit_aluno_email")

        self.gridLayout_17.addWidget(self.lineEdit_aluno_email, 4, 1, 1, 1)

        self.label_26 = QLabel(self.Perfil_tab)
        self.label_26.setObjectName(u"label_26")

        self.gridLayout_17.addWidget(self.label_26, 1, 0, 1, 1)

        self.lineEdit_aluno_matricula = QLineEdit(self.Perfil_tab)
        self.lineEdit_aluno_matricula.setObjectName(u"lineEdit_aluno_matricula")

        self.gridLayout_17.addWidget(self.lineEdit_aluno_matricula, 0, 1, 1, 1)

        self.label_31 = QLabel(self.Perfil_tab)
        self.label_31.setObjectName(u"label_31")

        self.gridLayout_17.addWidget(self.label_31, 8, 0, 1, 1)

        self.lineEdit_aluno_cpf = QLineEdit(self.Perfil_tab)
        self.lineEdit_aluno_cpf.setObjectName(u"lineEdit_aluno_cpf")

        self.gridLayout_17.addWidget(self.lineEdit_aluno_cpf, 2, 1, 1, 1)

        self.lineEdit_aluno_bairro = QLineEdit(self.Perfil_tab)
        self.lineEdit_aluno_bairro.setObjectName(u"lineEdit_aluno_bairro")

        self.gridLayout_17.addWidget(self.lineEdit_aluno_bairro, 7, 1, 1, 1)

        self.label_33 = QLabel(self.Perfil_tab)
        self.label_33.setObjectName(u"label_33")

        self.gridLayout_17.addWidget(self.label_33, 10, 0, 1, 1)

        self.label_36 = QLabel(self.Perfil_tab)
        self.label_36.setObjectName(u"label_36")

        self.gridLayout_17.addWidget(self.label_36, 7, 0, 1, 1)

        self.lineEdit_aluno_numero = QLineEdit(self.Perfil_tab)
        self.lineEdit_aluno_numero.setObjectName(u"lineEdit_aluno_numero")

        self.gridLayout_17.addWidget(self.lineEdit_aluno_numero, 8, 1, 1, 1)

        self.label_2 = QLabel(self.Perfil_tab)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_17.addWidget(self.label_2, 0, 0, 1, 1)

        self.lineEdit_aluno_complemento = QLineEdit(self.Perfil_tab)
        self.lineEdit_aluno_complemento.setObjectName(u"lineEdit_aluno_complemento")

        self.gridLayout_17.addWidget(self.lineEdit_aluno_complemento, 9, 1, 1, 1)

        self.label_30 = QLabel(self.Perfil_tab)
        self.label_30.setObjectName(u"label_30")

        self.gridLayout_17.addWidget(self.label_30, 6, 0, 1, 1)

        self.label_37 = QLabel(self.Perfil_tab)
        self.label_37.setObjectName(u"label_37")

        self.gridLayout_17.addWidget(self.label_37, 5, 0, 1, 1)

        self.lineEdit_aluno_telefone = QLineEdit(self.Perfil_tab)
        self.lineEdit_aluno_telefone.setObjectName(u"lineEdit_aluno_telefone")

        self.gridLayout_17.addWidget(self.lineEdit_aluno_telefone, 5, 1, 1, 1)


        self.gridLayout_16.addLayout(self.gridLayout_17, 1, 0, 1, 1)

        self.tabWidget.addTab(self.Perfil_tab, "")
        self.pagamento_tab = QWidget()
        self.pagamento_tab.setObjectName(u"pagamento_tab")
        self.gridLayout_20 = QGridLayout(self.pagamento_tab)
        self.gridLayout_20.setObjectName(u"gridLayout_20")
        self.label_35 = QLabel(self.pagamento_tab)
        self.label_35.setObjectName(u"label_35")

        self.gridLayout_20.addWidget(self.label_35, 1, 0, 1, 1)

        self.verticalSpacer_9 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_20.addItem(self.verticalSpacer_9, 3, 0, 1, 1)

        self.label_34 = QLabel(self.pagamento_tab)
        self.label_34.setObjectName(u"label_34")
        sizePolicy6 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.label_34.sizePolicy().hasHeightForWidth())
        self.label_34.setSizePolicy(sizePolicy6)

        self.gridLayout_20.addWidget(self.label_34, 0, 0, 1, 1)

        self.comboBox_3 = QComboBox(self.pagamento_tab)
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.setObjectName(u"comboBox_3")
        sizePolicy4.setHeightForWidth(self.comboBox_3.sizePolicy().hasHeightForWidth())
        self.comboBox_3.setSizePolicy(sizePolicy4)
        self.comboBox_3.setMinimumSize(QSize(100, 0))

        self.gridLayout_20.addWidget(self.comboBox_3, 0, 1, 1, 1)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_20.addItem(self.horizontalSpacer_10, 0, 2, 1, 1)

        self.dateEdit = QDateEdit(self.pagamento_tab)
        self.dateEdit.setObjectName(u"dateEdit")
        self.dateEdit.setMaximumDate(QDate(9999, 12, 30))
        self.dateEdit.setCurrentSection(QDateTimeEdit.Section.DaySection)
        self.dateEdit.setCalendarPopup(True)

        self.gridLayout_20.addWidget(self.dateEdit, 1, 1, 1, 1)

        self.pushButton_13 = QPushButton(self.pagamento_tab)
        self.pushButton_13.setObjectName(u"pushButton_13")
        self.pushButton_13.setStyleSheet(u"color: white;\n"
"background-color: rgb(26, 95, 180);")

        self.gridLayout_20.addWidget(self.pushButton_13, 2, 1, 1, 1)

        self.tabWidget.addTab(self.pagamento_tab, "")

        self.gridLayout_13.addWidget(self.tabWidget, 3, 0, 1, 1)

        self.stacked_principal.addWidget(self.page_4)

        self.gridLayout_2.addWidget(self.stacked_principal, 0, 1, 6, 1)


        self.retranslateUi(Home)

        self.button_bar_inicio.setDefault(False)
        self.stacked_principal.setCurrentIndex(3)
        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Home)
    # setupUi

    def retranslateUi(self, Home):
        self.button_bar_inicio.setText(QCoreApplication.translate("Home", u"Inicio", None))
        self.button_bar_cadastrar.setText(QCoreApplication.translate("Home", u"Cadastro", None))
        self.button_bar_financeiro.setText(QCoreApplication.translate("Home", u"Financeiro", None))
        self.button_bar_aluno.setText(QCoreApplication.translate("Home", u"Aluno", None))
        self.pushButton.setText(QCoreApplication.translate("Home", u"1", None))
        self.label_4.setText(QCoreApplication.translate("Home", u"Endere\u00e7o:", None))
        self.cadastro_nome_lineEdit.setText("")
        self.pushButton_3.setText(QCoreApplication.translate("Home", u"Limpar", None))
        self.cadastro_endereco_lineEdit.setText(QCoreApplication.translate("Home", u"Rua Oscar Pereira de Briro", None))
        self.cadastro_cpf_lineEdit.setText(QCoreApplication.translate("Home", u"888.888.888-11", None))
        self.label_8.setText(QCoreApplication.translate("Home", u"Sexo:", None))
        self.cadastro_sexo_comboBox.setItemText(0, QCoreApplication.translate("Home", u"Selecione", None))
        self.cadastro_sexo_comboBox.setItemText(1, QCoreApplication.translate("Home", u"Masculino", None))
        self.cadastro_sexo_comboBox.setItemText(2, QCoreApplication.translate("Home", u"Feminino", None))
        self.cadastro_sexo_comboBox.setItemText(3, QCoreApplication.translate("Home", u"Outro", None))

        self.button_cadastrar_cliente.setText(QCoreApplication.translate("Home", u"Cadastrar Cliente", None))
        self.cadastro_nascimento_lineEdit.setText(QCoreApplication.translate("Home", u"12/12/1993", None))
        self.cadastro_email_lineEdit.setText(QCoreApplication.translate("Home", u"email.escolhido@gmail.com", None))
        self.label.setText(QCoreApplication.translate("Home", u"Cadastro de clientes:", None))
        self.label_10.setText(QCoreApplication.translate("Home", u"Data de Nascimento:", None))
        self.label_6.setText(QCoreApplication.translate("Home", u"Numero:", None))
        self.label_9.setText(QCoreApplication.translate("Home", u"Complemento:", None))
        self.label_3.setText(QCoreApplication.translate("Home", u"Nome:", None))
        self.label_11.setText(QCoreApplication.translate("Home", u"Email:", None))
        self.cadastro_telefone_lineEdit.setText(QCoreApplication.translate("Home", u"(67) 9 99999999", None))
        self.label_7.setText(QCoreApplication.translate("Home", u"CPF:", None))
        self.cadastro_bairro_lineEdit.setText(QCoreApplication.translate("Home", u"S\u00e3o Bento", None))
        self.label_12.setText(QCoreApplication.translate("Home", u"Telefone:", None))
        self.label_5.setText(QCoreApplication.translate("Home", u"Bairro:", None))
        self.cadastro_numero_lineEdit.setText(QCoreApplication.translate("Home", u"223", None))
        self.cadastro_complemento_lineEdit.setText(QCoreApplication.translate("Home", u"Casa", None))
        self.label_13.setText(QCoreApplication.translate("Home", u" Foto", None))
        self.label_14.setText(QCoreApplication.translate("Home", u"Pagamento:", None))
        self.label_21.setText(QCoreApplication.translate("Home", u"Status:", None))
        self.pushButton_2.setText(QCoreApplication.translate("Home", u"Efetuar pagamento", None))
        self.label_18.setText(QCoreApplication.translate("Home", u"CPF:", None))
        self.label_20.setText(QCoreApplication.translate("Home", u"Vencimento:", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("Home", u"Diario", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("Home", u"Mensal", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("Home", u"Trimestral", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("Home", u"Semestral", None))
        self.comboBox.setItemText(4, QCoreApplication.translate("Home", u"Anual", None))

        self.label_17.setText(QCoreApplication.translate("Home", u"Nome:", None))
        self.label_19.setText(QCoreApplication.translate("Home", u"Plano:", None))
        self.label_24.setText(QCoreApplication.translate("Home", u"Valor a pagar:", None))
        self.label_15.setText(QCoreApplication.translate("Home", u"Nome:", None))
        self.pushButton_6.setText(QCoreApplication.translate("Home", u"Limpar", None))
        self.button_financeiro_pesquisar.setText(QCoreApplication.translate("Home", u"Pesquisar", None))
        self.pushButton_7.setText(QCoreApplication.translate("Home", u"Limpar", None))
        self.pushButton_4.setText(QCoreApplication.translate("Home", u"Pesquisar", None))
        self.label_16.setText(QCoreApplication.translate("Home", u"Matricula:", None))
        self.btn_aluno_pesquisa.setText(QCoreApplication.translate("Home", u"Buscar", None))
        self.label_23.setText(QCoreApplication.translate("Home", u"Matricula", None))
        self.label_22.setText(QCoreApplication.translate("Home", u"Nome:", None))
        self.pushButton_8.setText(QCoreApplication.translate("Home", u"Buscar", None))
        self.btn_aluno_salvar.setText(QCoreApplication.translate("Home", u"Salvar", None))
        self.pushButton_12.setText(QCoreApplication.translate("Home", u"Cancelar", None))
        self.label_25.setText(QCoreApplication.translate("Home", u"Foto", None))
        self.pushButton_10.setText(QCoreApplication.translate("Home", u"Salvar Foto", None))
        self.pushButton_11.setText(QCoreApplication.translate("Home", u"Escolher Foto", None))
        self.label_29.setText(QCoreApplication.translate("Home", u"Email:", None))
        self.label_27.setText(QCoreApplication.translate("Home", u"CPF:", None))
        self.label_28.setText(QCoreApplication.translate("Home", u"Data Nascimento:", None))
        self.label_32.setText(QCoreApplication.translate("Home", u"Complemento:", None))
        self.label_26.setText(QCoreApplication.translate("Home", u"Nome:", None))
        self.label_31.setText(QCoreApplication.translate("Home", u"Numero:", None))
        self.label_33.setText(QCoreApplication.translate("Home", u"Sexo:", None))
        self.label_36.setText(QCoreApplication.translate("Home", u"Bairro:", None))
        self.label_2.setText(QCoreApplication.translate("Home", u"Matricula:", None))
        self.label_30.setText(QCoreApplication.translate("Home", u"Endere\u00e7o:", None))
        self.label_37.setText(QCoreApplication.translate("Home", u"Telefone:", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Perfil_tab), QCoreApplication.translate("Home", u"Perfil", None))
        self.label_35.setText(QCoreApplication.translate("Home", u"Dia do vencimento:", None))
        self.label_34.setText(QCoreApplication.translate("Home", u"Tipo de plano:", None))
        self.comboBox_3.setItemText(0, QCoreApplication.translate("Home", u"Selecione:", None))
        self.comboBox_3.setItemText(1, QCoreApplication.translate("Home", u"Diario", None))
        self.comboBox_3.setItemText(2, QCoreApplication.translate("Home", u"Mensal", None))
        self.comboBox_3.setItemText(3, QCoreApplication.translate("Home", u"Trimestral", None))
        self.comboBox_3.setItemText(4, QCoreApplication.translate("Home", u"Semestral", None))
        self.comboBox_3.setItemText(5, QCoreApplication.translate("Home", u"Anual", None))

        self.dateEdit.setDisplayFormat(QCoreApplication.translate("Home", u"dd", None))
        self.pushButton_13.setText(QCoreApplication.translate("Home", u"Salvar", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.pagamento_tab), QCoreApplication.translate("Home", u"Plano", None))
        pass
    # retranslateUi

