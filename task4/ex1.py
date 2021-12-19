#1. Проанализировать скорость и сложность одного любого алгоритма, разработанных в рамках
# домашнего задания первых трех уроков.
#Примечание: попробуйте написать несколько реализаций алгоритма и сравнить их.

import time
import random
def get_func_time(func):
    def wrapper(arg):
        start_time = time.time_ns()
        result = func(arg)
        stop_time = time.time_ns()
        delta_time = stop_time - start_time
        print(f"Время выполнения функции: {delta_time} ns")
        print(f"Результат выполнения функции:\n {result}")
        return result, delta_time
    return wrapper
@get_func_time
#7. В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба являться минимальными), так и различаться.
def ex7(my_list):
    min_index1 = my_list.index(min(my_list))
    min_index2 = my_list.index(min(my_list[:min_index1]+my_list[min_index1+1:]))
    return my_list[min_index1], my_list[min_index2]

@get_func_time
#7. В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба являться минимальными), так и различаться.
def ex7_1(my_list):
    min_index1 = my_list.index(min(my_list))
    if my_list[:min_index1] == []:
        if my_list[min_index1 + 1:] == []:
            return my_list[min_index1], None
        else:
            min_index_2half = my_list.index(min(my_list[min_index1 + 1:]))
            return  my_list[min_index1], my_list[min_index_2half]
    else:
        if my_list[min_index1 + 1:] == []:
            min_index_1half = my_list.index(min(my_list[:min_index1]))
            return  my_list[min_index1], my_list[min_index_1half]
        else:
            min_index_1half = my_list.index(min(my_list[:min_index1]))
            min_index_2half = my_list.index(min(my_list[min_index1 + 1:]))
            min_val = min([my_list[min_index_1half], my_list[min_index_2half]])
            return  my_list[min_index1], min_val

@get_func_time
def ex7_2(my_list):
    min_index1 = my_list.index(min(my_list))
    new_list = my_list[:min_index1]+my_list[min_index1+1:]
    min_val1 = my_list[min_index1]
    min_val2 = min(new_list)
    return min_val1, min_val2




def ex1(rand_list):
    time1 = ex7(rand_list)[1]
    time2 = ex7_1(rand_list)[1]
    time3 = ex7_2(rand_list)[1]
    return time1, time2, time3

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    f1_time = []
    f2_time = []
    f3_time = []
    for j in range(1000):
        rand_list = []
        for i in range(10000):
            rand_list.append(random.randint(-100000, 100000))
        print("=="*10)
        t1, t2, t3 = ex1(rand_list)
        f1_time.append(t1)
        f2_time.append(t2)
        f3_time.append(t3)
    print(sum(f1_time)/len(f1_time), sum(f2_time)/len(f2_time), sum(f3_time)/len(f3_time))

# Сложность выполнения функций одинакова и равнва =  О(n)
# Несколько запусков алгоритмов показывают приблизительно одинаковое время
# f1        f2      f3
# 776828.9 799955.1 659113.6
# 874284.5 755024.3 644501.0
# 977456.1 819340.9 847932.1
# 948813.2 801858.5 738161.4
# 1202220.8 854590.3 667339.0
# 974618.7 1000811.2 746717.8
# 949627.4 1055492.1 719798.3