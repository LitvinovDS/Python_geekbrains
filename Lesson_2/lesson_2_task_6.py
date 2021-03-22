def set_list(my_key, product):
    in_list = list()
    for n in range(len(product)):
        if product[n][1][my_key] not in in_list:
            in_list.append(product[n][1][my_key])
    return in_list
# функция для наполнения итоговых списков аналитики БЕЗ ПОВТОРОВ !


num = int(input('Сколько товарных позиций добавить? '))
products = list()
for i in range(num):
    print('Товар № ', i+1, ':', sep='')
    title = input('Введите название: ')
    price = int(input('Введите цену: '))
    quantity = int(input('Введите количество: '))
    products.append((i+1, {'название': title, 'цена': price, 'количество': quantity, 'eд': 'шт.'}))

result_dict = {}
for i in products[0][1].keys():
    result_dict.update({i: set_list(i, products)})

print(result_dict)
