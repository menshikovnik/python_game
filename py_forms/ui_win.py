# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'win.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QPushButton, QSizePolicy,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(828, 557)
        Form.setMinimumSize(QSize(828, 557))
        Form.setMaximumSize(QSize(828, 557))
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(210, 40, 421, 51))
        font = QFont()
        font.setFamilies([u"Andale Mono"])
        font.setPointSize(24)
        self.label.setFont(font)
        self.back_to_menu = QPushButton(Form)
        self.back_to_menu.setObjectName(u"back_to_menu")
        self.back_to_menu.setGeometry(QRect(259, 121, 331, 71))
        self.level_choose = QPushButton(Form)
        self.level_choose.setObjectName(u"level_choose")
        self.level_choose.setGeometry(QRect(260, 200, 331, 71))
        self.restart_level = QPushButton(Form)
        self.restart_level.setObjectName(u"restart_level")
        self.restart_level.setGeometry(QRect(260, 280, 331, 71))
        self.gif_label = QLabel(Form)
        self.gif_label.setObjectName(u"gif_label")
        self.gif_label.setGeometry(QRect(210, 360, 421, 191))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u041f\u043e\u0437\u0434\u0440\u0430\u0432\u043b\u044f\u044e, \u0432\u044b \u043f\u0440\u043e\u0448\u043b\u0438 \u0443\u0440\u043e\u0432\u0435\u043d\u044c", None))
        self.back_to_menu.setText(QCoreApplication.translate("Form", u"\u0412\u0435\u0440\u043d\u0443\u0442\u044c\u0441\u044f \u0432 \u041c\u0435\u043d\u044e", None))
        self.level_choose.setText(QCoreApplication.translate("Form", u"\u0412\u044b\u0431\u0440\u0430\u0442\u044c \u0423\u0440\u043e\u0432\u0435\u043d\u044c", None))
        self.restart_level.setText(QCoreApplication.translate("Form", u"\u041f\u0440\u043e\u0439\u0442\u0438 \u0423\u0440\u043e\u0432\u0435\u043d\u044c \u0437\u0430\u043d\u043e\u0432\u043e", None))
        self.gif_label.setText("")
    # retranslateUi

