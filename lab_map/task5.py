# Дано масив (список) елементів цілого типу.
#  Знайти добуток від’ємних елементів.
from functools import reduce
a = int(input('Введіть кількість елементів: '))
list_el = [float(input('Введіть елемент: ')) for x in range(a)]
neg_el = list(filter(lambda x: x < 0, list_el))
if len(neg_el) == 0:
	print('Від’ємних елементів немає')
else:
	result = reduce((lambda result, x: result * x), 	neg_el, 1)
	print('Добуток відємних елементів = {0}'.format(result))
