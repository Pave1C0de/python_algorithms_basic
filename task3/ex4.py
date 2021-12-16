#4. Определить, какое число в массиве встречается чаще всего.
import random

def ex4_1(list_vals):
    dict_of_unic_vals = {}
    for i in list_vals:
        if i not in dict_of_unic_vals.keys():
            dict_of_unic_vals[i] = 1
        else:
            dict_of_unic_vals[i] += 1
    max_val = max(dict_of_unic_vals.values())
    if max_val == 1:
        return None
    for k, v in dict_of_unic_vals.items():
        if v == max_val:
            return k

if __name__ == '__main__':
    list_vals = []
    for i in range(20):
        list_vals.append(random.randint(0,100))
    result = ex4_1(list_vals)
    print(list_vals)
    print(result)