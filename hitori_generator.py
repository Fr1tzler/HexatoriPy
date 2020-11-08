from random import randint, choice
import sys
from additional_math import *

class HitoriGenerator:
    empty = 'e'
    border = 'r'
    black = 'b'
    white = 'w'

    hr_line = [0, -1]
    v1_line = [-1, 0]
    v2_line = [-1, -1]

    def __init__(self, edge_size):
        arr_size = edge_size * 2 - 1
        self.hex_map = [[self.empty] * arr_size for j in range(arr_size)]

        for line_number in range(arr_size):
            shift = line_number - edge_size + 1
            if shift < 0:
                self.hex_map[line_number][shift:] = [self.border] * -shift
            elif shift > 0:
                self.hex_map[line_number][:shift] = [self.border] * shift   
        self.edge_size = edge_size
        self.arr_size = arr_size

    def print_map(self):
        for i in range(self.arr_size):
            print(' ' * abs(i - self.edge_size + 1), end=' ')
            filtered_arr = filter(lambda x : x != self.border, self.hex_map[i])
            print(' '.join(filtered_arr))
    
    def point_inside(self, arr, point):
        if point[0] < 0 or point[0] >= self.arr_size:
            return False
        if point[1] < 0 or point[1] >= self.arr_size:
            return False
        return arr[point[0]][point[1]] != self.border

    def get_point_neighbours(self, arr, point):
        if not self.point_inside(arr, point):
            return []
        point_arr = []
        point_arr.append(arr_sum(point, self.v2_line))
        point_arr.append(arr_sum(point, self.hr_line))
        point_arr.append(arr_sum(point, self.v1_line))
        point_arr.append(arr_diff(point, self.v2_line))
        point_arr.append(arr_diff(point, self.hr_line))
        point_arr.append(arr_diff(point, self.v1_line))
        return list(filter(lambda x : self.point_inside(arr, x), point_arr))

    def get_point_lines(self, arr, point):
        if not self.point_inside(arr, point):
            return []
        points = []
        my_range = range(self.arr_size)
        points += [arr_sum(point, arr_mul(self.v1_line, i)) for i in my_range]
        points += [arr_sum(point, arr_mul(self.v1_line, -i)) for i in my_range]
        points += [arr_sum(point, arr_mul(self.v2_line, i)) for i in my_range]
        points += [arr_sum(point, arr_mul(self.v2_line, -i)) for i in my_range]
        points += [arr_sum(point, arr_mul(self.hr_line, i)) for i in my_range]
        points += [arr_sum(point, arr_mul(self.hr_line, -i)) for i in my_range]
        return list(filter(lambda x : self.point_inside(arr, x), points))

    def set_black_tiles(self):
        remaining_amount = int(self.edge_size ** 2 // 3)
        while(remaining_amount > 0):
            x = randint(0, self.arr_size - 1)
            y = randint(0, self.arr_size - 1)
            if self.hex_map[y][x] == self.empty:
                self.hex_map[y][x] = self.black
                for i in self.get_point_neighbours(self.hex_map, [y, x]):
                    self.hex_map[i[0]][i[1]] = self.white
                remaining_amount -= 1
        for i in range(self.arr_size):
            for j in range(self.arr_size):
                if self.hex_map[i][j] == self.white:
                    self.hex_map[i][j] = self.empty

    def set_number_on_field(self, number):
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
            self.set_number_on_field(str(current_number))
            current_number += 1

    def set_numbers_on_black(self):
        for y in range(self.arr_size):
            while (self.hex_map[y].count(self.black) != 0):
                x = self.hex_map[y].index(self.black)
                near = self.get_point_neighbours(self.hex_map, [y, x])
                values = set([self.hex_map[p[0]][p[1]] for p in near])
                if self.black in values:
                    values.remove(self.black)
                values = list(values)
                self.hex_map[y][x] = choice(values)


def main():
    a = HitoriGenerator(int(sys.argv[1]))
    a.set_black_tiles()
    a.set_numbers_on_field()
    #a.print_map()
    a.set_numbers_on_black()
    a.print_map()


def foo(i):
    a = HitoriGenerator(i)
    a.set_black_tiles()
    a.set_numbers_on_field()

    a.set_numbers_on_black()
    return a.hex_map

if __name__ == "__main__":
    main()
