from additional_math import arr_copy, arr_sum, arr_diff, arr_mul
from hexatori import Hexatori
from hexatori_generator import HexatoriGenerator, get_map
from collections import deque


class HexatoriSolver(Hexatori):
    # конструктор класса решателя
    def __init__(self, hex_map):
        self.hex_map = hex_map
        self.wb_map = arr_copy(hex_map)
        self.arr_size = len(hex_map)
        self.set_points_inside()

    # удаляет все уникальные клетки
    def set_uniques_white(self):
        for point in self.points_inside:
            value = self.wb_map[point[0]][point[1]]
            lines = self.get_point_values(
                self.hex_map, self.get_point_lines(point))
            processed_numbers = list(
                filter(lambda elem: elem.isdigit(), lines))
            if processed_numbers.count(value) == 0:
                self.wb_map[point[0]][point[1]] = self.white
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
        return self.hex_map[point[0]][point[1]]

    # возвращает цвет поля, или число, если цвет ещё не задан
    def color_at(self, point):
        if not self.point_inside(point):
            return None
        return self.wb_map[point[0]][point[1]]

    # удаляет клетку, конфликтующую с белой
    def set_point_whose_conflict_is_white(self):
        for point in self.points_inside:
            value = self.wb_map[point[0]][point[1]]
            lines = self.get_point_lines(point)
            for i in lines:
                if self.value_at(i) == value and self.color_at(i) == self.white:
                    self.set_point_black(point)
        self.update_points_inside()

    # делает белой клетку, все конфликты которой - черные
    def clear_conflicts(self):
        for point in self.points_inside:
            lines = self.get_point_lines(point)
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
        for neighbor in self.get_point_neighbours(point):
            if self.color_at(neighbor) == self.black:
                return False
        self.wb_map[point[0]][point[1]] = self.black
        for neighbor in self.get_point_neighbours(point):
            self.set_point_white(neighbor)
        return True

    # окрашивает клетку в белый
    def set_point_white(self, point):
        self.wb_map[point[0]][point[1]] = self.white
        return True

    def set_point_neutral(self, point):
        self.wb_map[point[0]][point[1]] = self.hex_map[point[0]][point[1]]
        return True

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

    def set_point_wo_neighbours_black(self):
        for horizontal_line in range(self.arr_size):
            for vertical_line in range(self.arr_size):
                value = self.wb_map[horizontal_line][vertical_line]
                if not value.isdigit():
                    continue
                point = [horizontal_line, vertical_line]
                neigbours = self.get_point_neighbours(point)
                values = self.get_point_values(self.wb_map, neigbours)
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
                if self.count_conflicts(self.hex_map, point) != 1:
                    continue
                neigbours = self.get_point_neighbours(point)
                neigbour_values = self.get_point_values(self.wb_map, neigbours)
                value_set = set(neigbour_values)
                if len(value_set) != 2:
                    continue
                if self.value_at(point) not in value_set:
                    continue
                if self.white not in value_set:
                    continue
                for neigbour in neigbours:
                    if self.color_at(neigbour) != self.white:
                        if self.count_conflicts(self.hex_map, neigbour) == 1:
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

    def set_points_inside(self):
        points = [[x, y] for x in range(self.arr_size)
                  for y in range(self.arr_size)]
        points = list(filter(lambda x: self.point_inside(x), points))
        points = list(filter(lambda x: self.color_at(x).isdigit(), points))
        self.points_inside = points

    def update_points_inside(self):
        self.points_inside = list(
            filter(lambda point: self.color_at(point).isdigit(), self.points_inside))

    def solve(self):
        self.set_uniques_white()
        self.set_nearly_to_pairs()
        for iteration in range(4):
            self.set_point_whose_conflict_is_white()
            self.set_point_wo_neighbours_black()
            self.clear_conflicts()
            self.set_point_w_white_conflict_neighbour_black()
            self.set_special_pairs()

    def solve_all(self):
        self.solve()
        if self.check_for_success():
            return
        self.wb_map = self.BFS()

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

    def count_not_colored_points(self):
        arr = [self.wb_map[i] for i in range(self.arr_size)]
        merged_arr = []
        for i in arr:
            merged_arr += i
        return len(list(filter(lambda x: x.isdigit(), merged_arr)))

    def BFS(self):
        pass
        temp_wb_map = arr_copy(self.wb_map)
        field_queue = deque()
        field_queue.append(temp_wb_map)
        used = set()

        hashing_dict = dict()
        value = 1
        for i in self.get_conflicts(temp_wb_map):
            hashing_dict[i] = value
            value *= 2

        while (len(field_queue) > 0):
            current_elem = field_queue.popleft()
            conflicts = self.get_conflicts(current_elem)
            hash_value = self.hash_conflicts(hashing_dict, conflicts)
            if hash_value in used:
                continue
            used.add(hash_value)

            for conflict in conflicts:
                temp_map = arr_copy(current_elem)
                temp_map[conflict[0]][conflict[1]] = self.white
                temp_solver = HexatoriSolver(temp_map)
                temp_solver.solve()
                if temp_solver.check_for_success():
                    return temp_solver.wb_map
                field_queue.append(temp_map)
        return self.wb_map

    def get_conflicts(self, hex_map):
        points = [(x, y) for x in range(self.arr_size)
                  for y in range(self.arr_size)]
        result = []
        for point in points:
            if hex_map[point[0]][point[1]].isdigit():
                result.append(point)
        return result

    def hash_conflicts(self, hashing_dict, conflicts):
        result = 0
        for i in conflicts:
            result += hashing_dict[i]
        return result

    def update_map(self):
        for x in range(self.arr_size):
            for y in range(self.arr_size):
                if not self.point_inside([x, y]):
                    continue
                if self.color_at([x, y]) == self.black:
                    for point in self.get_point_neighbours([x, y]):
                        self.wb_map[point[0]][point[1]] = self.white

def test():
    from time import time
    for a in range(2, 100):
        iters = 100# 2000 // int(a ** 1.5) #00 // int(a**1.5)
        t = time()
        ctra = 0
        ctrb = 0
        ptsa = 0
        ptsb = 0
        for i in range(iters):
            ar = HexatoriSolver(get_map(a))
            ptsb += ar.count_not_colored_points()
            ar.solve_all()
            if ar.check_for_success():
                ctra += 1
            ctrb += 1
            ptsa += ar.count_not_colored_points()
        print('-' * 30)
        print('size:                 ', a)
        print('iterations:           ', iters)
        time_ms = time() - t
        print('total time:           ', int(time_ms * 1000), 'ms')
        print('time for iteration:   ', int((time_ms / iters) * 1000), 'ms')
        print('total:                ', ctrb)
        print('succeed:              ', ctra)
        print('success percent:      ', int((ctra / ctrb) * 1000) / 10)
        print('remaining points:     ', ptsa / iters)
        print('total points:         ', ptsb/iters)
        print('remaining percent:    ', (ptsa / ptsb) * 100)


if __name__ == "__main__":
    test()
