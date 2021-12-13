#3. Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
# Например, если введено число 3486, то надо вывести число 6843.

def ex3(num):
    if num[0] == "-":
        num = float(num[:0:-1])*(-1)
    else:
        num = float(num[::-1])
    return num


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    num = input("Введите число")
    result = ex3(num)
    print(result)