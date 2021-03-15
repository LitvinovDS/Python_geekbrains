'''В функции реализована проверка деления на ноль'''
def my_funk(num_1, num_2):
    try:
        return round(num_1 / num_2, 2)
    except ZeroDivisionError:
        return 'Деление на ноль!'


print('Результат: ', my_funk(float(input('Введите делимое: \n')), float(input('Введите делитель: \n'))))
