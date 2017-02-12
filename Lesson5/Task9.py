#Дано предложение. Определить, сколько в нем гласных букв

my_str = "Дано предложение. Определить, сколько в нем гласных букв"
lower_my_str = my_str.lower()
vowels = ["а", "е", "ё", "и", "о", "у", "ы", "э", "ю", "я"]
print(len(vowels))

count = 0

for i in lower_my_str:
    if i in vowels:
        count += 1
print(count)