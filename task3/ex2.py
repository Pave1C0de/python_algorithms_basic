#2. Во втором массиве сохранить индексы четных элементов первого массива.
# Например, если дан массив со значениями 8, 3, 15, 6, 4, 2,
# то во второй массив надо заполнить значениями 1, 4, 5, 6 (или 0, 3, 4, 5 - если индексация начинается с нуля),
# т.к. именно в этих позициях первого массива стоят четные числа.
def ex2(my_list):
    even_vals_indexes = []
    for i in range(len(my_list)):
        if my_list[i]%2 == 0:
            even_vals_indexes.append(i)
    return even_vals_indexes


if __name__ == '__main__':
    my_list = [0, 2, 4, 13, 7, 9, 8, 6, 1, 4]
    result = ex2(my_list)
    print(my_list)
    print(result)