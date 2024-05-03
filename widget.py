import sys
from PySide6.QtWidgets import QApplication
from windows.MenuWindow import MenuWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MenuWindow()
    window.show()
    sys.exit(app.exec())
