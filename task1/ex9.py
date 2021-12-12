#9. Вводятся три разных числа.
# Найти, какое из них является средним (больше одного, но меньше другого).
def ex9(num1, num2, num3):
    if (num1 == num2) or (num1 == num3) or (num2 == num3):
        result = "отсутствует"
    elif (num1 < num2):
        if (num2 < num3):
            result = num2
        elif (num3 < num1):
            result = num1
        else:
            result = num3
    elif (num1 > num2):
        if (num2 > num3):
            result = num2
        elif (num3 > num1):
            result = num1
        else:
            result = num3
    return f"Среднее число - {result}"


if __name__ == '__main__':
    num1 = float(input("Введите первое число:"))
    num2 = float(input("Введите второе число:"))
    num3 = float(input("Введите третье число:"))
    result = ex9(num1, num2, num3)
    print(result)