#5. В массиве найти максимальный отрицательный элемент.
# Вывести на экран его значение и позицию в массиве.
def ex5(my_list):
    val = min(my_list)
    if val < 0:
        index = my_list.index(val)
        return val, index
    else:
        return None, None

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    my_list = [76, 35, 7, 97, 46, -7, -27, 40, 81, 60]
    result = ex5(my_list)
    print(result)