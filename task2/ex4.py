#4. Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
# Количество элементов (n) вводится с клавиатуры.
def ex4(num, count, sum):
    while count > 0:
        count -= 1
        sum = sum + num
        print(f"{num:>20} : {sum:>20}")
        if count == 0:
            return sum
        return ex4(-num/2, count, sum)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    start_val = 1
    num = int(input("Введите количество элеменьов последовательности:"))
    ret = ex4(start_val, num, 0)
    print(ret)