from random import randint, choice
import sys, os
sys.path.append(os.path.join(sys.path[0], '../Model'))
from additional_math import *
from hexatori import Hexatori


class HexatoriGenerator(Hexatori):
    def set_black_tiles(self):
        remaining_amount = int(self.edge_size ** 2 // 3)
        while(self.count_empty_cells() > 0):
            x = randint(0, self.arr_size - 1)
            y = randint(0, self.arr_size - 1)
            if self.hex_map[y][x] == self.empty:
                self.hex_map[y][x] = self.black
                for i in self.get_point_neighbours([y, x]):
                    self.hex_map[i[0]][i[1]] = self.white
                remaining_amount -= 1
        for i in range(self.arr_size):
            for j in range(self.arr_size):
                if self.hex_map[i][j] == self.white:
                    self.hex_map[i][j] = self.empty

    def set_numbers_on_white(self, number):
        self.temp_hex_map = arr_copy(self.hex_map)
        for y in range(self.arr_size):
            tiles_count = self.temp_hex_map[y].count(self.empty)
            if tiles_count > 0:
                x_arr = positions_in_arr(self.temp_hex_map[y], self.empty)
                if tiles_count == 1:
                    p = 0
                else:
                    p = randint(0, tiles_count - 1)
                x = x_arr[p]
                current_tile = [y, x]
                lines = self.get_point_lines(self.temp_hex_map, current_tile)
                for pt in lines:
                    self.temp_hex_map[pt[0]][pt[1]] = self.white
                self.hex_map[current_tile[0]][current_tile[1]] = number

    def count_empty_cells(self):
        return sum(i.count(self.empty) for i in self.hex_map)

    def set_numbers_on_field(self):
        current_number = 0
        while (self.count_empty_cells() > 0):
            self.set_numbers_on_white(str(current_number))
            current_number += 1

    def set_numbers_on_black(self):
        for y in range(self.arr_size):
            while (self.hex_map[y].count(self.black) != 0):
                x = self.hex_map[y].index(self.black)
                near = self.get_point_neighbours([y, x])
                values = set([self.hex_map[p[0]][p[1]] for p in near])
                if self.black in values:
                    values.remove(self.black)
                values = list(values)
                self.hex_map[y][x] = choice(values)


def get_map(map_size):
    result = HexatoriGenerator(map_size)
    result.set_black_tiles()
    result.set_numbers_on_field()
    result.set_numbers_on_black()
    return result.hex_map
