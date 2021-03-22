from itertools import cycle

my_list = [int(i) for i in input('Введите элементы массива через пробел: ').split(' ')]
my_list_new = []
next_num = cycle(my_list)
for i in range(len(my_list)):
    my_list_new.append(next(next_num))
print('Новый массив: ', my_list_new)
