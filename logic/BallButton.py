from PySide6.QtWidgets import QPushButton
from windows.WinWindow import WinWindow
from PySide6.QtCore import Qt

class BallButton(QPushButton):
    def __init__(self, row, column, game_board, has_ball, parent=None):
        super().__init__(parent)
        self.setFixedSize(50, 50)
        if has_ball:
            self.has_ball = True
        else:
            self.has_ball = False
        self.setStyleSheet("border-radius: 25px;")
        self.row = row
        self.column = column
        self.parent_window = parent
        self.game_board = game_board
        self.update_style()
        self.isPressed = False


    def update_style(self):
        if self.has_ball:
            self.setStyleSheet("background-color: red; border-radius: 25px;")
        else:
            self.setStyleSheet("background-color: white; border-radius: 25px;")

    def mousePressEvent(self, event):
            if event.button() == Qt.LeftButton:
                tmp_row, tmp_col = self.find_pressed()
                if not self.isPressed and self.has_ball and tmp_row == -1 and tmp_col == -1:
                    self.setStyleSheet("background-color: yellow; border: 2px solid black; border-radius: 25px;")
                    self.isPressed = True
                elif self.isPressed and self.has_ball:
                    self.setStyleSheet("background-color: red; border-radius: 25px;")
                    self.isPressed = False
                if not self.has_ball:
                    row, col = self.find_pressed()
                    if row != -1 and col != -1:
                        tuple_to_check = (self.row, self.column)

                        if tuple_to_check in self.is_can_move(row, col):
                            if self.column - col == 2:
                                self.game_board[row][self.column - 1].setStyleSheet("background-color: white; border-radius: 25px;")
                                self.game_board[row][self.column - 1].has_ball = False
                                self.move_ball(row, col)
                            elif self.column - col == -2:
                                self.game_board[row][self.column + 1].setStyleSheet("background-color: white; border-radius: 25px;")
                                self.game_board[row][self.column + 1].has_ball = False
                                self.move_ball(row, col)
                            elif self.row - row == 2:
                                self.game_board[self.row - 1][col].setStyleSheet("background-color: white; border-radius: 25px;")
                                self.game_board[self.row - 1][col].has_ball = False
                                self.move_ball(row, col)
                            elif self.row - row == -2:
                                self.game_board[self.row + 1][col].setStyleSheet("background-color: white; border-radius: 25px;")
                                self.game_board[self.row + 1][col].has_ball = False
                                self.move_ball(row, col)
                            if self.check_win() == True:
                                self.show_win_widget()


    def find_pressed(self):
        for i in range(len(self.game_board)):
            for j in range(len(self.game_board[i])):
                if self.game_board[i][j].isPressed:
                    return i, j
        return -1, -1


    def is_can_move(self, row, col):
        move_list = []
        if col < 6 and self.game_board[row][col + 1].has_ball:
            move_list.append((row, col + 2))
        if col > 1 and self.game_board[row][col - 1].has_ball:
            move_list.append((row, col - 2))
        if row < 6 and self.game_board[row + 1][col].has_ball:
            move_list.append((row + 2, col))
        if row > 1 and self.game_board[row - 1][col].has_ball:
            move_list.append((row - 2, col))
        return move_list


    def move_ball(self, row, col):
        self.setStyleSheet("background-color: red; border-radius: 25px;")
        self.has_ball = True
        self.game_board[row][col].setStyleSheet("background-color: white; border-radius: 25px;")
        self.game_board[row][col].has_ball = False
        self.game_board[row][col].isPressed = False


    def check_win(self):
        count = 0
        for i in range(len(self.game_board)):
            for j in range(len(self.game_board[i])):
                if self.game_board[i][j].has_ball:
                    count += 1
        if count > 1:
            return False
        else:
            return True


    def show_win_widget(self):
        self.parent_window.close()
        self.victory_window = WinWindow()
        self.victory_window.show()
        self.victory_window.start_fireworks()

