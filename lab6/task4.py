#Стиснути масив, вилучивши з нього всі елементи, модуль яких не перевищує 1,
# місце яке звільнилось в кінці масиву заповнити нулями.
n = int(input('Введіть кількість елементів : '))
num_list = [float(input('Введіть чиcло : ')) for x in range(n)]
result = [i for i in num_list if abs(i) > 1]
r = len(num_list) - len(result)
for x in range(r):
    result.append(0)
print('Результат = {0}'.format(result))