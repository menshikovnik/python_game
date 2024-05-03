# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
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
from PySide6.QtWidgets import (QApplication, QPushButton, QSizePolicy, QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(800, 600)
        Widget.setMinimumSize(QSize(800, 600))
        Widget.setMaximumSize(QSize(800, 600))
        self.button_start = QPushButton(Widget)
        self.button_start.setObjectName(u"button_start")
        self.button_start.setGeometry(QRect(280, 110, 271, 121))
        self.button_level_choose = QPushButton(Widget)
        self.button_level_choose.setObjectName(u"button_level_choose")
        self.button_level_choose.setGeometry(QRect(280, 230, 271, 121))

        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Widget", None))
        self.button_start.setText(QCoreApplication.translate("Widget", u"\u0421\u0442\u0430\u0440\u0442", None))
        self.button_level_choose.setText(QCoreApplication.translate("Widget", u"\u0412\u044b\u0431\u0440\u0430\u0442\u044c \u0423\u0440\u043e\u0432\u0435\u043d\u044c", None))
    # retranslateUi

