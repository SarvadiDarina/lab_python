#Елементи масиву A=(ai), (ai=1,2,....n) задаються так:....Обчислити z
from math import cos
i = int(input('Введіть i = '))
list_el = []
numerator = 1
denominator = 0
sum_pos = 0
sum_neg = 0
for x in range(1, i + 1):
    product = (2 * x - 1) * (cos(x))
    denominator += x ** 2
    numerator *= product
    element = numerator / denominator
    if element > 0:
        sum_pos += 1
    else:
        sum_neg += 1
    list_el.append(element)
if sum_neg < sum_pos:
    print(-1)
else:
    print(1)