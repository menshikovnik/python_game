from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget
from PySide6.QtCore import Qt, QTimer
from PySide6.QtGui import QPixmap, QPainter
import random
import sys

class FireworksAnimation(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        self.fireworks_timer = QTimer(self)
        self.fireworks_timer.timeout.connect(self.create_firework)
        self.fireworks_timer.start(100)  # Создавать новые фейерверки каждую секунду

        self.duration_timer = QTimer(self)
        self.duration_timer.setSingleShot(True)
        self.duration_timer.timeout.connect(self.finish_animation)
        self.duration_timer.start(3000)

        self.fireworks = []

    def create_firework(self):
        firework = {'x': random.randint(0, self.width()), 'y': random.randint(0, self.height()), 'size': random.randint(20, 100)}
        self.fireworks.append(firework)
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        for firework in self.fireworks:
            pixmap = QPixmap("pngwing.com.png").scaled(firework['size'], firework['size'])
            painter.drawPixmap(firework['x'], firework['y'], pixmap)

            # Увеличиваем размер фейерверка на следующей итерации
            firework['size'] += 50

        # Удаляем фейерверки, которые вышли за пределы окна
        self.fireworks = [firework for firework in self.fireworks if firework['size'] <= 200]


    def finish_animation(self):
        self.fireworks_timer.stop()
        self.close()
