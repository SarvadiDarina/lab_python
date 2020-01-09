#  Дано масив (список) елементів цілого типу.Знайти середнє арифметичне.
from functools import reduce
a = int(input('Введіть кількість елементів: '))
b = [int(input('Введіть елемент: ')) for x in range(a)]
suma = reduce(lambda suma, el: suma + el, b , 0)
arithmetic_mean = suma / len(b)
print('Середнє арифметичне = {0}'.format(arithmetic_mean))
