import sys
import os
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtCore import QPoint
import design
sys.path.append(os.path.join(sys.path[0], '../Model'))
import hitori_solver
import hitori_generator


class HexatoriApp(QtWidgets.QMainWindow, design.Ui_HexatoriPy):

    black_color = "#00665E"
    background_color = "#33CEC3"
    checked_color = "#FF9340"
    unchecked_color = "#FFB073"

    def __init__(self, map_size):
        super().__init__()
        self.setupUi(self)
        self.setStyleSheet("background-color:"+self.background_color+";")

        self.ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
        self.map_size = map_size
        self.array_size = map_size * 2 - 1

        self.init_buttons()
        self.buttons = []
        self.generate_map()
        self.mode = 0
        self.show()

    def init_buttons(self):
        self.newGameButton.move(700, 100)
        self.init_button(self.newGameButton, self.newGameClick, 'obeme.jpg', "new game")
        self.hintButton.move(635, 195)
        self.init_button(self.hintButton, self.hintClick, 'obeme.jpg', "hint")
        self.solveButton.move(700, 290)
        self.init_button(self.solveButton, self.solveClick, 'obeme.jpg', "solve")
        self.blackButton.move(-30, 450)
        self.blackButton.resize(100, 100)
        self.init_button(self.blackButton, self.switchBlackClick, 'obeme.jpg', "black")
        self.whiteButton.move(23, 530)
        self.whiteButton.resize(100, 100)
        self.init_button(self.whiteButton, self.switchWhiteClick, 'obeme.jpg', "white")

    def init_button(self, button, onclick, iconName, text):
        #icon = QtGui.QIcon(self.ROOT_DIR + '/Images/' + iconName)
        #button.setIcon(icon)
        #button.setIconSize(QtCore.QSize(120, 120))
        button.setText(text)
        self.hexagonize_button(button)
        button.setStyleSheet("background-color:"+self.black_color+";")

        button.clicked.connect(onclick)

    def newGameClick(self):
        self.generate_map()

    def hintClick(self):
        pass

    def solveClick(self):
        self.solver.solve()
        self.update_map(self.solver.wb_array)

    def switchWhiteClick(self):
        self.mode = 1

    def switchBlackClick(self):
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
                if value == self.solver.black:
                    self.set_tile_black(x, y)
                elif value == self.solver.white:
                    self.set_tile_white(x, y)

    def generate_map(self):
        self.clear_map()
        
        self.hex_map = hitori_generator.generate_map(self.map_size)
        self.solver = hitori_solver.HitoriSolver(self.hex_map)

        self.array_size = len(self.hex_map)
        offset = (self.array_size - 1) // 2

        button_width = 600 // self.array_size - 2
        button_height = 600 // self.array_size

        for y in range(self.array_size):
            offset = y - self.map_size + 1
            offset *= -1
            for x in range(self.array_size):
                if not self.hex_map[x][y].isdigit():
                    self.buttons.append(None)
                    continue
                button = QtWidgets.QPushButton(self.hex_map[x][y], self)
                button.resize(button_width, button_height)
                button.move(*self.get_position(x, y, button_width, 
                        button_height, offset))
                self.hexagonize_button(button)
                self.buttons.append(button)
                button.setStyleSheet("background-color:" + self.unchecked_color + "; color: black;")
                button.setFont(QtGui.QFont("Ubuntu BOLD", 200 // self.array_size))
                button.show()
        for y in range(self.array_size):
            for x in range(self.array_size):
                button_id = y * self.array_size + x
                if self.buttons[button_id] == None:
                    continue
                self.buttons[button_id].clicked.connect(
                    lambda temp, arg=button_id: self.tile_click(arg))

    def get_position(self, x, y, button_width, button_height, offset):
        bw = button_width + 2
        bh = button_height * 3 // 4 + 4
        return 15 + bw * x + offset * bw // 2, 40 + bh * y

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
        button.setMask(QtGui.QRegion(QtGui.QPolygon(points)))
        button.setStyleSheet("background-color: white; border: none")

    def tile_click(self, button_id):
        x, y = button_id % self.array_size, button_id // self.array_size
        if self.mode == 0:
            if not self.set_tile_black(x, y):
                self.alert("impossible to set tile black")
        else:
            if not self.set_tile_white(x, y):
                self.alert("impossible to set tile white")

    def set_tile_black(self, x, y):
        # проверить в wb_map, можно ли
        self.buttons[y * self.array_size + x].setStyleSheet("background-color:"+self.black_color+"; color: white;")
        return True

    def set_tile_white(self, x, y):
        # проверить в wb_map, можно ли
        self.buttons[y * self.array_size + x].setStyleSheet("background-color:"+self.checked_color+"; color: black;")
        return True

    def alert(self, message):
        print(message)

    def check_game(self):
        pass

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = HexatoriApp(10)
    app.exec_()

if __name__ == "__main__":
    main()


"""
TODO
refactor
solver fixes
"""