def even_sum(lst):
    list1 = lst[::2]
    sum_list = sum(list1)
    return sum_list

data = [
    [1, 2, 3, 4, 5, 6, 7],
    [-1, -2, -3, -4, -5, -6, -7],
    [99, 56, 209, -308, -12, -18, 42],
    [-1, -2, -3, 0, 1, 2, 3],
]

test_data = [
    16, -16, 338, 0
]


for i, d in enumerate(data):
    assert even_sum(d) == test_data[i], f'С набором {d} есть ошибка, не проходит проверку'
    print(f'Тестовый набор {d} прошёл проверку')
print('Всё ок')
