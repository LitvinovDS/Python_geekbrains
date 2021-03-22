my_list = [int(i) for i in input('Введите числа через пробел: ').split(' ')]
my_list_new = [elem for elem in my_list if my_list.count(elem) == 1]
print(my_list_new)
