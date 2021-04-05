import math

print("Введите цифру (круг-1,прямоугольник-2,трапеция-3,треугольник-4):")
a = int(input())

sqrt = 0
perim = 0

if a == 1:
    print("Введите радиус:")
    r = int(input())

    sqrt = math.pi * r ** 2
    perim = 2 * math.pi * r
elif a == 2:
    h = int(input("Введите высоту:"))
    l = int(input("Введите длину:"))

    sqrt = h*l
    perim = (h+l)*2
elif a == 3:
    h = int(input("Введите высоту:"))
    a = int(input("Введите длину верхнего основания:"))
    b = int(input("Введите длину нижнего основания:"))

    sqrt = ((a+b)/2)*h
    perim = h + a + b + math.sqrt(a**2 + (b-a)**2)
elif a == 4:
    h = int(input("Введите высоту:"))
    a = int(input("Введите длину основания:"))

    sqrt = (a*h)/2
    perim = a + 2 * math.sqrt((a/2)**2 + (h/2)**2)


print("Площадь: %d" % sqrt)
print("Периметр: %d" % perim)
