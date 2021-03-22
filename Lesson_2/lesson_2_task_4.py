my_list = [i for i in input('Введите строку: ').split()]
for i in range(len(my_list)):
    print(i+1, my_list[i][0:10:1])
