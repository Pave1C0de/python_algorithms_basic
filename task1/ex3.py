#3. По введенным пользователем координатам двух точек вывести уравнение прямой вида y=kx+b,
# проходящей через эти точки.
def ex3(x1, y1, x2, y2):
    if (x1 == x2) and (y1 == y2):
        return f"невозможно провисти однозначно линию по одной точке ({x1}, {y1})"
    else:
        k = (y2 - y1) / (x2 - x1)
        b = -( (y2 - y1) / (x2 - x1) ) * x1 + y1
        if b>=0:
            return(f"Уравнение прямой по двум координатам a({x1},{y1}) и b({x2},{y2}): y = {round(k, 2)}x + {round(b, 2)}")
        else:
            return(f"Уравнение прямой по двум координатам a({x1},{y1}) и b({x2},{y2}): y = {round(k, 2)}x - {round(abs(b), 2)}")

    second_cdt = int(input("Please insert first coordinate:"))
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    x1 = int(input("Please insert x1  coordinate of {x1, y1}:"))
    y1 = int(input("Please insert y1  coordinate of {x1, y1}:"))
    x2 = "{0:.2f}".format(float(input("Please insert x2  coordinate of {x2, y2}:")))
    y2 = float(input("Please insert y2  coordinate of {x2, y2}:"))
    result = ex3(x1, y1, x2, y2)
    print(result)