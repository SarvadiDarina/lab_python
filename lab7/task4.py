#	Розмістити елементи непарних стовпців у порядку зростання.
n = int(input('Розмір матриці= '))
matrix = [[int(input("El {0},{1} = ".format(k, l))) for l in range(n)] for k in range(n)]
print('Задана матриця')
for row in matrix:
    print(row)

transposed_matrix = [[matrix[l][k] for l in range(len(matrix))] for k in range(len(matrix))]
res = []
for row in transposed_matrix:
    if transposed_matrix.index(row) % 2 == 0:
        res.append(sorted(row))

    if transposed_matrix.index(row) % 2 != 0:
        res.append(row)

print('Відсортована матриця ')
transposed_res = [[res[l][k] for l in range(len(res))] for k in range(len(res))]
for j in transposed_res:
    print(j)