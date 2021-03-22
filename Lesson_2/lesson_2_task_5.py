my_list = [7, 5, 3, 3, 2]
num = int(input('Введите число: '))
if num in my_list:
    i = len(my_list) - my_list[::-1].index(num) - 1
    my_list = my_list[:i] + [num] +  my_list[i:]
else:
    if my_list[-1] > num:
        my_list.append(num)
    else:
        for i in range(len(my_list)):
            if num >= my_list[i]:
                my_list = my_list[:i] + [num] + my_list[i:]
                break
print(my_list)
