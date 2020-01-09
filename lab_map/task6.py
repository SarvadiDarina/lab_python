# Дано масив (список) елементів цілого типу.
# Знайти суму додатних елементів
from functools import reduce
count = int(input('Кількість елементів: '))
element_list = [int(input('Введіть елемент: ')) for x in range(count)]
positiv_el = list(filter(lambda x: x > 0, element_list))
suma = reduce(lambda suma, x: suma + x, positiv_el, 0)
print('Сумa додатнiх елементів = {0}'.format(suma))
