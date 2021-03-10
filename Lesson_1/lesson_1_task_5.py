revenue = int(input('Введите выручку: '))
costs = int(input('Введите издержки: '))
if revenue - costs < 0:
    print('Вы работаете в убыток!')
elif revenue - costs == 0:
    print('Вы работали в ноль!')
else:
    print('Рентабельность составляет:', revenue - costs)
    profit = (revenue - costs) / int(input('Введите число сотрудников: '))
    print('Прибыль фирмы на сотрудника составляет:', round(profit, 1))