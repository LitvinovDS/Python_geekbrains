a = int(input('Сколько пробегает спортсмен в первый день: '))
b = int(input('Какова цель спортсмена: '))
num_days = 1
while a < b:
    a = 1.1 * a
    num_days += 1
print(num_days)