#5. Вывести на экран коды и символы таблицы ASCII, начиная с символа под номером 32 и заканчивая 127-м включительно.
# Вывод выполнить в табличной форме: по десять пар "код-символ" в каждой строке.
def ex5(start, stop):
    st =""
    count = 1
    for i in range(start, stop+1):
        st = st + f"  {i:4} - {chr(i)}"
        if ((count%10 == 0) and (count != 0)) or i == stop:
            st += "\n"
        count += 1
    return st


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    result = ex5(32, 127)
    print(result)