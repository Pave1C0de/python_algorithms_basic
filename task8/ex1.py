
#1. Определение количества различных подстрок с использованием хэш-функции.
# Пусть дана строка S длиной N, состоящая только из маленьких латинских букв.
# Требуется найти количество различных подстрок в этой строке.
def ex1(string):
    # Use a breakpoint in the code line below to debug your script.
    my_dict = {}
    for i in range(len(string)):
        for j in range(len(string[i:])+1):
            if ((j !=0)):
                my_hash = hash(string[i:(i+j)])
                #print(f'{i} {i+j} {string[i:(i+j)]} -- {my_hash}')  # Press Ctrl+F8 to toggle the breakpoint.
                if my_dict.get(my_hash) == None:
                    my_dict[my_hash] = string[i:(i+j)]
    #print(my_dict)
    return len(my_dict)
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    res = ex1("aba")
    print(res)