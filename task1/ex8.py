#8. Определить, является ли год, который ввел пользователем,
# високосным или невисокосным.
def ex8(year):
    if year > 0:
        if (year % 4 == 0) and (year % 100 != 0):
            result = "является"
        else:
            result = "не является"
        return(f"Год {year} - {result} високосным")
    else:
        return (f"Error: год {year} - какой-то странный!")

if __name__ == '__main__':
    year = int((input("Введите год:")))
    result = ex8(year)
    print(result)