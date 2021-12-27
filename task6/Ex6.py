#6. Пользователь вводит номер буквы в алфавите. Определить, какая это буква.
def ex6(letter_num):                                                                    #28 bytes
    if (letter_num > 0) and (letter_num < 27):
        alphabet = "abcdefghijklmnopqrstuvwxyz"                                         #37 + 26 bytes
        return f"Number {letter_num} letter in alphabet is '{alphabet[letter_num-1]}'"  #34 bytes
                                                                                        #----------------
                                                                                        # 125 bytes (OS Win 64) python version 3.9.1
    else:
        return f"Error: value out of range"
if __name__ == '__main__':
    letter_num = int((input("Please insert number letter from the alphabet:")))
    result = ex6(letter_num)
    print(result)