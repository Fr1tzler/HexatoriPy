from additional_math import *
from hitori_generator import foo


class HitoriSolver:
    empty = 'e'
    border = 'r'
    black = 'b'
    white = 'w'

    hr_line = [0, -1]
    v1_line = [-1, 0]
    v2_line = [-1, -1]

    # конструктор класса решателя
    def __init__(self, hex_array):
        self.hex_array = hex_array
        self.wb_array = arr_copy(hex_array)
        self.arr_size = len(hex_array)
        self.get_points_inside()

    # удаляет все уникальные клетки
    def set_uniques_white(self):
        for point in self.points_inside:
            value = self.wb_array[point[0]][point[1]]
            lines = self.get_point_values(self.hex_array, self.get_point_lines(point))
            processed_numbers = list(filter(lambda elem : elem.isdigit(), lines))
            if processed_numbers.count(value) == 0:
                self.wb_array[point[0]][point[1]] = self.white
        self.update_points_inside()
 
    # удяляет клетки с конфликтами поблизости
    def set_nearly_to_pairs(self):
        for point in self.points_inside:
            pv1 = arr_sum(point, self.v1_line)
            pv2 = arr_sum(point, self.v2_line)
            ph = arr_sum(point, self.hr_line)
            pv1m = arr_diff(point, self.v1_line)
            pv2m = arr_diff(point, self.v2_line)
            phm = arr_diff(point, self.hr_line)
            if self.value_at(pv1) == self.value_at(pv2) and self.value_at(pv1) != None:
                self.set_point_white(point)
            elif self.value_at(pv2) == self.value_at(ph) and self.value_at(pv2) != None:
                self.set_point_white(point)
            elif self.value_at(ph) == self.value_at(pv1m) and self.value_at(ph) != None:
                self.set_point_white(point)
            elif self.value_at(pv1m) == self.value_at(pv2m) and self.value_at(pv1m) != None:
                self.set_point_white(point)
            elif self.value_at(pv2m) == self.value_at(phm) and self.value_at(pv2m) != None:
                self.set_point_white(point)
            elif self.value_at(phm) == self.value_at(pv1) and self.value_at(phm) != None:
                self.set_point_white(point)
            elif self.value_at(phm) == self.value_at(ph) and self.value_at(phm) != None:
                self.set_point_white(point)
            elif self.value_at(pv1) == self.value_at(pv1m) and self.value_at(pv1) != None:
                self.set_point_white(point)
            elif self.value_at(pv2) == self.value_at(pv2m) and self.value_at(pv2) != None:
                self.set_point_white(point)
        self.update_points_inside()
    
    # возващает численное значение на поле
    def value_at(self, point):
        if not self.point_inside(point):
            return None
        return self.hex_array[point[0]][point[1]]
    
    # возвращает цвет поля, или число, если цвет ещё не задан
    def color_at(self, point):
        if not self.point_inside(point):
            return None
        return self.wb_array[point[0]][point[1]]
    
    # удаляет клетку, конфликтующую с белой
    def set_point_whose_conflict_is_white(self):
        for point in self.points_inside:
            value = self.wb_array[point[0]][point[1]]
            lines = self.get_point_lines(point)
            for i in lines:
                if self.value_at(i) == value and self.color_at(i) == self.white:
                    self.set_point_black(point)
        self.update_points_inside()
               
    # делает белой клетку, все конфликты которой - черные
    def clear_conflicts(self):
        for point in self.points_inside:
            lines  = self.get_point_lines(point)
            flag = True
            value = self.value_at(point)
            for i in lines:
                if self.value_at(i) != value:
                    continue
                if self.color_at(i) != self.black:
                    flag = False
            if flag:
                self.set_point_white(point)
        self.update_points_inside()

    # окрашивает клетку в чёрный
    def set_point_black(self, point):
        self.wb_array[point[0]][point[1]] = self.black
        for neighbor in self.get_point_neighbours(point):
            self.set_point_white(neighbor)

    # окрашивает клетку в белый
    def set_point_white(self, point):
        self.wb_array[point[0]][point[1]] = self.white

    # возвращает значения клеток из указанной карты
    def get_point_values(self, hex_map, points):
        res = []
        for point in points:
            res.append(hex_map[point[0]][point[1]])
        return res

    # возвращает линии, содержащие поле
    def get_point_lines(self, point):
        hr = self.get_line(point, self.hr_line)
        v1 = self.get_line(point, self.v1_line)
        v2 = self.get_line(point, self.v2_line)
        result = []
        for i in hr + v1 + v2:
            if result.count(i) == 0:
                result.append(i)
        return result

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
        return self.wb_array[point[0]][point[1]] != self.border

    def get_point_neighbours(self, point):
        if not self.point_inside(point):
            return []
        point_arr = []
        point_arr.append(arr_sum(point, self.hr_line))
        point_arr.append(arr_sum(point, self.v2_line))
        point_arr.append(arr_sum(point, self.v1_line))
        point_arr.append(arr_diff(point, self.hr_line))
        point_arr.append(arr_diff(point, self.v2_line))
        point_arr.append(arr_diff(point, self.v1_line))
        return list(filter(lambda x : self.point_inside(x), point_arr))

    def set_point_wo_neighbours_black(self):
        for horizontal_line in range(self.arr_size):
            for vertical_line in range(self.arr_size):
                value = self.wb_array[horizontal_line][vertical_line]
                if not value.isdigit():
                    continue
                point = [horizontal_line, vertical_line]
                neigbours = self.get_point_neighbours(point)
                values = self.get_point_values(self.wb_array, neigbours)
                if values.count(self.white) == len(values):
                    self.set_point_black(point)

    def count_conflicts(self, arr, point):
        lines = self.get_point_lines(point)
        res = 0
        value = self.value_at(point)
        for i in lines:
            if self.value_at(i) == value and self.color_at(i) != self.black:
                res += 1
        return res

    def set_special_pairs(self):
        for horizontal_line in range(self.arr_size):
            for vertical_line in range(self.arr_size):
                point = [horizontal_line, vertical_line]
                if self.color_at(point) == None or not self.color_at(point).isdigit():
                    continue
                if self.count_conflicts(self.hex_array, point) != 1:
                    continue
                neigbours = self.get_point_neighbours(point)
                neigbour_values = self.get_point_values(self.wb_array, neigbours)
                value_set = set(neigbour_values)
                if len(value_set) != 2:
                    continue
                if self.value_at(point) not in value_set:
                    continue
                if self.white not in value_set:
                    continue
                for neigbour in neigbours:
                    if self.color_at(neigbour) != self.white:
                        if self.count_conflicts(self.hex_array, neigbour) == 1:
                            self.set_point_black(point)
                        else:
                            self.set_point_black(neigbour)
    
    def set_point_w_white_conflict_neighbour_black(self):
        for horizontal_line in range(self.arr_size):
            for vertical_line in range(self.arr_size):
                point = [horizontal_line, vertical_line]
                value = self.value_at(point)
                neigbours = self.get_point_neighbours(point)
                for i in neigbours:
                    if self.value_at(i) == value and self.color_at(i) == self.white:
                        self.set_point_black(point)
                        break

    def print_map(self):
        l = 0
        print('-' * self.arr_size * 2)
        for i in range(self.arr_size):
            print(' ' * abs(i - (self.arr_size + 1) // 2 + 1), end=' ')
            filtered_arr = filter(lambda x : x != self.border, self.wb_array[i])
            for j in filtered_arr:
                if j == self.white:
                    l += 0
                    print('_', end = ' ')
                elif j == self.black:
                    l += 0
                    print(self.black, end = ' ')     
                else:
                    l += 1
                    print(j, end = ' ')
            print()
        return l

    def count_map(self):
        l = 0
        for i in range(self.arr_size):
            filtered_arr = filter(lambda x : x != self.border, self.wb_array[i])
            for j in filtered_arr:
                if j == self.white or j == self.black:
                    l += 0
                else:
                    l += 1
        return l

    def three_problem(self):
        pass

    def BFS(self):
        pass

    def get_points_inside(self):
        self.points_inside = []
        for horizontal_line in range(self.arr_size):
            for vertical_line in range(self.arr_size):
                point = [horizontal_line, vertical_line]
                if not self.point_inside(point):
                    continue
                value = self.wb_array[horizontal_line][vertical_line]
                if not value.isdigit():
                    continue
                self.points_inside.append(point)

    def update_points_inside(self):
        self.points_inside = list(filter(lambda point : self.color_at(point).isdigit(), self.points_inside))
        
    def solve(self):
        self.set_uniques_white()
        self.set_nearly_to_pairs()
        for i in range(5):
            self.set_point_whose_conflict_is_white()
            self.set_point_wo_neighbours_black()
            self.clear_conflicts()
            self.set_point_w_white_conflict_neighbour_black()
            self.set_special_pairs()
            self.three_problem()
        self.BFS()

    def check_for_success(self):
        for horizontal_line in range(self.arr_size):
            for vertical_line in range(self.arr_size):
                point = [horizontal_line, vertical_line]
                value = self.value_at(point)
                if self.color_at(point) == self.black:
                    continue
                lines = self.get_point_lines(point)
                for i in lines:
                    if self.value_at(i) == value:
                        if self.color_at(i) != self.black:
                            return False
        return True

from time import time
for a in range(2, 25):
    iters = 2000 // int(a ** 1.5) + 1
    print('size:                 ', a)
    print('iterations:           ', iters)
    t = time()
    ctra = 0
    ctrb = 0
    for i in range(iters):
        ar = HitoriSolver(foo(a))
        ar.solve()
        if ar.check_for_success():
            ctra += 1
        ctrb += 1
    print('time for iteration:   ', int(((time() - t) / iters) * 1000), 'ms')
    print('total:                ', ctrb)
    print('succeed:              ', ctra)
    print('percent:              ', int((ctra / ctrb) * 1000) / 10)
    print('-' * 30)