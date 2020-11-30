def arr_sum(arr1, arr2):
    longer_arr = arr1 if len(arr1) >= len(arr2) else arr2
    return [x + y for x, y in zip(arr1, arr2)] + longer_arr[min(len(arr1), len(arr2)):]


def arr_diff(arr1, arr2):
    subtrahend = [-i for i in arr2]
    return arr_sum(arr1, subtrahend)


def arr_mul(arr, const):
    return [i * const for i in arr]


def arr_copy(arr):
    return [i.copy() for i in arr]


def positions_in_arr(arr, value):
    indices = [i for i in range(len(arr))]
    return list(map(lambda x: x[0], filter(lambda x: x[1] == value, (zip(indices, arr)))))
