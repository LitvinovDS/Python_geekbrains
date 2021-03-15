def my_funk(num_1, num_2, num_3):
    return num_1 + num_2 + num_3 - min(num_1, num_2, num_3)


print('Сумма наибольших двух: ', my_funk(int(input('Введите первое число: \n')), int(input('Введите второе число: \n')), int(input('Введите третье число: \n'))))
