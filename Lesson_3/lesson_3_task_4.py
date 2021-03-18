def my_funk(num_1, num_2):
    result = 1
    for i in range(-num_2):
        result *= num_1
    return 1/result


x, y = int(input('Введите число: ')), int(input('Введите степень: '))
print('Решение через встроенный оператор: ', x**y)
print('Решение через my_funk: ', my_funk(x, y))
