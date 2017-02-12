import math

a = float(input("Введите длину a: "))
b = float(input("Введите длину b: "))
c = float(input("Введите длину c: "))

if a + b > c and a + c > b and b + c > a:
    print("Треугольник существует")
    if c == math.sqrt(a*a + b*b):
        print("Треугольник прямоугольный")
    else:
        print("Треугольник не является прямоугольным")
else:
    print("Треугольник не существует")

math.hypot()
