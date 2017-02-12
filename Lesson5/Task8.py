n = list(range(31, 100))
m = [2, 4, 8]


summa = 0
for i in n:
    if i%3 == 0 and i%10 in m:
        summa += i
print(summa)


print(str(m[0].__add__(-2)))

