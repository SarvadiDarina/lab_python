#Дана цілочислова прямокутна матриця.Визначити добуток додатних елементів матриці
# вище головної діагоналі.

n = int(input('Кількість рядків: '))
m = int(input('Кількість стовпців: '))
matrix = [
    [int(input('Елементи: ')) for i in range(m)] for j in range(n)
    ]
for el in matrix:
    print(el)
product = 1
for j in range(n):
    for i in range(n):
        if j < i and matrix[j][i] > 0:
            product *= matrix[j][i]
print(product)
