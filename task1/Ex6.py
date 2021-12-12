#6. Пользователь вводит номер буквы в алфавите. Определить, какая это буква.
def ex6(letter_num):
    if (letter_num > 0) and (letter_num < 27):
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        return f"Number {letter_num} letter in alphabet is '{alphabet[letter_num-1]}'"
    else:
        return f"Error: value out of range"
if __name__ == '__main__':
    letter_num = int((input("Please insert number letter from the alphabet:")))
    result = ex6(letter_num)
    print(result)