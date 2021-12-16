#3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
import random
def ex3():
    rand_arr = list()
    for i in range(100):
        rand_arr.append(random.randint(0, 100))
    print(rand_arr)

    min_index = rand_arr.index(min(rand_arr))
    max_index = rand_arr.index(max(rand_arr))

    buff = rand_arr[min_index]
    rand_arr[min_index] = rand_arr[max_index]
    rand_arr[max_index] = buff
    print(rand_arr)
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    result = ex3()