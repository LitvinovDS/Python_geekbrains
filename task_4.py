num = abs(int(input('Введите целое число: ')))
max_num = num % 10
while num // 10 > 0:
    if max_num < num % 10:
        max_num = num % 10
    num = num // 10
print('Наибольшая цифра:', max_num)