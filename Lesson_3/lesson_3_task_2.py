'''Функция вернет только те данные о пользователе, которые в нее передали'''
def user(firstname='', lastname='', birthday='', city='', email='', phone=''):
    return " ".join([firstname, lastname, birthday, city, email, phone])


print(user(firstname='Nikola', lastname='Tesla', birthday='10.07.1856', city='Smiljan'))
