import sys, os
from PyQt5 import QtWidgets, QtGui, QtCore
import design
sys.path.append(os.path.join(sys.path[0], '../Model'))
import hitori_generator, hitori_solver

class HexatoriApp(QtWidgets.QMainWindow, design.Ui_HexatoriPy):
    def __init__(self, map_size):
        super().__init__()
        self.setupUi(self)
        self.ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
        self.map_size = map_size
        self.init_buttons()
        self.scene = QtWidgets.QGraphicsScene(self)
        self.view = QtWidgets.QGraphicsView(self.scene)
        self.buttons = []
        self.generate_map()
        self.show()

    def init_buttons(self):
        self.init_button(self.newGameButton, self.newGameClick, 'obeme.jpg')
        self.init_button(self.hintButton, self.hintClick, 'obeme.jpg')
        self.init_button(self.solveButton, self.solveClick, 'obeme.jpg')

    def init_button(self, button, onclick, iconName):
        icon = QtGui.QIcon(self.ROOT_DIR + '/Images/' + iconName)
        button.setIcon(icon)
        button.setIconSize(QtCore.QSize(120, 120))
        button.clicked.connect(onclick)

    def newGameClick(self):
        print("new game clicked")
        self.generate_map()

    def generate_map(self):
        self.hex_map = hitori_generator.generate_map(self.map_size)
        size = len(self.hex_map)
        offset = (size - 1) // 2
        for button in self.buttons:
            button.deleteLater()
        self.buttons = []

        button_width = 500 // size
        button_height = 500 // (size)
        for y in range(size):
            offset = y - self.map_size + 1
            offset *= -1
            for x in range(size):
                if not self.hex_map[x][y].isdigit():
                    continue
                button = QtWidgets.QPushButton(self.hex_map[x][y], self)
                button.resize(button_width, button_height)
                button.move(50 + button_width * x + offset * button_width // 2, 50 + button_height * y)
                button.show()
                self.buttons.append(button)

        a = [lambda: self.foo(x) for x in range(len(self.buttons))]
        for button_id in range(len(self.buttons)):
            self.buttons[button_id].clicked.connect(a[button_id])

    def foo(self, button_id):
        self.buttons[button_id].setStyleSheet("background-color: red")
        print(button_id)

    def foo2(self, button):
        button.setStyleSheet("background-color: red")

    def hintClick(self):
        print("hint clicked")

    def solveClick(self):
        print("solve clicked")


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = HexatoriApp(5)
    app.exec_()

if __name__ == "__main__":
    main()