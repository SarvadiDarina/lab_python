#Дано текстовий файл, який містить цілі числа.
# Визначити кількість елементів більших за найменший елемент
with open('1.txt') as f:
    numbers = []
    for el in f:
        numbers.append(int(el))
    min_el = min(numbers)
    count_min = numbers.count(min_el)
    res = len(numbers) - count_min
    print(res)