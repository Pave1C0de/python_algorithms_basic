#1. Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.
def ex1(number):
    if (number > 99) and (number < 1000):
        units = number % 10
        decs = (number % 100) // 10
        hundreds = number // 100
        sum_num_of_three_digit_number = units + decs + hundreds
        mul_num_of_three_digit_number = units * decs * hundreds
        return sum_num_of_three_digit_number, mul_num_of_three_digit_number
    else:
        return "Number in not three-digit"

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    number = int(input("please insert three-digit number:"))
    result = ex1(number)
    print(f"sum: {result[0]} \nmul: {result[1]}")