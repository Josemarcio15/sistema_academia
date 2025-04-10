# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'home.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLayout, QPushButton,
    QSizePolicy, QSpacerItem, QWidget)

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
        self.button_bar_configuracoes = QPushButton(Home)
        self.button_bar_configuracoes.setObjectName(u"button_bar_configuracoes")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_bar_configuracoes.sizePolicy().hasHeightForWidth())
        self.button_bar_configuracoes.setSizePolicy(sizePolicy)
        self.button_bar_configuracoes.setMinimumSize(QSize(0, 0))
        self.button_bar_configuracoes.setMaximumSize(QSize(500, 100))
        self.button_bar_configuracoes.setSizeIncrement(QSize(0, 0))

        self.gridLayout_2.addWidget(self.button_bar_configuracoes, 3, 0, 1, 1)

        self.button_bar_inicio = QPushButton(Home)
        self.button_bar_inicio.setObjectName(u"button_bar_inicio")
        sizePolicy.setHeightForWidth(self.button_bar_inicio.sizePolicy().hasHeightForWidth())
        self.button_bar_inicio.setSizePolicy(sizePolicy)
        self.button_bar_inicio.setMinimumSize(QSize(0, 0))
        self.button_bar_inicio.setMaximumSize(QSize(500, 100))
        self.button_bar_inicio.setSizeIncrement(QSize(0, 0))

        self.gridLayout_2.addWidget(self.button_bar_inicio, 0, 0, 1, 1)

        self.button_bar_cadastrar = QPushButton(Home)
        self.button_bar_cadastrar.setObjectName(u"button_bar_cadastrar")
        sizePolicy.setHeightForWidth(self.button_bar_cadastrar.sizePolicy().hasHeightForWidth())
        self.button_bar_cadastrar.setSizePolicy(sizePolicy)
        self.button_bar_cadastrar.setMinimumSize(QSize(0, 0))
        self.button_bar_cadastrar.setMaximumSize(QSize(500, 100))
        self.button_bar_cadastrar.setSizeIncrement(QSize(0, 0))

        self.gridLayout_2.addWidget(self.button_bar_cadastrar, 1, 0, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer, 0, 1, 1, 1)

        self.button_bar_cobranca = QPushButton(Home)
        self.button_bar_cobranca.setObjectName(u"button_bar_cobranca")
        sizePolicy.setHeightForWidth(self.button_bar_cobranca.sizePolicy().hasHeightForWidth())
        self.button_bar_cobranca.setSizePolicy(sizePolicy)
        self.button_bar_cobranca.setMinimumSize(QSize(0, 0))
        self.button_bar_cobranca.setMaximumSize(QSize(500, 100))
        self.button_bar_cobranca.setSizeIncrement(QSize(0, 0))

        self.gridLayout_2.addWidget(self.button_bar_cobranca, 2, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer, 4, 0, 1, 1)


        self.retranslateUi(Home)

        QMetaObject.connectSlotsByName(Home)
    # setupUi

    def retranslateUi(self, Home):
        self.button_bar_configuracoes.setText(QCoreApplication.translate("Home", u"Configura\u00e7\u00f5es", None))
        self.button_bar_inicio.setText(QCoreApplication.translate("Home", u"Inicio", None))
        self.button_bar_cadastrar.setText(QCoreApplication.translate("Home", u"Cadastrar", None))
        self.button_bar_cobranca.setText(QCoreApplication.translate("Home", u"Pagamento", None))
        pass
    # retranslateUi

