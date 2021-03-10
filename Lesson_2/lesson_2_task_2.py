print('Введите целые числа через пробел:')
my_list = [int(i) for i in input().split()]
print('Ваш список:', my_list)
for i in range(len(my_list)//2):
    num = my_list[i*2 + 1]
    my_list[i*2 + 1] = my_list[i*2]
    my_list[i*2] = num
print('Новый список:', my_list)
