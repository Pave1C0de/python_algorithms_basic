#1. Написать программу, которая будет складывать, вычитать,
# умножать или делить два числа. Числа и знак операции вводятся пользователем.
# После выполнения вычисления программа не должна завершаться, а должна запрашивать новые данные для вычислений.
# Завершение программы должно выполняться при вводе символа '0' в качестве знака операции.
# Если пользователь вводит неверный знак (не '0', '+', '-', '*', '/'),
# то программа должна сообщать ему об ошибке и снова запрашивать знак операции.
# Также сообщать пользователю о невозможности деления на ноль, если он ввел 0 в качестве делителя.

def operations_algo(a, operation, b):
    if operation == "+":
        return int(a) + int(b)
    elif operation == "-":
        return int(a) - int(b)
    elif operation == "*":
        return int(a) * int(b)
    elif operation == "/":
        if b == "0":
            return "Error: divide by zero"
        else:
            return int(a) / int(b)
    else:
        return "Error"

def terminal_algo(a, operation, b):
    if ((operation == '+') or (operation == '-') or (operation == '*') or (operation == '/')):
        result = operations_algo(a, operation, b)
        print(f"{a}{operation}{b}={result}\n")
    elif operation == '0':
        print("Завершение работы программы")
    else:
        print(
            f"Введен не верный оператор '{operation}', попробуйте еще раз и введите что-нибудь из этого: '0', '+', '-', '*', '/'")

def ex1():
    operation = ""
    while operation != "0":
        a = int(input("Введите первый операнд:"))
        operation = input("Введите оператор:")
        b = int(input("Введите второй операнд:"))
        terminal_algo(a, operation, b)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    ex1()
