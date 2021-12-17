#6. В одномерном массиве найти сумму элементов,
# находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.
def ex6(my_list):
    min_val_index = my_list.index(min(my_list))
    max_val_index = my_list.index(max(my_list))
    if   min_val_index < max_val_index:
        return sum(my_list[min_val_index + 1: max_val_index])
    elif min_val_index > max_val_index:
        return sum(my_list[max_val_index + 1: min_val_index])
    else:
        None


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    my_list = [76, 35, 700, -1, 101, 100, -270, 40, 81, 60]
    result = ex6(my_list)
    print(result)