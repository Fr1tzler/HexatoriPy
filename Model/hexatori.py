from additional_math import *

class Hexatori():
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

    def get_point_neighbours(self, point):
        if not self.point_inside(point):
            return []
        point_arr = []
        point_arr.append(arr_sum(point, self.v2_line))
        point_arr.append(arr_sum(point, self.hr_line))
        point_arr.append(arr_sum(point, self.v1_line))
        point_arr.append(arr_diff(point, self.v2_line))
        point_arr.append(arr_diff(point, self.hr_line))
        point_arr.append(arr_diff(point, self.v1_line))
        return list(filter(lambda x : self.point_inside(x), point_arr))

    def get_point_lines(self, arr, point):
        if not self.point_inside(point):
            return []
        points = []
        my_range = range(self.arr_size)
        points += [arr_sum(point, arr_mul(self.v1_line, i)) for i in my_range]
        points += [arr_sum(point, arr_mul(self.v1_line, -i)) for i in my_range]
        points += [arr_sum(point, arr_mul(self.v2_line, i)) for i in my_range]
        points += [arr_sum(point, arr_mul(self.v2_line, -i)) for i in my_range]
        points += [arr_sum(point, arr_mul(self.hr_line, i)) for i in my_range]
        points += [arr_sum(point, arr_mul(self.hr_line, -i)) for i in my_range]
        return list(filter(lambda x : self.point_inside(x), points))

    # возвращает линию, содержащую поле
    def get_line(self, point, direction):
        points = []
        my_range = range(1, self.arr_size + 1)
        points += [arr_sum(point, arr_mul(direction, i)) for i in my_range]
        points += [arr_sum(point, arr_mul(direction, -i)) for i in my_range]
        res = list(filter(lambda x : self.point_inside(x), points))
        return res

    # возвращает True, если клетка внутри сетки
    def point_inside(self, point):
        if point[0] < 0 or point[0] >= self.arr_size or point[1] < 0 or point[1] >= self.arr_size:
            return False
        return self.hex_map[point[0]][point[1]] != self.border
