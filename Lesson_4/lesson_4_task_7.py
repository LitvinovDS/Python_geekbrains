def fact(n):
    n_fact = 1
    for i in range(1, n+1):
        n_fact = n_fact * i
        yield n_fact


for i, el in enumerate(fact(int(input('Введите число: ')))):
    print(i+1, '! = ',el, sep='')
