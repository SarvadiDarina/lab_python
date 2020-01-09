#Дано матриці  A і B
# Знайти матрицю  C= A x B.
k1 = int(input('Рядок 1: '))  # count of rows in 1 matrix
j1 = int(input('Стовпчик 1: '))  # count of columns in 1 matrix
k2 = int(input('Рядок 2: '))  # count of rows in 2 matrix
j2 = int(input('Стовпчик2: '))  # count of columns in 2 matrix

if j1 == k2:
    A = [[int(input('El [{0}][{1}]: '.format(k, j))) for k in range(j1)] for j in range(k1)]
    for h in A:
        print(h)
    B = [[int(input('El [{0}][{1}]: '.format(x, y))) for x in range(j2)] for y in range(k2)]
    for q in B:
        print(q)
    result = [[0 for x in range(j2)] for y in range(k1)]
    for k in range(len(A)):  # iterate through rows of A
        for j in range(len(B[0])):  # iterate through columns of B
            for m in range(len(B)):  # iterate through rows of B
                result[k][j] += A[k][m] * B[m][j]
    for s in result:
        print(s)
else:
    print('Неправильний розмір матриць')