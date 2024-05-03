# This Python file uses the following encoding: utf-8
from PySide6.QtWidgets import QMainWindow
from windows.MainWindow import MainWindow
from PySide6.QtCore import Qt
from py_forms.ui_form import Ui_Widget

class MenuWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Widget()
        self.ui.setupUi(self)

        self.ui.button_start.clicked.connect(self.start_game)
        self.setWindowState(self.windowState() & ~Qt.WindowFullScreen)

        self.game_window = None

    def start_game(self):
        self.close()
        self.game_window = MainWindow()
        self.game_window.show()
