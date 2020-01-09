#Дано  n дійсних чисел: x1,x2,x3....xn . Знайти найменше серед них.
k = int(input('Введіт кількість чисел: '))
num = [float(input('Введіть число = ')) for i in range(k)]
min = num[0]
for i in num:
    if i < min:
        min = i
print('Найменше число = {0}'.format(min))