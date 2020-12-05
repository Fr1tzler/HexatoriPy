import sys
import os
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QMainWindow, QShortcut, QApplication, QMessageBox
from PyQt5.QtGui import QKeySequence, QFont, QPolygon, QRegion
from PyQt5.QtCore import QPoint
from design import Ui_HexatoriPy

sys.path.append(os.path.join(sys.path[0], '../Model'))
from hexatori import Hexatori
from hexatori_solver import HexatoriSolver
from hexatori_generator import get_map

class HexatoriApp(QMainWindow, Ui_HexatoriPy, Hexatori):
    black_color = "#00665E"
    background_color = "#33CEC3"
    unchecked_color = "#DF8330"
    checked_color = "#FFB073"

    def __init__(self, map_size=5):
        super().__init__()
        self.setupUi(self)

        self.map_size = map_size
        self.array_size = map_size * 2 - 1

        self.new_game = True
        self.init_styles()
        self.groupBox.setStyleSheet(self.checked_style)
        self.init_buttons()
        self.init_size_slider()
        self.buttons = []
        self.undo = []
        self.generate_map()
        self.mode = 0
        self.shortcut = QShortcut(QKeySequence("Ctrl+Z"), self)
        self.shortcut.activated.connect(self.undo_click)

        self.show()

    def init_styles(self):
        self.black_style = "background-color:" + self.black_color + "; color: white;"
        self.checked_style = "background-color:" + \
            self.checked_color + "; color: black;"
        self.unchecked_style = "background-color:" + \
            self.unchecked_color + "; color: black;"
        self.setStyleSheet("background-color:" + self.background_color + ";")

    def init_buttons(self):
        self.newGameButton.move(690, 100)
        self.init_button(self.newGameButton, self.new_game_click, "New game")
        self.hintButton.move(627, 195)
        self.init_button(self.hintButton, self.hint_click, "Hint")
        self.solveButton.move(690, 290)
        self.init_button(self.solveButton, self.solve_click, "Solve")
        self.blackButton.move(-20, 450)
        self.blackButton.resize(100, 100)
        self.init_button(self.blackButton, self.switch_black_click, "Black")
        self.whiteButton.move(33, 530)
        self.whiteButton.resize(100, 100)
        self.init_button(self.whiteButton, self.switch_white_click, "White")
        self.undoButton.move(627, 305)
        self.undoButton.resize(57, 57)
        self.init_button(self.undoButton, self.undo_click, "Undo")

    def init_button(self, button, onclick, text):
        button.setText(text)
        self.hexagonize_button(button)
        button.setStyleSheet(self.black_style)
        button.clicked.connect(onclick)
        button.setFont(QFont("Ubuntu BOLD", 12))

    def new_game_click(self):
        self.change_slider_visibility(self.new_game)
        if (self.new_game):
            self.newGameButton.setText("Continue?")
        else:
            self.newGameButton.setText("New game")
            self.generate_map()
        self.new_game = not self.new_game

    def undo_click(self):
        if len(self.undo) <= 0:
            return
        points = self.undo.pop()
        for point in points:
            self.buttons[point[1] * self.array_size +
                         point[0]].setStyleSheet(self.unchecked_style)
            self.solver.set_point_neutral(point)
        self.solver.update_map()
        self.update_map(self.solver.wb_map)

    def change_slider_visibility(self, value):
        self.hintButton.setVisible(not value)
        self.groupBox.setVisible(value)
        self.size_label.setVisible(value)
        self.horizontalSlider.setVisible(value)

    def init_size_slider(self):
        self.groupBox.resize(120, 120)
        self.groupBox.move(627, 195)
        self.hexagonize_button(self.groupBox)
        self.groupBox.setStyleSheet(self.black_style + "border: none;")

        temp_stylesheet = "color: white; background-color:{};".format(
            self.black_color)

        self.size_label.setText(str(self.map_size))
        self.size_label.setFont(QFont("Ubuntu BOLD", 20))
        self.size_label.setStyleSheet(temp_stylesheet)
        self.size_label.move(675, 220)
        self.size_label.resize(60, 30)
        self.size_label.show()

        self.horizontalSlider.setMinimum(3)
        self.horizontalSlider.setMaximum(10)
        self.horizontalSlider.setSingleStep(1)
        self.horizontalSlider.setValue(self.map_size)
        self.horizontalSlider.valueChanged.connect(self.slider_change)
        self.horizontalSlider.resize(110, 20)
        self.horizontalSlider.setStyleSheet(temp_stylesheet)
        self.horizontalSlider.move(630, 260)

        self.change_slider_visibility(False)

    def slider_change(self):
        value = self.horizontalSlider.value()
        self.size_label.setText(str(value))
        self.map_size = value

    def hint_click(self):
        self.alert("HINT")

    def solve_click(self):
        self.solver = HexatoriSolver(self.hex_map)
        self.solver.solve_all()
        self.update_map(self.solver.wb_map)

    def switch_white_click(self):
        self.mode = 1

    def switch_black_click(self):
        self.mode = 0

    def clear_map(self):
        for button in self.buttons:
            if button != None:
                button.deleteLater()
        self.buttons = []

    def update_map(self, wb_map):
        for x in range(self.array_size):
            for y in range(self.array_size):
                value = wb_map[x][y]
                id = y * self.array_size + x
                if value == self.solver.black:
                    self.buttons[id].setStyleSheet(self.black_style)
                elif value == self.solver.white:
                    self.buttons[id].setStyleSheet(self.checked_style)

    def generate_map(self):
        self.mode = 0
        self.clear_map()
        self.hex_map = get_map(self.map_size)
        self.solver = HexatoriSolver(self.hex_map)
        self.array_size = len(self.hex_map)
        width = 600 // self.array_size - 2
        height = 600 // self.array_size

        for y in range(self.array_size):
            offset = self.map_size - y - 1
            for x in range(self.array_size):
                if not self.hex_map[x][y].isdigit():
                    self.buttons.append(None)
                    continue
                button = QtWidgets.QPushButton(self.hex_map[x][y], self)
                button.resize(width, height)
                button.move(*self.get_position(x, y, width, height, offset))
                self.hexagonize_button(button)
                self.buttons.append(button)
                button.setStyleSheet(self.unchecked_style)
                button.setFont(QFont("Ubuntu BOLD", 200 // self.array_size))
                button.show()
        for y in range(self.array_size):
            for x in range(self.array_size):
                button_id = y * self.array_size + x
                if self.buttons[button_id] is None:
                    continue

                def function(temp, arg=button_id): return self.tile_click(arg)
                self.buttons[button_id].clicked.connect(function)

    def get_position(self, x, y, width, height, offset):
        block_w = width + 1
        block_h = height * 3 // 4 + 3
        return 20 + block_w * x + offset * block_w // 2, 40 + block_h * y

    def hexagonize_button(self, button):
        x = button.width()
        y = button.height()
        p1 = QPoint(x // 2, 0)
        p2 = QPoint(x, y // 4)
        p3 = QPoint(x, 3 * y // 4)
        p4 = QPoint(x // 2, y)
        p5 = QPoint(0, 3 * y // 4)
        p6 = QPoint(0, y // 4)
        points = [p1, p2, p3, p4, p5, p6]
        button.setMask(QtGui.QRegion(QPolygon(points)))
        button.setStyleSheet("border: none")

    def tile_click(self, button_id):
        x, y = button_id % self.array_size, button_id // self.array_size
        if self.mode == 0:
            if not self.set_tile_black(x, y):
                self.alert("impossible to set tile black")
        elif self.mode == 1:
            if not self.set_tile_white(x, y):
                self.alert("impossible to set tile white")
        else:
            pass
        self.check_game()

    def set_tile_black(self, x, y):
        if not self.solver.set_point_black([x, y]):
            return False
        self.buttons[y * self.array_size + x].setStyleSheet(self.black_style)
        colored_tiles = [[x, y]]
        for point in self.solver.get_point_neighbours([x, y]):
            id = point[1] * self.array_size + point[0]
            if not self.tile_in_undo(point):
                colored_tiles.append(point)
            self.buttons[id].setStyleSheet(self.checked_style)
        self.undo.append(colored_tiles)
        return True

    def tile_in_undo(self, tile):
        for action in self.undo:
            if tile in action:
                return True
        return False

    def set_tile_white(self, x, y):
        if not self.solver.set_point_white([x, y]):
            return False
        self.undo.append([[x, y]])
        self.buttons[y * self.array_size + x].setStyleSheet(self.checked_style)
        return True

    def alert(self, message):
        QMessageBox.question(self, 'Message from Hexatori', message, QMessageBox.Ok)

    def check_game(self):
        if self.solver.check_for_success():
            self.alert("YOU WIN")
            self.mode = -1

def main():
    app = QApplication(sys.argv)
    HexatoriApp()
    app.exec_()


if __name__ == "__main__":
    main()

"""
TODO
hint_button()
solver чёт дурит
background style
"""
