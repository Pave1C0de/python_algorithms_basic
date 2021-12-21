#2. Написать программу сложения и умножения двух шестнадцатеричных чисел.
# При этом каждое число представляется как массив, элементы которого это цифры числа.
# Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
# Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
class Hex_list:
    def __init__(self, hex=[]):
        self.hex = hex
        
    def __add__(self, obj):
        self.sumax = list(hex(int("".join(self.hex), base=16) + int("".join(obj.hex), base=16))[2:])

    def __mul__(self, obj):
        self.multx =  list(hex(int("".join(self.hex), base=16) * int("".join(obj.hex), base=16))[2:])



def ex2():
    a = Hex_list(["A", "2"])
    b = Hex_list(["C", "4", "F"])
    a + b
    print(a.sumax)
    a * b
    print(a.multx)




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    ex2()