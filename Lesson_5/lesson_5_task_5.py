# не совсем понял как именно программно заполнять числами файл (пользователь вводит или произвольные числа)
# Поэтому заполнил произвольными числами

from random import randint
with open('lesson_5_task_5_testfile.txt', 'w') as my_file:
    for i in range(20):
        my_file.write(str(randint(0, 100)) + ' ')
with open('lesson_5_task_5_testfile.txt', 'r') as my_file:
    numbers = my_file.readline().rstrip().split(' ')
my_sum = 0
for num in numbers:
    my_sum += int(num)
print(my_sum)
