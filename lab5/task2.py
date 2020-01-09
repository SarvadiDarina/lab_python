#Дано натуральне число n, побудувати алгоритм для визнач
num = int(input('Введіть число: '))
min = 10
while num>0:
    if num%10 < min:
        min = num%10
    num = num//10
print('Найменшe число= {0}'.format(min))