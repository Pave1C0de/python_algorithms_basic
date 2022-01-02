#2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
# заданный случайными числами на промежутке [0; 50).
# Выведите на экран исходный и отсортированный массивы.
import random

def create_random_list(length_of_list):
    random_list = [0] * length_of_list
    for i in range(length_of_list):
        random_list[i] = random.uniform(0, 50)
    return random_list

def merge_sort(nums):
    if len(nums) > 1:
        mid = len(nums)//2
        left = nums[:mid]
        right = nums[mid:]
        merge_sort(left)
        merge_sort(right)

        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                nums[k] = left[i]
                i+=1
            else:
                nums[k] = right[j]
                j+=1
            k+=1

        while i < len(left):
            nums[k] = left[i]
            i+=1
            k+=1

        while j < len(right):
            nums[k] = right[j]
            j+=1
            k+=1

def body():
    # Use a breakpoint in the code line below to debug your script.
    list_for_sort = create_random_list(50)
    print(list_for_sort)

    merge_sort(list_for_sort)
    print(list_for_sort)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    body()