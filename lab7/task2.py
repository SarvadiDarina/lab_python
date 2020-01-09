#Дано дійсну матрицю розмірності nxn , всі елементи якої різні
# Знайти скаляр¬ний добуток i-го рядка і j-го стовпчика
# (i, j задаються користувачем)
n = int(input('Розмір матриці: '))
matrix = [[int(input('El [{0}][{1}]: '.format(i, j))) for i in range(n)] for j in range(n)]
for el in matrix:
    print(el)
i = int(input('Введіть рядок = '))
j = int(input('Введіть стовпчик = '))
A = matrix[i]  # i-ряд
B = [row[j] for row in matrix]  # j-стовпчик
C = sum(a * b for a, b in zip(A, B))
print(C)