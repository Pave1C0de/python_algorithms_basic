#2. Посчитать четные и нечетные цифры введенного натурального числа.
# Например, если введено число 34560, то у него 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).
def count_even_odd(natural_num):
    count_even_nums = 0
    for i in natural_num:
        if (int(i)%2 == 0):
            count_even_nums += 1
    count_odd_nums = len(natural_num) - count_even_nums
    return count_even_nums, count_odd_nums

def ex2(natural_num):
    try:
        if (int(natural_num) >= 0):
            result = count_even_odd(natural_num)
            print(f"In {natural_num:7}:\n{'even nums':10}: {result[0]}\n{'odd nums':10}: {result[1]}")
        else:
            print(f"{natural_num:10}- not natural num")
    except ValueError:
        print(f"{natural_num:10}- not natural num")

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    natural_num = input("Введите нечетные цифры введеного натурального числа:")
    ex2(natural_num)

