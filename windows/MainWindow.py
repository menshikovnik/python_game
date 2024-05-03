# This Python file uses the following encoding: utf-8
from PySide6.QtWidgets import QMainWindow
from logic.BallButton import BallButton
from py_forms.ui_main_window import Ui_Form
from PySide6.QtCore import QTimer
import json

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.setWindowTitle("Игра Вогл")

        self.layout = self.ui.game_grid

        self.ui.time_bar.setMaximum(100)
        self.ui.time_bar.setValue(0)

        self.total_steps = 120
        self.current_step = 0

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_progress_bar)
        self.timer.start(1000)
        self.elapsed_time = 0

        self.game_board = []
        self.GAME_BOARD_SIZE = 7
        self.curr_level = 1
        self.create_game_board(self.curr_level)
        self.ui.reset_button.clicked.connect(self.reset_game_board)

    def create_game_board(self, level):
        ball_coordinates = self.select_level(level)
        for i in range(self.GAME_BOARD_SIZE):
            row = []
            for j in range(self.GAME_BOARD_SIZE):
                has_ball = (i, j) in ball_coordinates
                ball = BallButton(i, j, self.game_board, has_ball, parent=self)
                self.layout.addWidget(ball, i, j)
                row.append(ball)
            self.game_board.append(row)


    def update_progress_bar(self):
        self.elapsed_time += 1

        if self.elapsed_time <= 120:
            progress = self.elapsed_time * 100 / 120
            self.ui.time_bar.setValue(progress)
        else:
            self.timer.stop()



    def load_levels(self, filename):
        with open(filename, 'r') as file:
            levels = json.load(file)
        return levels


    def select_level(self, level):
        levels = self.load_levels('resources/levels.json')
        level_tuples = levels[level - 1]
        level_tuples = [tuple(coords) for coords in level_tuples]
        return level_tuples

    def reset_game_board(self):
       self.game_board.clear()
       self.create_game_board(self.curr_level)
