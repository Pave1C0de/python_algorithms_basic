#4. Написать программу, которая генерирует в указанных пользователем границах:
#случайное целое число;
#случайное вещественное число;
#случайный символ.
#Для каждого из трех случаев пользователь задает свои границы диапазона.
# Например, если надо получить случайный символ от 'a' до 'f', то вводятся эти символы.
# Программа должна вывести на экран любой символ алфавита от 'a' до 'f' включительно.
import random
def ex4(low, height):
    try:
        low = int(low)
        height = int(height)
        if low < height:
            return (f"Random int number: {random.randint(low, height)}")
        else:
            return "wrong border"
    except:
        try:
            low = float(low)
            height = float(height)
            if low < height:
                return (f'Random float value: {random.uniform(low, height)}')
            else:
                return "wrong border"

        except:
            try:
                f = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!#$%&'()*+,-./:;<=>?@[\]^_`{|}~"
                low = str(low)
                height = str(height)
                if f.index(low) < f.index(height):
                    return (f"Random alphabet sign: {random.choice(f[f.index(low):f.index(height)])}")
                else:
                    return "wrong border"

            except:
                return "Wrong type input date"



if __name__ == '__main__':
    low = (input("Please insert lower bound of the range (str):"))
    height = (input("Please insert height bound of the range (str):"))
    result = ex4(low, height)
    print(result)