# 1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
# заданный случайными числами на промежутке [-100; 100).
# Выведите на экран исходный и отсортированный массивы.
# Сортировка должна быть реализована в виде функции.
# По возможности доработайте алгоритм (сделайте его умнее).
import random

def create_random_list(length_of_list):
    random_list = [0] * length_of_list
    for i in range(length_of_list):
        random_list[i] = (random.randint(-100, 99))
    return random_list

def list_bubble_sort(list_for_sort, side="rise"):
    N = len(list_for_sort)
    for i in range(N - 1):
        for j in range(N - i - 1):
            if (side == "rise") and (list_for_sort[j] > list_for_sort[j + 1]):
                list_for_sort[j], list_for_sort[j + 1] = list_for_sort[j + 1], list_for_sort[j]
            elif (side == "decline") and (list_for_sort[j] < list_for_sort[j + 1]):
                list_for_sort[j], list_for_sort[j + 1] = list_for_sort[j + 1], list_for_sort[j]
    return list_for_sort


def body():
    list_for_sort = create_random_list(100)
    print(f"Unsorted random list:\n {list_for_sort}")
    sorted_list = list_bubble_sort(list_for_sort)
    print(f"S"
          f"Sorted list:\n {sorted_list}")




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    body()