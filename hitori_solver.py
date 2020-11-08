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

    def __init__(self, hex_array):
        self.hex_array = hex_array
        self.wb_array = arr_copy(hex_array)
        self.arr_size = len(hex_array)

    # удаляет все уникальные клетки
    def set_uniques_white(self):
        for horizontal_line in range(self.arr_size):
            for vertical_line in range(self.arr_size):
                value = self.wb_array[horizontal_line][vertical_line]
                if not value.isdigit():
                    continue
                point = [horizontal_line, vertical_line]
                lines = self.get_point_values(self.hex_array, self.get_point_lines(point))
                processed_numbers = self.get_numbers(lines)
                if processed_numbers.count(value) == 0:
                    self.wb_array[horizontal_line][vertical_line] = self.white
    #удяляет клетки с конфликтами поблизости
    def set_nearly_to_pairs(self):
        for horizontal_line in range(self.arr_size):
            for vertical_line in range(self.arr_size):
                value = self.wb_array[horizontal_line][vertical_line]
                if not value.isdigit():
                    continue
                point = [horizontal_line, vertical_line]
                pv1 = arr_sum(point, self.v1_line)
                pv2 = arr_sum(point, self.v2_line)
                ph = arr_sum(point, self.hr_line)
                pv1m = arr_diff(point, self.v1_line)
                pv2m = arr_diff(point, self.v2_line)
                phm = arr_diff(point, self.hr_line)
                if self.value_at(pv1) == self.value_at(pv2) and self.value_at(pv1) != None:
                    self.wb_array[horizontal_line][vertical_line] = self.white
                elif self.value_at(pv2) == self.value_at(ph) and self.value_at(pv2) != None:
                    self.wb_array[horizontal_line][vertical_line] = self.white
                elif self.value_at(ph) == self.value_at(pv1m) and self.value_at(ph) != None:
                    self.wb_array[horizontal_line][vertical_line] = self.white
                elif self.value_at(pv1m) == self.value_at(pv2m) and self.value_at(pv1m) != None:
                    self.wb_array[horizontal_line][vertical_line] = self.white
                elif self.value_at(pv2m) == self.value_at(phm) and self.value_at(pv2m) != None:
                    self.wb_array[horizontal_line][vertical_line] = self.white
                elif self.value_at(phm) == self.value_at(pv1) and self.value_at(phm) != None:
                    self.wb_array[horizontal_line][vertical_line] = self.white
                elif self.value_at(phm) == self.value_at(ph) and self.value_at(phm) != None:
                    self.wb_array[horizontal_line][vertical_line] = self.white
                elif self.value_at(pv1) == self.value_at(pv1m) and self.value_at(pv1) != None:
                    self.wb_array[horizontal_line][vertical_line] = self.white
                elif self.value_at(pv2) == self.value_at(pv2m) and self.value_at(pv2) != None:
                    self.wb_array[horizontal_line][vertical_line] = self.white
    
    def value_at(self, point):
        if not self.point_inside(point):
            return None
        return self.hex_array[point[0]][point[1]]
    
    def color_at(self, point):
        if not self.point_inside(point):
            return None
        return self.wb_array[point[0]][point[1]]
    # удаляет клетку, конфликтующую с белой
    def set_point_whose_conflict_is_white(self):
        for horizontal_line in range(self.arr_size):
            for vertical_line in range(self.arr_size):
                value = self.wb_array[horizontal_line][vertical_line]
                if not value.isdigit():
                    continue
                point = [horizontal_line, vertical_line]
                lines = self.get_point_lines(point)
                values = self.get_point_values(self.hex_array, self.get_point_lines(point))
                if values.count(value) == 1:
                    for i in lines:
                        if self.value_at(i) == value and self.color_at(i) == self.white:
                            self.set_point_black(point)
                            break

    def set_point_whose_conflict_is_white_v2(self):
        for horizontal_line in range(self.arr_size):
            for vertical_line in range(self.arr_size):
                value = self.wb_array[horizontal_line][vertical_line]
                if not value.isdigit():
                    continue
                point = [horizontal_line, vertical_line]
                lines = self.get_point_lines(point)
                for i in lines:
                    if self.value_at(i) == value and self.color_at(i) == self.white:
                        self.set_point_black(point)

                        
    # удаляет клетку, конфликтующую с черной
    def clear_conflicts(self):
        for horizontal_line in range(self.arr_size):
            for vertical_line in range(self.arr_size):
                value = self.wb_array[horizontal_line][vertical_line]
                if not value.isdigit():
                    continue
                point = [horizontal_line, vertical_line]
                lines = self.get_point_lines(point)
                flag = True
                for i in lines:
                    if self.value_at(i) != value:
                        continue
                    if self.color_at(i) != self.black:
                        flag = False
                if flag:
                    self.wb_array[horizontal_line][vertical_line] = self.white
                        
    def set_point_black(self, point):
        self.wb_array[point[0]][point[1]] = self.black
        points = self.get_point_neighbours(point)
        for i in points:
            self.wb_array[i[0]][i[1]] = self.white

    def get_numbers(self, arr):
        res = []
        for i in arr:
            if i.isdigit():
                res.append(i)
        return res

    def get_point_values(self, arr, points):
        res = []
        for i in points:
            res.append(arr[i[0]][i[1]])
        return res

    def get_point_lines(self, point):
        hr = self.get_line(point, self.hr_line)
        v1 = self.get_line(point, self.v1_line)
        v2 = self.get_line(point, self.v2_line)
        res = hr + v1 + v2
        res2 = []
        for i in res:
            if res2.count(i) == 0:
                res2.append(i)
        return res2

    def get_line(self, point, direction):
        if not self.point_inside(point):
            return []
        points = []
        my_range = range(1, self.arr_size + 1)
        points += [arr_sum(point, arr_mul(direction, i)) for i in my_range]
        points += [arr_sum(point, arr_mul(direction, -i)) for i in my_range]
        res = list(filter(lambda x : self.point_inside(x), points))
        return res

    def point_inside(self, point):
        if point[0] < 0 or point[0] >= self.arr_size:
            return False
        if point[1] < 0 or point[1] >= self.arr_size:
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
                            return 0
        return 1

    def three_problem(self):
        pass

    def BFS(self):
        pass

    def solve(self):
        total = self.count_map()
        self.set_uniques_white()
        self.set_nearly_to_pairs()
        for i in range(5):
            self.set_point_whose_conflict_is_white_v2()
            self.set_point_wo_neighbours_black()
            self.clear_conflicts()
            self.set_point_w_white_conflict_neighbour_black()
            self.set_special_pairs()
            self.three_problem()
        self.BFS()


i = 20
ar = HitoriSolver(foo(i))
ar.print_map()
ar.solve()
print(ar.print_map())
print(ar.check_for_success())
'''

q = 625
from time import time
for a in range(2, 25):
    iters = q // int(a ** 1.5) + 1
    print('size:                 ', a)
    print('iterations:           ', iters)
    t = time()
    ctra = 0
    ctrb = 0
    for i in range(iters):
        ar = HitoriSolver(foo(a))
        res = ar.solve()
        ctra += ar.check_for_success()
        ctrb += 1
    print('time for iteration:   ', int(((time() - t) / iters) * 1000), 'ms')
    print('total:                ', ctra)
    print('succeed:              ', ctrb)
    print('percent:              ', int((ctra / ctrb) * 1000) / 10)
    print('-' * 30)
    '''