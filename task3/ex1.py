#1. В диапазоне натуральных чисел от 2 до 99 определить,
# сколько из них кратны каждому из чисел в диапазоне от 2 до 9.
def ex1(low_b, high_b, low_div_b, high_div_b):
    res = dict.fromkeys(range(low_b, high_b+1))
    for i in range(low_b, high_b+1):
        count = 0
        for j in range(low_div_b, high_div_b):
            if j%i == 0:
                count += 1
        res[i] = count
    return(res)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    result = ex1(2, 9, 2, 99)
    for i in range(2,9+1):
        print(f"{i} - {result[i]}")