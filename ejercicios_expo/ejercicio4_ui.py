# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ejercicio4.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLCDNumber,
    QLabel, QLayout, QLineEdit, QMainWindow,
    QPushButton, QRadioButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(585, 653)
        MainWindow.setStyleSheet(u"font: 12pt \"Calculator\";")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(19, 39, 561, 611))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setSizeConstraint(QLayout.SizeConstraint.SetFixedSize)
        self.horizontalLayout_16.setContentsMargins(-1, 30, -1, 50)
        self.entrada_numero_4 = QLineEdit(self.verticalLayoutWidget)
        self.entrada_numero_4.setObjectName(u"entrada_numero_4")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(20)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.entrada_numero_4.sizePolicy().hasHeightForWidth())
        self.entrada_numero_4.setSizePolicy(sizePolicy1)

        self.horizontalLayout_16.addWidget(self.entrada_numero_4)

        self.button_convertidor_4 = QPushButton(self.verticalLayoutWidget)
        self.button_convertidor_4.setObjectName(u"button_convertidor_4")

        self.horizontalLayout_16.addWidget(self.button_convertidor_4)

        self.horizontalSpacer_4 = QSpacerItem(150, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_16.addItem(self.horizontalSpacer_4)

        self.label_6 = QLabel(self.verticalLayoutWidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMaximumSize(QSize(260, 119))
        self.label_6.setBaseSize(QSize(150, 0))
        self.label_6.setFrameShape(QFrame.Shape.Box)
        self.label_6.setLineWidth(1)
        self.label_6.setTextFormat(Qt.TextFormat.AutoText)
        self.label_6.setPixmap(QPixmap(u"C:\\Users\\SEBASTIAN\\OneDrive\\Documentos\\GitHub\\Tercer_Semestre_U\\ejercicios_expo\\Escudo_udenar.png"))
        self.label_6.setScaledContents(True)

        self.horizontalLayout_16.addWidget(self.label_6)


        self.horizontalLayout_17.addLayout(self.horizontalLayout_16)


        self.verticalLayout.addLayout(self.horizontalLayout_17)

        self.pantalla = QLCDNumber(self.verticalLayoutWidget)
        self.pantalla.setObjectName(u"pantalla")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        sizePolicy2.setHorizontalStretch(100)
        sizePolicy2.setVerticalStretch(130)
        sizePolicy2.setHeightForWidth(self.pantalla.sizePolicy().hasHeightForWidth())
        self.pantalla.setSizePolicy(sizePolicy2)
        self.pantalla.setBaseSize(QSize(0, 0))

        self.verticalLayout.addWidget(self.pantalla)

        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.horizontalLayout_18.setContentsMargins(-1, 100, -1, 100)
        self.Decimal_4 = QRadioButton(self.verticalLayoutWidget)
        self.Decimal_4.setObjectName(u"Decimal_4")

        self.horizontalLayout_18.addWidget(self.Decimal_4)

        self.Binario_4 = QRadioButton(self.verticalLayoutWidget)
        self.Binario_4.setObjectName(u"Binario_4")

        self.horizontalLayout_18.addWidget(self.Binario_4)

        self.Octal_4 = QRadioButton(self.verticalLayoutWidget)
        self.Octal_4.setObjectName(u"Octal_4")

        self.horizontalLayout_18.addWidget(self.Octal_4)

        self.Hexadecimal_4 = QRadioButton(self.verticalLayoutWidget)
        self.Hexadecimal_4.setObjectName(u"Hexadecimal_4")

        self.horizontalLayout_18.addWidget(self.Hexadecimal_4)


        self.verticalLayout.addLayout(self.horizontalLayout_18)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.button_convertidor_4.setText(QCoreApplication.translate("MainWindow", u"convertir", None))
        self.label_6.setText("")
        self.Decimal_4.setText(QCoreApplication.translate("MainWindow", u"Decimal", None))
        self.Binario_4.setText(QCoreApplication.translate("MainWindow", u"Binario", None))
        self.Octal_4.setText(QCoreApplication.translate("MainWindow", u"Octal", None))
        self.Hexadecimal_4.setText(QCoreApplication.translate("MainWindow", u"Hexadecimal", None))
    # retranslateUi

