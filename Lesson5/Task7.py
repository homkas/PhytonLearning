#6.32. Дано натуральное число. Определить, сколько раз в нем встречается минимальная цифра

n = list(input("Введите любое натуральное число: "))
print(n.count(min(n)))

