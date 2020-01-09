#  Дано масив (список) елементів цілого типу.
#  Підрахувати кількість елементів, які більші за середнє арифметичне.
from functools import reduce
count = int(input('Введіть кількість: '))
element_list = [int(input('Елементи: ')) for x in range(count)]
suma = reduce((lambda suma, el: suma + el), element_list, 0)
element = suma / len(element_list)
result = len(list(filter(lambda el: el > element, element_list)))
print('Відповідь = {0}'.format(result))
