# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.6.3
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QProgressBar,
    QPushButton, QSizePolicy, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(833, 729)
        Form.setMinimumSize(QSize(833, 729))
        Form.setMaximumSize(QSize(833, 729))
        self.gridLayoutWidget = QWidget(Form)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(80, 70, 671, 481))
        self.game_grid = QGridLayout(self.gridLayoutWidget)
        self.game_grid.setObjectName(u"game_grid")
        self.game_grid.setContentsMargins(0, 0, 0, 0)
        self.reset_button = QPushButton(Form)
        self.reset_button.setObjectName(u"reset_button")
        self.reset_button.setGeometry(QRect(640, 0, 191, 61))
        self.time_bar = QProgressBar(Form)
        self.time_bar.setObjectName(u"time_bar")
        self.time_bar.setGeometry(QRect(190, 20, 431, 23))
        self.time_bar.setValue(24)
        self.game_name = QLabel(Form)
        self.game_name.setObjectName(u"game_name")
        self.game_name.setGeometry(QRect(10, 10, 161, 41))
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(24)
        self.game_name.setFont(font)
        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(110, 610, 181, 71))
        self.choose_button = QPushButton(Form)
        self.choose_button.setObjectName(u"choose_button")
        self.choose_button.setGeometry(QRect(310, 610, 181, 71))
        self.reset_game = QPushButton(Form)
        self.reset_game.setObjectName(u"reset_game")
        self.reset_game.setGeometry(QRect(510, 610, 181, 71))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.reset_button.setText(QCoreApplication.translate("Form", u"\u0421\u0431\u0440\u043e\u0441\u0438\u0442\u044c", None))
        self.game_name.setText(QCoreApplication.translate("Form", u"      Waggle", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"\u0412\u044b\u0439\u0442\u0438 \u0432 \u0433\u043b\u0430\u0432\u043d\u043e\u0435 \u043c\u0435\u043d\u044e", None))
        self.choose_button.setText(QCoreApplication.translate("Form", u"\u0412\u044b\u0431\u0440\u0430\u0442\u044c \u0443\u0440\u043e\u0432\u0435\u043d\u044c", None))
        self.reset_game.setText(QCoreApplication.translate("Form", u" \u041d\u0430\u0447\u0430\u0442\u044c \u0437\u0430\u043d\u043e\u0432\u043e", None))
    # retranslateUi

