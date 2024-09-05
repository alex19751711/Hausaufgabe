immutable_var = 'Year', 2015, False
print('Immutable tuple:', immutable_var)
# immutable_var[2] = True // Попытка изменить элемент кортежа! Это невозможно, так как кортеж относится к
# print(immutable_var)  // неизменяемым типам данных и не поддерживает обращение по элементам
mutable_list = ['Year', 2015, False]
print('Mutable list (original):', mutable_list)
mutable_list[1] = 2024
mutable_list[2] = True
mutable_list.append('Modified by AV Grishin')
print('Mutable list (modified):', mutable_list)
