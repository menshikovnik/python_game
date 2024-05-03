# This Python file uses the following encoding: utf-8
from py_forms.ui_win import Ui_Form
from logic.FireworksAnimation import FireworksAnimation
from PySide6.QtWidgets import QWidget
from PySide6.QtGui import QMovie

class WinWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.setWindowTitle("Победа!")
        self.menu_window = None
        movie = QMovie("you-cant-win.gif")
        self.ui.gif_label.setMovie(movie)
        movie.start()
        self.ui.back_to_menu.clicked.connect(self.back_to_menu)

    def start_fireworks(self):
        self.fireworks_widget = FireworksAnimation()
        main_window_geometry = self.geometry()
        fireworks_geometry = self.fireworks_widget.geometry()
        fireworks_geometry.moveCenter(main_window_geometry.center())
        self.fireworks_widget.setGeometry(fireworks_geometry)
        self.fireworks_widget.show()


    def back_to_menu(self):
        from windows.MenuWindow import MenuWindow
        self.menu_window = MenuWindow()
        self.close()
        self.menu_window.show()
