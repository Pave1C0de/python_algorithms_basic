#7. В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба являться минимальными), так и различаться.
def ex7(my_list):
    min_index1 = my_list.index(min(my_list))
    min_index2 = my_list.index(min(my_list[:min_index1]+my_list[min_index1+1:]))
    return my_list[min_index1], my_list[min_index2]


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    my_list = [-760, 35, 700, -270, 101, 100, 40, 81, 60]
    result = ex7(my_list)
    print(result)