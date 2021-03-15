def my_funk(num):
    sum_str = 0
    for i in range(len(num)):
        if num[i] == '$':
            return sum_str
        else:
            sum_str += int(num[i])
    return sum_str


print('Для завершения работы программы введите знак $')
my_sum = 0
while True:
    numbers = input('Введите строку: ').split(' ')
    if '$' not in numbers:
        my_sum += my_funk(numbers)
        print('Сумма = ', my_sum)
    else:
        my_sum += my_funk(numbers)
        print('Работа программы завершена, итоговая сумма = ', my_sum)
        break
