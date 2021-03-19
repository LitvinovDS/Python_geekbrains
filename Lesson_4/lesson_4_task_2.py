my_list = [int(i) for i in input('Введите числа через пробел: ').split(' ')]
my_list_new = [my_list[i] for i in range(len(my_list) - 1) if my_list[i] > my_list[i-1] and i!=0]
print(my_list_new)
