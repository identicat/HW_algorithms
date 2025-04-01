letters = {"АВЕИНОРСТ": 1, "ДКЛМПУ": 2, "БГЁЬЯ": 3, "ЙЫ": 4, "ЖЗХЦЧ": 5, "ШЭЮ": 8, "ФЩЪ": 10}

word = input("Введите слово: ").upper()
score = 0
for letter in word:
    for key in letters:
        if letter in key:
            score += letters[key]
            break

print("Стоимость слова:", score)