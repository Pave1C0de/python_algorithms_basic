#6. В программе генерируется случайное целое число от 0 до 100.
# Пользователь должен его отгадать не более чем за 10 попыток.
# После каждой неудачной попытки должно сообщаться больше или меньше введенное пользователем число,
# чем то, что загадано. Если за 10 попыток число не отгадано, то вывести загаданное число.
import random
def ex6(guessing_val, val, i):
    if guessing_val < val:
        return f"Число {guessing_val} меньше загаданного числа, осталось {i} попыток"
    elif guessing_val > val:
        return f"Число {guessing_val} больше загаданного числа, осталось {i} попыток"
    else:
        return f"Вы угадали загаданное число {guessing_val} с {10-i} попыти, поздравляю!"

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    low_border  = 0
    high_border = 100
    try_num = 10
    val = random.randint(low_border, high_border)
    print(val)
    for i in range(try_num - 1, -1, -1):
        guessing_val = int(input(f"Угадайте число от {low_border} до {high_border}, у вас {i+1} попыток"))
        result = (ex6(guessing_val, val, i))
        print(result)
        if "Вы угадали загаданное число" in  result:
            break
        if i == 0:
            print("Попытки закончились! ")
            break