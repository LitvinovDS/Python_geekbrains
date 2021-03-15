def int_funk(my_string):
    return my_string.title()


user_string = input('Введите строку: ').split(' ')
for word in user_string:
    print(int_funk(word))
