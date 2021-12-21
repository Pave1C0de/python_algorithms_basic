#1. Пользователь вводит данные о количестве предприятий,
# их наименования и прибыль за 4 квартала (т.е. 4 отдельных числа)
# для каждого предприятия.. Программа должна определить среднюю прибыль
# (за год для всех предприятий) и вывести наименования предприятий,
# чья прибыль выше среднего и отдельно вывести наименования пред2приятий,
# чья прибыль ниже среднего.
import collections


def ex1():
    defdict = collections.defaultdict(list)
    mean_year_money_of_factoryes = 0
    factories_num = int(input(f"Введите количество предприятий:"))
    for i in range(factories_num):
        factory, first, second, third, fourth = input(f"Введите название предприятия и прибыль по кварталам:").split(" ")
        defdict[factory].append([float(first), float(second), float(third), float(fourth), (float(first)+float(second)+float(third)+float(fourth))])
        mean_year_money_of_factoryes += (float(first)+float(second)+float(third)+float(fourth))
    mean_year_money_of_factoryes = mean_year_money_of_factoryes / factories_num

    more_then_mean = list()
    less_then_mean = list()
    for key, val in defdict.items():
        if mean_year_money_of_factoryes > defdict[key][0][-1]:
            more_then_mean.append(key)
        elif mean_year_money_of_factoryes < defdict[key][0][-1]:
            less_then_mean.append(key)
    print(f"Предприятия чья прибыль больше среднего: {more_then_mean}")
    print(f"Предприятия чья прибыль меньше среднего: {less_then_mean}")

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    ex1()

#example:
#Введите количество предприятий:4
#Введите название предприятия и прибыль по кварталам:ГорСантех 100000 200000 150000 90000
#Введите название предприятия и прибыль по кварталам:Старт 40000 20000 45000 50000
#Введите название предприятия и прибыль по кварталам:Продукты 500000 400000 450000 400000
#Введите название предприятия и прибыль по кварталам:Спорт_товары 200000 150000 230000 199000
#Предприятия чья прибыль больше среднего: ['ГорСантех', 'Старт', 'Спорт_товары']
#Предприятия чья прибыль меньше среднего: ['Продукты']