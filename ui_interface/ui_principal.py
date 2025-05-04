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
    QStackedWidget, QTabWidget, QWidget)

class Ui_Principal(object):
    def setupUi(self, Principal):
        if not Principal.objectName():
            Principal.setObjectName(u"Principal")
        Principal.setWindowModality(Qt.WindowModality.WindowModal)
        Principal.setEnabled(True)
        Principal.resize(1121, 881)
        Principal.setWindowTitle(u"SysMar")
        Principal.setStyleSheet(u"background-color: grey;")
        self.gridLayout_2 = QGridLayout(Principal)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setSizeConstraint(QLayout.SizeConstraint.SetNoConstraint)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 1)
        self.stacked_principal = QStackedWidget(Principal)
        self.stacked_principal.setObjectName(u"stacked_principal")
        self.page_inicio = QWidget()
        self.page_inicio.setObjectName(u"page_inicio")
        self.pushButton = QPushButton(self.page_inicio)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(100, 40, 89, 25))
        self.stacked_principal.addWidget(self.page_inicio)
        self.page_cadastro_cliente = QWidget()
        self.page_cadastro_cliente.setObjectName(u"page_cadastro_cliente")
        self.gridLayout_3 = QGridLayout(self.page_cadastro_cliente)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label_4 = QLabel(self.page_cadastro_cliente)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_3.addWidget(self.label_4, 4, 0, 1, 1)

        self.cadastro_nome_lineEdit = QLineEdit(self.page_cadastro_cliente)
        self.cadastro_nome_lineEdit.setObjectName(u"cadastro_nome_lineEdit")
        self.cadastro_nome_lineEdit.setStyleSheet(u"color: white;")

        self.gridLayout_3.addWidget(self.cadastro_nome_lineEdit, 2, 0, 1, 1)

        self.pushButton_3 = QPushButton(self.page_cadastro_cliente)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setMinimumSize(QSize(0, 40))
        self.pushButton_3.setMaximumSize(QSize(200, 16777215))
        self.pushButton_3.setStyleSheet(u"background-color: rgb(192, 28, 40);")

        self.gridLayout_3.addWidget(self.pushButton_3, 12, 1, 1, 1)

        self.cadastro_endereco_lineEdit = QLineEdit(self.page_cadastro_cliente)
        self.cadastro_endereco_lineEdit.setObjectName(u"cadastro_endereco_lineEdit")
        self.cadastro_endereco_lineEdit.setStyleSheet(u"color: white;")

        self.gridLayout_3.addWidget(self.cadastro_endereco_lineEdit, 5, 0, 1, 1)

        self.cadastro_cpf_lineEdit = QLineEdit(self.page_cadastro_cliente)
        self.cadastro_cpf_lineEdit.setObjectName(u"cadastro_cpf_lineEdit")
        self.cadastro_cpf_lineEdit.setStyleSheet(u"color: white;")

        self.gridLayout_3.addWidget(self.cadastro_cpf_lineEdit, 2, 1, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer_2, 13, 0, 1, 1)

        self.label_8 = QLabel(self.page_cadastro_cliente)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_3.addWidget(self.label_8, 1, 2, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)

        self.gridLayout_3.addItem(self.verticalSpacer_4, 6, 0, 1, 1)

        self.verticalSpacer_5 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)

        self.gridLayout_3.addItem(self.verticalSpacer_5, 10, 1, 1, 1)

        self.cadastro_sexo_comboBox = QComboBox(self.page_cadastro_cliente)
        self.cadastro_sexo_comboBox.addItem("")
        self.cadastro_sexo_comboBox.addItem("")
        self.cadastro_sexo_comboBox.addItem("")
        self.cadastro_sexo_comboBox.addItem("")
        self.cadastro_sexo_comboBox.setObjectName(u"cadastro_sexo_comboBox")
        self.cadastro_sexo_comboBox.setMaximumSize(QSize(110, 16777215))
        self.cadastro_sexo_comboBox.setStyleSheet(u"color: white;")

        self.gridLayout_3.addWidget(self.cadastro_sexo_comboBox, 2, 2, 1, 1)

        self.button_cadastrar_cliente = QPushButton(self.page_cadastro_cliente)
        self.button_cadastrar_cliente.setObjectName(u"button_cadastrar_cliente")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_cadastrar_cliente.sizePolicy().hasHeightForWidth())
        self.button_cadastrar_cliente.setSizePolicy(sizePolicy)
        self.button_cadastrar_cliente.setMinimumSize(QSize(0, 40))
        self.button_cadastrar_cliente.setMaximumSize(QSize(200, 40))
        self.button_cadastrar_cliente.setStyleSheet(u"color: white;\n"
"background-color: rgb(26, 95, 180);")

        self.gridLayout_3.addWidget(self.button_cadastrar_cliente, 11, 1, 1, 1)

        self.gridLayout_7 = QGridLayout()
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.cadastro_nascimento_lineEdit = QLineEdit(self.page_cadastro_cliente)
        self.cadastro_nascimento_lineEdit.setObjectName(u"cadastro_nascimento_lineEdit")
        self.cadastro_nascimento_lineEdit.setMaximumSize(QSize(100, 16777215))

        self.gridLayout_7.addWidget(self.cadastro_nascimento_lineEdit, 0, 0, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_7.addItem(self.horizontalSpacer_2, 0, 1, 1, 1)


        self.gridLayout_3.addLayout(self.gridLayout_7, 8, 0, 1, 1)

        self.cadastro_email_lineEdit = QLineEdit(self.page_cadastro_cliente)
        self.cadastro_email_lineEdit.setObjectName(u"cadastro_email_lineEdit")
        self.cadastro_email_lineEdit.setStyleSheet(u"color: white;")

        self.gridLayout_3.addWidget(self.cadastro_email_lineEdit, 8, 1, 1, 1)

        self.label = QLabel(self.page_cadastro_cliente)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(20)
        self.label.setFont(font)

        self.gridLayout_3.addWidget(self.label, 0, 0, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer, 0, 1, 1, 1)

        self.label_10 = QLabel(self.page_cadastro_cliente)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout_3.addWidget(self.label_10, 7, 0, 1, 1)

        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.label_6 = QLabel(self.page_cadastro_cliente)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMaximumSize(QSize(60, 16777215))

        self.gridLayout_5.addWidget(self.label_6, 0, 0, 1, 1)

        self.label_9 = QLabel(self.page_cadastro_cliente)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout_5.addWidget(self.label_9, 0, 1, 1, 1)


        self.gridLayout_3.addLayout(self.gridLayout_5, 4, 1, 1, 1)

        self.label_3 = QLabel(self.page_cadastro_cliente)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_3.addWidget(self.label_3, 1, 0, 1, 1)

        self.label_11 = QLabel(self.page_cadastro_cliente)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout_3.addWidget(self.label_11, 7, 1, 1, 1)

        self.cadastro_telefone_lineEdit = QLineEdit(self.page_cadastro_cliente)
        self.cadastro_telefone_lineEdit.setObjectName(u"cadastro_telefone_lineEdit")
        self.cadastro_telefone_lineEdit.setStyleSheet(u"color: white;")

        self.gridLayout_3.addWidget(self.cadastro_telefone_lineEdit, 8, 2, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)

        self.gridLayout_3.addItem(self.verticalSpacer_3, 3, 0, 1, 1)

        self.label_7 = QLabel(self.page_cadastro_cliente)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_3.addWidget(self.label_7, 1, 1, 1, 1)

        self.cadastro_bairro_lineEdit = QLineEdit(self.page_cadastro_cliente)
        self.cadastro_bairro_lineEdit.setObjectName(u"cadastro_bairro_lineEdit")
        self.cadastro_bairro_lineEdit.setStyleSheet(u"color: white;")

        self.gridLayout_3.addWidget(self.cadastro_bairro_lineEdit, 5, 2, 1, 1)

        self.label_12 = QLabel(self.page_cadastro_cliente)
        self.label_12.setObjectName(u"label_12")

        self.gridLayout_3.addWidget(self.label_12, 7, 2, 1, 1)

        self.label_5 = QLabel(self.page_cadastro_cliente)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_3.addWidget(self.label_5, 4, 2, 1, 1)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.cadastro_numero_lineEdit = QLineEdit(self.page_cadastro_cliente)
        self.cadastro_numero_lineEdit.setObjectName(u"cadastro_numero_lineEdit")
        self.cadastro_numero_lineEdit.setMaximumSize(QSize(60, 16777215))

        self.gridLayout.addWidget(self.cadastro_numero_lineEdit, 0, 0, 1, 1)

        self.cadastro_complemento_lineEdit = QLineEdit(self.page_cadastro_cliente)
        self.cadastro_complemento_lineEdit.setObjectName(u"cadastro_complemento_lineEdit")

        self.gridLayout.addWidget(self.cadastro_complemento_lineEdit, 0, 1, 1, 1)


        self.gridLayout_3.addLayout(self.gridLayout, 5, 1, 1, 1)

        self.stacked_principal.addWidget(self.page_cadastro_cliente)
        self.page_financeiro = QWidget()
        self.page_financeiro.setObjectName(u"page_financeiro")
        self.gridLayout_6 = QGridLayout(self.page_financeiro)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.label_14 = QLabel(self.page_financeiro)
        self.label_14.setObjectName(u"label_14")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_14.sizePolicy().hasHeightForWidth())
        self.label_14.setSizePolicy(sizePolicy1)
        self.label_14.setMinimumSize(QSize(100, 0))
        self.label_14.setFont(font)

        self.gridLayout_6.addWidget(self.label_14, 0, 0, 1, 1)

        self.gridLayout_25 = QGridLayout()
        self.gridLayout_25.setObjectName(u"gridLayout_25")
        self.btn_financeiro_efetuarPagamento = QPushButton(self.page_financeiro)
        self.btn_financeiro_efetuarPagamento.setObjectName(u"btn_financeiro_efetuarPagamento")
        self.btn_financeiro_efetuarPagamento.setStyleSheet(u"color: white;\n"
"background-color: rgb(26, 95, 180);")

        self.gridLayout_25.addWidget(self.btn_financeiro_efetuarPagamento, 0, 0, 1, 1)

        self.horizontalSpacer_16 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_25.addItem(self.horizontalSpacer_16, 0, 2, 1, 1)

        self.pushButton_5 = QPushButton(self.page_financeiro)
        self.pushButton_5.setObjectName(u"pushButton_5")

        self.gridLayout_25.addWidget(self.pushButton_5, 0, 1, 1, 1)


        self.gridLayout_6.addLayout(self.gridLayout_25, 3, 1, 1, 1)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_6.addItem(self.verticalSpacer_6, 6, 0, 1, 1)

        self.verticalSpacer_8 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_6.addItem(self.verticalSpacer_8, 4, 1, 1, 1)

        self.gridLayout_11 = QGridLayout()
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.gridLayout_19 = QGridLayout()
        self.gridLayout_19.setObjectName(u"gridLayout_19")
        self.comboBox_financeiro_plano = QComboBox(self.page_financeiro)
        self.comboBox_financeiro_plano.addItem("")
        self.comboBox_financeiro_plano.addItem("")
        self.comboBox_financeiro_plano.addItem("")
        self.comboBox_financeiro_plano.addItem("")
        self.comboBox_financeiro_plano.addItem("")
        self.comboBox_financeiro_plano.setObjectName(u"comboBox_financeiro_plano")

        self.gridLayout_19.addWidget(self.comboBox_financeiro_plano, 0, 0, 1, 1)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_19.addItem(self.horizontalSpacer_8, 0, 1, 1, 1)


        self.gridLayout_11.addLayout(self.gridLayout_19, 2, 1, 1, 1)

        self.lineEdit_financeiro_nome = QLineEdit(self.page_financeiro)
        self.lineEdit_financeiro_nome.setObjectName(u"lineEdit_financeiro_nome")
        sizePolicy1.setHeightForWidth(self.lineEdit_financeiro_nome.sizePolicy().hasHeightForWidth())
        self.lineEdit_financeiro_nome.setSizePolicy(sizePolicy1)
        self.lineEdit_financeiro_nome.setMaximumSize(QSize(400, 16777215))

        self.gridLayout_11.addWidget(self.lineEdit_financeiro_nome, 0, 1, 1, 1)

        self.gridLayout_23 = QGridLayout()
        self.gridLayout_23.setObjectName(u"gridLayout_23")
        self.dateEdit_financeiro_vencimento = QDateEdit(self.page_financeiro)
        self.dateEdit_financeiro_vencimento.setObjectName(u"dateEdit_financeiro_vencimento")
        self.dateEdit_financeiro_vencimento.setCalendarPopup(True)

        self.gridLayout_23.addWidget(self.dateEdit_financeiro_vencimento, 0, 0, 1, 1)

        self.horizontalSpacer_14 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_23.addItem(self.horizontalSpacer_14, 0, 1, 1, 1)


        self.gridLayout_11.addLayout(self.gridLayout_23, 2, 3, 1, 1)

        self.gridLayout_21 = QGridLayout()
        self.gridLayout_21.setObjectName(u"gridLayout_21")
        self.comboBox_financeiro_status = QComboBox(self.page_financeiro)
        self.comboBox_financeiro_status.addItem("")
        self.comboBox_financeiro_status.addItem("")
        self.comboBox_financeiro_status.addItem("")
        self.comboBox_financeiro_status.setObjectName(u"comboBox_financeiro_status")

        self.gridLayout_21.addWidget(self.comboBox_financeiro_status, 0, 2, 1, 1)

        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_21.addItem(self.horizontalSpacer_12, 0, 3, 1, 1)


        self.gridLayout_11.addLayout(self.gridLayout_21, 4, 1, 1, 1)

        self.label_17 = QLabel(self.page_financeiro)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setMaximumSize(QSize(100, 16777215))

        self.gridLayout_11.addWidget(self.label_17, 0, 0, 1, 1)

        self.label_19 = QLabel(self.page_financeiro)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setMaximumSize(QSize(100, 16777215))

        self.gridLayout_11.addWidget(self.label_19, 2, 0, 1, 1)

        self.label_18 = QLabel(self.page_financeiro)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setMaximumSize(QSize(100, 16777215))
        self.label_18.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.label_18.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_11.addWidget(self.label_18, 0, 2, 1, 1)

        self.label_20 = QLabel(self.page_financeiro)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setMaximumSize(QSize(100, 16777215))
        self.label_20.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.label_20.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_11.addWidget(self.label_20, 2, 2, 1, 1)

        self.label_21 = QLabel(self.page_financeiro)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setMaximumSize(QSize(100, 16777215))

        self.gridLayout_11.addWidget(self.label_21, 4, 0, 1, 1)

        self.label_24 = QLabel(self.page_financeiro)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setMaximumSize(QSize(100, 16777215))
        self.label_24.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.label_24.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_11.addWidget(self.label_24, 4, 2, 1, 1)

        self.gridLayout_22 = QGridLayout()
        self.gridLayout_22.setObjectName(u"gridLayout_22")
        self.lineEdit_financeiro_cpf = QLineEdit(self.page_financeiro)
        self.lineEdit_financeiro_cpf.setObjectName(u"lineEdit_financeiro_cpf")

        self.gridLayout_22.addWidget(self.lineEdit_financeiro_cpf, 0, 0, 1, 1)

        self.horizontalSpacer_13 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_22.addItem(self.horizontalSpacer_13, 0, 1, 1, 1)


        self.gridLayout_11.addLayout(self.gridLayout_22, 0, 3, 1, 1)

        self.gridLayout_24 = QGridLayout()
        self.gridLayout_24.setObjectName(u"gridLayout_24")
        self.gridLayout_24.setHorizontalSpacing(0)
        self.horizontalSpacer_15 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_24.addItem(self.horizontalSpacer_15, 1, 1, 1, 1)

        self.lineEdit_financeiro_valorApagar = QLineEdit(self.page_financeiro)
        self.lineEdit_financeiro_valorApagar.setObjectName(u"lineEdit_financeiro_valorApagar")

        self.gridLayout_24.addWidget(self.lineEdit_financeiro_valorApagar, 1, 0, 1, 1)


        self.gridLayout_11.addLayout(self.gridLayout_24, 4, 3, 1, 1)


        self.gridLayout_6.addLayout(self.gridLayout_11, 2, 1, 1, 1)

        self.label_13 = QLabel(self.page_financeiro)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setMinimumSize(QSize(85, 113))
        self.label_13.setMaximumSize(QSize(85, 113))
        self.label_13.setStyleSheet(u"background-color: rgb(153, 193, 241);")
        self.label_13.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_6.addWidget(self.label_13, 1, 0, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.gridLayout_6.addItem(self.horizontalSpacer_3, 0, 1, 1, 1)

        self.gridLayout_8 = QGridLayout()
        self.gridLayout_8.setSpacing(0)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_10 = QGridLayout()
        self.gridLayout_10.setSpacing(0)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.label_15 = QLabel(self.page_financeiro)
        self.label_15.setObjectName(u"label_15")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_15.sizePolicy().hasHeightForWidth())
        self.label_15.setSizePolicy(sizePolicy2)
        self.label_15.setMaximumSize(QSize(16777215, 30))
        self.label_15.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_10.addWidget(self.label_15, 0, 0, 1, 1)


        self.gridLayout_8.addLayout(self.gridLayout_10, 0, 0, 1, 1)

        self.gridLayout_nome = QGridLayout()
        self.gridLayout_nome.setSpacing(0)
        self.gridLayout_nome.setObjectName(u"gridLayout_nome")
        self.gridLayout_nome.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_nome.addItem(self.horizontalSpacer_6, 0, 3, 1, 1)

        self.lineEdit_pesquisa_cliente = QLineEdit(self.page_financeiro)
        self.lineEdit_pesquisa_cliente.setObjectName(u"lineEdit_pesquisa_cliente")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.lineEdit_pesquisa_cliente.sizePolicy().hasHeightForWidth())
        self.lineEdit_pesquisa_cliente.setSizePolicy(sizePolicy3)
        self.lineEdit_pesquisa_cliente.setMinimumSize(QSize(400, 0))

        self.gridLayout_nome.addWidget(self.lineEdit_pesquisa_cliente, 0, 0, 1, 1)

        self.pushButton_6 = QPushButton(self.page_financeiro)
        self.pushButton_6.setObjectName(u"pushButton_6")

        self.gridLayout_nome.addWidget(self.pushButton_6, 0, 2, 1, 1)

        self.btn_financeiro_pesquisar = QPushButton(self.page_financeiro)
        self.btn_financeiro_pesquisar.setObjectName(u"btn_financeiro_pesquisar")
        sizePolicy3.setHeightForWidth(self.btn_financeiro_pesquisar.sizePolicy().hasHeightForWidth())
        self.btn_financeiro_pesquisar.setSizePolicy(sizePolicy3)
        self.btn_financeiro_pesquisar.setStyleSheet(u"color: white;\n"
"background-color: rgb(26, 95, 180);")

        self.gridLayout_nome.addWidget(self.btn_financeiro_pesquisar, 0, 1, 1, 1)


        self.gridLayout_8.addLayout(self.gridLayout_nome, 0, 1, 1, 1)

        self.gridLayout_9 = QGridLayout()
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.pushButton_7 = QPushButton(self.page_financeiro)
        self.pushButton_7.setObjectName(u"pushButton_7")

        self.gridLayout_9.addWidget(self.pushButton_7, 0, 2, 1, 1)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_9.addItem(self.horizontalSpacer_5, 0, 3, 1, 1)

        self.pushButton_4 = QPushButton(self.page_financeiro)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setStyleSheet(u"color: white;\n"
"background-color: rgb(26, 95, 180);")

        self.gridLayout_9.addWidget(self.pushButton_4, 0, 1, 1, 1)

        self.lineEdit_pesquisa_id = QLineEdit(self.page_financeiro)
        self.lineEdit_pesquisa_id.setObjectName(u"lineEdit_pesquisa_id")
        sizePolicy3.setHeightForWidth(self.lineEdit_pesquisa_id.sizePolicy().hasHeightForWidth())
        self.lineEdit_pesquisa_id.setSizePolicy(sizePolicy3)

        self.gridLayout_9.addWidget(self.lineEdit_pesquisa_id, 0, 0, 1, 1)


        self.gridLayout_8.addLayout(self.gridLayout_9, 1, 1, 1, 1)

        self.label_16 = QLabel(self.page_financeiro)
        self.label_16.setObjectName(u"label_16")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.label_16.sizePolicy().hasHeightForWidth())
        self.label_16.setSizePolicy(sizePolicy4)
        self.label_16.setMaximumSize(QSize(16777215, 20))

        self.gridLayout_8.addWidget(self.label_16, 1, 0, 1, 1)


        self.gridLayout_6.addLayout(self.gridLayout_8, 1, 1, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_6.addItem(self.horizontalSpacer_4, 5, 1, 1, 1)

        self.stacked_principal.addWidget(self.page_financeiro)
        self.page_aluno = QWidget()
        self.page_aluno.setObjectName(u"page_aluno")
        self.gridLayout_13 = QGridLayout(self.page_aluno)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.gridLayout_12 = QGridLayout()
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.gridLayout_14 = QGridLayout()
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.pushButton_8 = QPushButton(self.page_aluno)
        self.pushButton_8.setObjectName(u"pushButton_8")
        sizePolicy3.setHeightForWidth(self.pushButton_8.sizePolicy().hasHeightForWidth())
        self.pushButton_8.setSizePolicy(sizePolicy3)
        self.pushButton_8.setStyleSheet(u"color: white;\n"
"background-color: rgb(26, 95, 180);")

        self.gridLayout_14.addWidget(self.pushButton_8, 3, 1, 1, 1)

        self.btn_aluno_pesquisa = QPushButton(self.page_aluno)
        self.btn_aluno_pesquisa.setObjectName(u"btn_aluno_pesquisa")
        sizePolicy3.setHeightForWidth(self.btn_aluno_pesquisa.sizePolicy().hasHeightForWidth())
        self.btn_aluno_pesquisa.setSizePolicy(sizePolicy3)
        self.btn_aluno_pesquisa.setStyleSheet(u"color: white;\n"
"background-color: rgb(26, 95, 180);")

        self.gridLayout_14.addWidget(self.btn_aluno_pesquisa, 1, 1, 1, 1)

        self.label_23 = QLabel(self.page_aluno)
        self.label_23.setObjectName(u"label_23")

        self.gridLayout_14.addWidget(self.label_23, 2, 0, 1, 1)

        self.label_22 = QLabel(self.page_aluno)
        self.label_22.setObjectName(u"label_22")

        self.gridLayout_14.addWidget(self.label_22, 0, 0, 1, 1)

        self.lineEdit_5 = QLineEdit(self.page_aluno)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setMaximumSize(QSize(200, 16777215))

        self.gridLayout_14.addWidget(self.lineEdit_5, 2, 1, 1, 1)

        self.lineEdit_aluno_pesquisa_nome = QLineEdit(self.page_aluno)
        self.lineEdit_aluno_pesquisa_nome.setObjectName(u"lineEdit_aluno_pesquisa_nome")

        self.gridLayout_14.addWidget(self.lineEdit_aluno_pesquisa_nome, 0, 1, 1, 1)


        self.gridLayout_12.addLayout(self.gridLayout_14, 0, 0, 1, 1)


        self.gridLayout_13.addLayout(self.gridLayout_12, 0, 0, 1, 1)

        self.tabWidget = QTabWidget(self.page_aluno)
        self.tabWidget.setObjectName(u"tabWidget")
        self.Perfil_tab = QWidget()
        self.Perfil_tab.setObjectName(u"Perfil_tab")
        self.gridLayout_16 = QGridLayout(self.Perfil_tab)
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        self.gridLayout_18 = QGridLayout()
        self.gridLayout_18.setObjectName(u"gridLayout_18")
        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_18.addItem(self.horizontalSpacer_9, 0, 2, 1, 1)

        self.pushButton_12 = QPushButton(self.Perfil_tab)
        self.pushButton_12.setObjectName(u"pushButton_12")
        sizePolicy3.setHeightForWidth(self.pushButton_12.sizePolicy().hasHeightForWidth())
        self.pushButton_12.setSizePolicy(sizePolicy3)

        self.gridLayout_18.addWidget(self.pushButton_12, 0, 1, 1, 1)

        self.btn_aluno_salvar = QPushButton(self.Perfil_tab)
        self.btn_aluno_salvar.setObjectName(u"btn_aluno_salvar")
        sizePolicy3.setHeightForWidth(self.btn_aluno_salvar.sizePolicy().hasHeightForWidth())
        self.btn_aluno_salvar.setSizePolicy(sizePolicy3)
        self.btn_aluno_salvar.setStyleSheet(u"color: white;\n"
"background-color: rgb(26, 95, 180);")

        self.gridLayout_18.addWidget(self.btn_aluno_salvar, 0, 0, 1, 1)


        self.gridLayout_16.addLayout(self.gridLayout_18, 2, 0, 1, 1)

        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_16.addItem(self.verticalSpacer_7, 3, 0, 1, 1)

        self.gridLayout_15 = QGridLayout()
        self.gridLayout_15.setSpacing(0)
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.gridLayout_15.setSizeConstraint(QLayout.SizeConstraint.SetFixedSize)
        self.label_25 = QLabel(self.Perfil_tab)
        self.label_25.setObjectName(u"label_25")
        sizePolicy3.setHeightForWidth(self.label_25.sizePolicy().hasHeightForWidth())
        self.label_25.setSizePolicy(sizePolicy3)
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
        self.label_29 = QLabel(self.Perfil_tab)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setMaximumSize(QSize(100, 16777215))

        self.gridLayout_17.addWidget(self.label_29, 4, 0, 1, 1)

        self.lineEdit_aluno_bairro = QLineEdit(self.Perfil_tab)
        self.lineEdit_aluno_bairro.setObjectName(u"lineEdit_aluno_bairro")
        self.lineEdit_aluno_bairro.setMaximumSize(QSize(300, 16777215))

        self.gridLayout_17.addWidget(self.lineEdit_aluno_bairro, 7, 1, 1, 1)

        self.lineEdit_aluno_nascimento = QLineEdit(self.Perfil_tab)
        self.lineEdit_aluno_nascimento.setObjectName(u"lineEdit_aluno_nascimento")
        self.lineEdit_aluno_nascimento.setMaximumSize(QSize(300, 16777215))

        self.gridLayout_17.addWidget(self.lineEdit_aluno_nascimento, 3, 1, 1, 1)

        self.label_2 = QLabel(self.Perfil_tab)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(100, 16777215))

        self.gridLayout_17.addWidget(self.label_2, 0, 0, 1, 1)

        self.comboBox_aluno_sexo = QComboBox(self.Perfil_tab)
        self.comboBox_aluno_sexo.addItem("")
        self.comboBox_aluno_sexo.addItem("")
        self.comboBox_aluno_sexo.addItem("")
        self.comboBox_aluno_sexo.setObjectName(u"comboBox_aluno_sexo")

        self.gridLayout_17.addWidget(self.comboBox_aluno_sexo, 10, 1, 1, 1)

        self.lineEdit_aluno_numero = QLineEdit(self.Perfil_tab)
        self.lineEdit_aluno_numero.setObjectName(u"lineEdit_aluno_numero")
        self.lineEdit_aluno_numero.setMaximumSize(QSize(300, 16777215))

        self.gridLayout_17.addWidget(self.lineEdit_aluno_numero, 8, 1, 1, 1)

        self.lineEdit_aluno_endereco = QLineEdit(self.Perfil_tab)
        self.lineEdit_aluno_endereco.setObjectName(u"lineEdit_aluno_endereco")
        self.lineEdit_aluno_endereco.setMaximumSize(QSize(300, 16777215))

        self.gridLayout_17.addWidget(self.lineEdit_aluno_endereco, 6, 1, 1, 1)

        self.lineEdit_aluno_telefone = QLineEdit(self.Perfil_tab)
        self.lineEdit_aluno_telefone.setObjectName(u"lineEdit_aluno_telefone")
        self.lineEdit_aluno_telefone.setMaximumSize(QSize(300, 16777215))

        self.gridLayout_17.addWidget(self.lineEdit_aluno_telefone, 5, 1, 1, 1)

        self.lineEdit_aluno_cpf = QLineEdit(self.Perfil_tab)
        self.lineEdit_aluno_cpf.setObjectName(u"lineEdit_aluno_cpf")
        self.lineEdit_aluno_cpf.setMaximumSize(QSize(300, 16777215))

        self.gridLayout_17.addWidget(self.lineEdit_aluno_cpf, 2, 1, 1, 1)

        self.lineEdit_aluno_email = QLineEdit(self.Perfil_tab)
        self.lineEdit_aluno_email.setObjectName(u"lineEdit_aluno_email")
        self.lineEdit_aluno_email.setMaximumSize(QSize(300, 16777215))

        self.gridLayout_17.addWidget(self.lineEdit_aluno_email, 4, 1, 1, 1)

        self.lineEdit_aluno_matricula = QLineEdit(self.Perfil_tab)
        self.lineEdit_aluno_matricula.setObjectName(u"lineEdit_aluno_matricula")
        self.lineEdit_aluno_matricula.setMaximumSize(QSize(300, 16777215))

        self.gridLayout_17.addWidget(self.lineEdit_aluno_matricula, 0, 1, 1, 1)

        self.label_31 = QLabel(self.Perfil_tab)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setMaximumSize(QSize(100, 16777215))

        self.gridLayout_17.addWidget(self.label_31, 8, 0, 1, 1)

        self.label_36 = QLabel(self.Perfil_tab)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setMaximumSize(QSize(100, 16777215))

        self.gridLayout_17.addWidget(self.label_36, 7, 0, 1, 1)

        self.label_32 = QLabel(self.Perfil_tab)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setMaximumSize(QSize(100, 16777215))

        self.gridLayout_17.addWidget(self.label_32, 9, 0, 1, 1)

        self.label_37 = QLabel(self.Perfil_tab)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setMaximumSize(QSize(100, 16777215))

        self.gridLayout_17.addWidget(self.label_37, 5, 0, 1, 1)

        self.label_30 = QLabel(self.Perfil_tab)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setMaximumSize(QSize(100, 16777215))

        self.gridLayout_17.addWidget(self.label_30, 6, 0, 1, 1)

        self.lineEdit_aluno_complemento = QLineEdit(self.Perfil_tab)
        self.lineEdit_aluno_complemento.setObjectName(u"lineEdit_aluno_complemento")
        self.lineEdit_aluno_complemento.setMaximumSize(QSize(300, 16777215))

        self.gridLayout_17.addWidget(self.lineEdit_aluno_complemento, 9, 1, 1, 1)

        self.label_26 = QLabel(self.Perfil_tab)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setMaximumSize(QSize(100, 16777215))

        self.gridLayout_17.addWidget(self.label_26, 1, 0, 1, 1)

        self.label_28 = QLabel(self.Perfil_tab)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setMaximumSize(QSize(100, 16777215))

        self.gridLayout_17.addWidget(self.label_28, 3, 0, 1, 1)

        self.lineEdit_aluno_nome = QLineEdit(self.Perfil_tab)
        self.lineEdit_aluno_nome.setObjectName(u"lineEdit_aluno_nome")
        self.lineEdit_aluno_nome.setMaximumSize(QSize(300, 16777215))

        self.gridLayout_17.addWidget(self.lineEdit_aluno_nome, 1, 1, 1, 1)

        self.label_33 = QLabel(self.Perfil_tab)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setMaximumSize(QSize(100, 16777215))

        self.gridLayout_17.addWidget(self.label_33, 10, 0, 1, 1)

        self.label_27 = QLabel(self.Perfil_tab)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setMaximumSize(QSize(100, 16777215))

        self.gridLayout_17.addWidget(self.label_27, 2, 0, 1, 1)

        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_17.addItem(self.horizontalSpacer_11, 0, 2, 1, 1)


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
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.label_34.sizePolicy().hasHeightForWidth())
        self.label_34.setSizePolicy(sizePolicy5)

        self.gridLayout_20.addWidget(self.label_34, 0, 0, 1, 1)

        self.comboBox_3 = QComboBox(self.pagamento_tab)
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.setObjectName(u"comboBox_3")
        sizePolicy3.setHeightForWidth(self.comboBox_3.sizePolicy().hasHeightForWidth())
        self.comboBox_3.setSizePolicy(sizePolicy3)
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

        self.stacked_principal.addWidget(self.page_aluno)

        self.gridLayout_2.addWidget(self.stacked_principal, 0, 1, 6, 1)

        self.frame_sidebar = QFrame(Principal)
        self.frame_sidebar.setObjectName(u"frame_sidebar")
        self.frame_sidebar.setStyleSheet(u"background-color: rgb(94, 92, 100);")
        self.frame_sidebar.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_sidebar.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_4 = QGridLayout(self.frame_sidebar)
        self.gridLayout_4.setSpacing(0)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.sidebar_grid = QGridLayout()
        self.sidebar_grid.setObjectName(u"sidebar_grid")
        self.sidebar_grid.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.sidebar_grid.setContentsMargins(0, -1, -1, -1)
        self.button_bar_inicio = QPushButton(self.frame_sidebar)
        self.button_bar_inicio.setObjectName(u"button_bar_inicio")
        sizePolicy6 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.button_bar_inicio.sizePolicy().hasHeightForWidth())
        self.button_bar_inicio.setSizePolicy(sizePolicy6)
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

        self.sidebar_grid.addWidget(self.button_bar_inicio, 0, 0, 1, 1)

        self.button_bar_cadastrar = QPushButton(self.frame_sidebar)
        self.button_bar_cadastrar.setObjectName(u"button_bar_cadastrar")
        sizePolicy6.setHeightForWidth(self.button_bar_cadastrar.sizePolicy().hasHeightForWidth())
        self.button_bar_cadastrar.setSizePolicy(sizePolicy6)
        self.button_bar_cadastrar.setMinimumSize(QSize(0, 0))
        self.button_bar_cadastrar.setMaximumSize(QSize(500, 60))
        self.button_bar_cadastrar.setSizeIncrement(QSize(0, 0))
        self.button_bar_cadastrar.setStyleSheet(u"background-color: rgb(26, 95, 180);\n"
"border: none;\n"
"color: white;")

        self.sidebar_grid.addWidget(self.button_bar_cadastrar, 1, 0, 1, 1)

        self.button_bar_financeiro = QPushButton(self.frame_sidebar)
        self.button_bar_financeiro.setObjectName(u"button_bar_financeiro")
        sizePolicy6.setHeightForWidth(self.button_bar_financeiro.sizePolicy().hasHeightForWidth())
        self.button_bar_financeiro.setSizePolicy(sizePolicy6)
        self.button_bar_financeiro.setMinimumSize(QSize(0, 0))
        self.button_bar_financeiro.setMaximumSize(QSize(500, 60))
        self.button_bar_financeiro.setSizeIncrement(QSize(0, 0))
        self.button_bar_financeiro.setStyleSheet(u"background-color: rgb(26, 95, 180);\n"
"border: none;\n"
"color: white;")

        self.sidebar_grid.addWidget(self.button_bar_financeiro, 2, 0, 1, 1)

        self.button_bar_aluno = QPushButton(self.frame_sidebar)
        self.button_bar_aluno.setObjectName(u"button_bar_aluno")
        sizePolicy6.setHeightForWidth(self.button_bar_aluno.sizePolicy().hasHeightForWidth())
        self.button_bar_aluno.setSizePolicy(sizePolicy6)
        self.button_bar_aluno.setMinimumSize(QSize(0, 0))
        self.button_bar_aluno.setMaximumSize(QSize(500, 60))
        self.button_bar_aluno.setSizeIncrement(QSize(0, 0))
        self.button_bar_aluno.setStyleSheet(u"background-color: rgb(26, 95, 180);\n"
"border: none;\n"
"color: white;")

        self.sidebar_grid.addWidget(self.button_bar_aluno, 3, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.sidebar_grid.addItem(self.verticalSpacer, 4, 0, 1, 1)


        self.gridLayout_4.addLayout(self.sidebar_grid, 0, 0, 1, 1)


        self.gridLayout_2.addWidget(self.frame_sidebar, 0, 0, 1, 1)


        self.retranslateUi(Principal)

        self.stacked_principal.setCurrentIndex(2)
        self.tabWidget.setCurrentIndex(1)
        self.button_bar_inicio.setDefault(False)


        QMetaObject.connectSlotsByName(Principal)
    # setupUi

    def retranslateUi(self, Principal):
        self.pushButton.setText(QCoreApplication.translate("Principal", u"1", None))
        self.label_4.setText(QCoreApplication.translate("Principal", u"Endere\u00e7o:", None))
        self.cadastro_nome_lineEdit.setText("")
        self.pushButton_3.setText(QCoreApplication.translate("Principal", u"Limpar", None))
        self.cadastro_endereco_lineEdit.setText(QCoreApplication.translate("Principal", u"Rua Oscar Pereira de Briro", None))
        self.cadastro_cpf_lineEdit.setText(QCoreApplication.translate("Principal", u"888.888.888-11", None))
        self.label_8.setText(QCoreApplication.translate("Principal", u"Sexo:", None))
        self.cadastro_sexo_comboBox.setItemText(0, QCoreApplication.translate("Principal", u"Selecione", None))
        self.cadastro_sexo_comboBox.setItemText(1, QCoreApplication.translate("Principal", u"Masculino", None))
        self.cadastro_sexo_comboBox.setItemText(2, QCoreApplication.translate("Principal", u"Feminino", None))
        self.cadastro_sexo_comboBox.setItemText(3, QCoreApplication.translate("Principal", u"Outro", None))

        self.button_cadastrar_cliente.setText(QCoreApplication.translate("Principal", u"Cadastrar Cliente", None))
        self.cadastro_nascimento_lineEdit.setText(QCoreApplication.translate("Principal", u"12/12/1993", None))
        self.cadastro_email_lineEdit.setText(QCoreApplication.translate("Principal", u"email.escolhido@gmail.com", None))
        self.label.setText(QCoreApplication.translate("Principal", u"Cadastro de clientes:", None))
        self.label_10.setText(QCoreApplication.translate("Principal", u"Data de Nascimento:", None))
        self.label_6.setText(QCoreApplication.translate("Principal", u"Numero:", None))
        self.label_9.setText(QCoreApplication.translate("Principal", u"Complemento:", None))
        self.label_3.setText(QCoreApplication.translate("Principal", u"Nome:", None))
        self.label_11.setText(QCoreApplication.translate("Principal", u"Email:", None))
        self.cadastro_telefone_lineEdit.setText(QCoreApplication.translate("Principal", u"(67) 9 99999999", None))
        self.label_7.setText(QCoreApplication.translate("Principal", u"CPF:", None))
        self.cadastro_bairro_lineEdit.setText(QCoreApplication.translate("Principal", u"S\u00e3o Bento", None))
        self.label_12.setText(QCoreApplication.translate("Principal", u"Telefone:", None))
        self.label_5.setText(QCoreApplication.translate("Principal", u"Bairro:", None))
        self.cadastro_numero_lineEdit.setText(QCoreApplication.translate("Principal", u"223", None))
        self.cadastro_complemento_lineEdit.setText(QCoreApplication.translate("Principal", u"Casa", None))
        self.label_14.setText(QCoreApplication.translate("Principal", u"Pagamento:", None))
        self.btn_financeiro_efetuarPagamento.setText(QCoreApplication.translate("Principal", u"Efetuar pagamento", None))
        self.pushButton_5.setText(QCoreApplication.translate("Principal", u"Limpar", None))
        self.comboBox_financeiro_plano.setItemText(0, QCoreApplication.translate("Principal", u"Diario", None))
        self.comboBox_financeiro_plano.setItemText(1, QCoreApplication.translate("Principal", u"Mensal", None))
        self.comboBox_financeiro_plano.setItemText(2, QCoreApplication.translate("Principal", u"Trimestral", None))
        self.comboBox_financeiro_plano.setItemText(3, QCoreApplication.translate("Principal", u"Semestral", None))
        self.comboBox_financeiro_plano.setItemText(4, QCoreApplication.translate("Principal", u"Anual", None))

        self.dateEdit_financeiro_vencimento.setDisplayFormat(QCoreApplication.translate("Principal", u"d", None))
        self.comboBox_financeiro_status.setItemText(0, QCoreApplication.translate("Principal", u"Ativo", None))
        self.comboBox_financeiro_status.setItemText(1, QCoreApplication.translate("Principal", u"Inativo", None))
        self.comboBox_financeiro_status.setItemText(2, QCoreApplication.translate("Principal", u"Em debito", None))

        self.label_17.setText(QCoreApplication.translate("Principal", u"Nome:", None))
        self.label_19.setText(QCoreApplication.translate("Principal", u"Plano:", None))
        self.label_18.setText(QCoreApplication.translate("Principal", u"CPF:", None))
        self.label_20.setText(QCoreApplication.translate("Principal", u"Vencimento:", None))
        self.label_21.setText(QCoreApplication.translate("Principal", u"Status:", None))
        self.label_24.setText(QCoreApplication.translate("Principal", u"Valor a pagar:", None))
        self.label_13.setText(QCoreApplication.translate("Principal", u" Foto", None))
        self.label_15.setText(QCoreApplication.translate("Principal", u"Nome: ", None))
        self.pushButton_6.setText(QCoreApplication.translate("Principal", u"Limpar", None))
        self.btn_financeiro_pesquisar.setText(QCoreApplication.translate("Principal", u"Pesquisar", None))
        self.pushButton_7.setText(QCoreApplication.translate("Principal", u"Limpar", None))
        self.pushButton_4.setText(QCoreApplication.translate("Principal", u"Pesquisar", None))
        self.label_16.setText(QCoreApplication.translate("Principal", u"Matricula: ", None))
        self.pushButton_8.setText(QCoreApplication.translate("Principal", u"Buscar", None))
        self.btn_aluno_pesquisa.setText(QCoreApplication.translate("Principal", u"Buscar", None))
        self.label_23.setText(QCoreApplication.translate("Principal", u"Matricula", None))
        self.label_22.setText(QCoreApplication.translate("Principal", u"Nome:", None))
        self.pushButton_12.setText(QCoreApplication.translate("Principal", u"Cancelar", None))
        self.btn_aluno_salvar.setText(QCoreApplication.translate("Principal", u"Salvar", None))
        self.label_25.setText(QCoreApplication.translate("Principal", u"Foto", None))
        self.pushButton_10.setText(QCoreApplication.translate("Principal", u"Salvar Foto", None))
        self.pushButton_11.setText(QCoreApplication.translate("Principal", u"Escolher Foto", None))
        self.label_29.setText(QCoreApplication.translate("Principal", u"Email:", None))
        self.label_2.setText(QCoreApplication.translate("Principal", u"Matricula:", None))
        self.comboBox_aluno_sexo.setItemText(0, QCoreApplication.translate("Principal", u"Masculino", None))
        self.comboBox_aluno_sexo.setItemText(1, QCoreApplication.translate("Principal", u"Feminino", None))
        self.comboBox_aluno_sexo.setItemText(2, QCoreApplication.translate("Principal", u"Outro", None))

        self.label_31.setText(QCoreApplication.translate("Principal", u"Numero:", None))
        self.label_36.setText(QCoreApplication.translate("Principal", u"Bairro:", None))
        self.label_32.setText(QCoreApplication.translate("Principal", u"Complemento:", None))
        self.label_37.setText(QCoreApplication.translate("Principal", u"Telefone:", None))
        self.label_30.setText(QCoreApplication.translate("Principal", u"Endere\u00e7o:", None))
        self.label_26.setText(QCoreApplication.translate("Principal", u"Nome:", None))
        self.label_28.setText(QCoreApplication.translate("Principal", u"Data Nascimento:", None))
        self.label_33.setText(QCoreApplication.translate("Principal", u"Sexo:", None))
        self.label_27.setText(QCoreApplication.translate("Principal", u"CPF:", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Perfil_tab), QCoreApplication.translate("Principal", u"Perfil", None))
        self.label_35.setText(QCoreApplication.translate("Principal", u"Dia do vencimento:", None))
        self.label_34.setText(QCoreApplication.translate("Principal", u"Tipo de plano:", None))
        self.comboBox_3.setItemText(0, QCoreApplication.translate("Principal", u"Selecione:", None))
        self.comboBox_3.setItemText(1, QCoreApplication.translate("Principal", u"Diario", None))
        self.comboBox_3.setItemText(2, QCoreApplication.translate("Principal", u"Mensal", None))
        self.comboBox_3.setItemText(3, QCoreApplication.translate("Principal", u"Trimestral", None))
        self.comboBox_3.setItemText(4, QCoreApplication.translate("Principal", u"Semestral", None))
        self.comboBox_3.setItemText(5, QCoreApplication.translate("Principal", u"Anual", None))

        self.dateEdit.setDisplayFormat(QCoreApplication.translate("Principal", u"dd", None))
        self.pushButton_13.setText(QCoreApplication.translate("Principal", u"Salvar", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.pagamento_tab), QCoreApplication.translate("Principal", u"Plano", None))
        self.button_bar_inicio.setText(QCoreApplication.translate("Principal", u"Inicio", None))
        self.button_bar_cadastrar.setText(QCoreApplication.translate("Principal", u"Cadastro", None))
        self.button_bar_financeiro.setText(QCoreApplication.translate("Principal", u"Financeiro", None))
        self.button_bar_aluno.setText(QCoreApplication.translate("Principal", u"Aluno", None))
        pass
    # retranslateUi

