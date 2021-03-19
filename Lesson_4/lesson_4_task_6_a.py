from itertools import count
from time import sleep

for i in count(int(input('С какого числа начнем? '))):
    print(i)
    sleep(0.5) # для задержки вывода
