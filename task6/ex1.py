#1. Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.
import sys
def ex1(number):                                                                #int - (28 bytes)
    if (number > 99) and (number < 1000):
        units = number % 10                                                     #int - (28 bytes)
        decs = (number % 100) // 10                                             #int - (28 bytes)
        hundreds = number // 100                                                #int - (28 bytes)
        sum_num_of_three_digit_number = units + decs + hundreds                 #int - (28 bytes)
        mul_num_of_three_digit_number = units * decs * hundreds                 #int - (28 bytes)
        #print(sys.getsizeof(number) + sys.getsizeof(units) + sys.getsizeof(decs) + sys.getsizeof(hundreds) + sys.getsizeof(sum_num_of_three_digit_number) + sys.getsizeof(mul_num_of_three_digit_number) + sys.getsizeof("Number in not three-digit"))

        return sum_num_of_three_digit_number, mul_num_of_three_digit_number
    else:
        return "Number in not three-digit"                                      # (37 + str_len) bytes
                                                                                #-----------------------------
                                                                                #242 bytes (OS Win 64) python version 3.9.1
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    number = int(input("please insert three-digit number:"))
    result = ex1(number)
    print(f"sum: {result[0]} \nmul: {result[1]}")