sec = int(input('Введите время в секундах: '))

hour = sec // 3600
minute = (sec % 3600) // 60
second = sec - 3600*hour - 60*minute

if hour <= 9:
    hour = '0' + str(hour)
if minute <= 9:
    minute ='0' + str(minute)
if second <= 9:
    second ='0' + str(second)

print(hour, minute, second, sep=':')