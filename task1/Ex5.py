#5. Пользователь вводит две буквы.
# Определить, на каких местах алфавита они стоят и сколько между ними находится букв.
import random
def ex5(num_letter_1, num_letter_2):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    if (num_letter_1 in alphabet) and (num_letter_2 in alphabet):
        if num_letter_1 != num_letter_2:
            return (f"Num first letter '{num_letter_1}' is {alphabet.index(num_letter_1)+1}.\nNum second letter '{num_letter_2}' is {alphabet.index(num_letter_2)+1}.\nNum's between letters is { abs((alphabet.index(num_letter_1) - alphabet.index(num_letter_2)))-1}")
        else:
            return (f"Num first letter '{num_letter_1}' is {alphabet.index(num_letter_1)+1}.\nNum second letter '{num_letter_2}' is {alphabet.index(num_letter_2)+1}.\nNum's between letters is {0}")
    else:
        return "Error: wrong input"
    
if __name__ == '__main__':
    num_letter_1 = str((input("Please insert 1st letter of the alphabet:")))
    num_letter_2 = str((input("Please insert 2nd letter of the alphabet:")))
    result = ex5(num_letter_1, num_letter_2)
    print(result)