word = input("Введите слово: ")
rare = False

for i in range(len(word)):
    if word[i].lower() == "ф":
        rare = True
        break

if rare:
    print("Ого! Это редкое слово!")
else:
    print("Эх, это не очень редкое слово...")