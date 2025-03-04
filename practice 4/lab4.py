print("Введите два из трех основных цветов: красный, синий, желтый")
color1 = input("Введите первый цвет: ")
color1 = color1.lower()
color2 = input("Введите второй цвет: ")
color2 = color2.lower()
colors = ["красный", "синий", "желтый"]
if color1 not in colors or color2 not in colors:
    print("Цвет введен неверно")
elif color1 == color2:
    print(color1)
elif (color1 == "красный" and color2 == "синий") or (color2 == "красный" and color1 == "синий"):
    print("Фиолетовый")
elif (color1 == "красный" and color2 == "желтый") or (color2 == "красный" and color1 == "желтый"):
    print("Оранжевый")
else:
    print("Зеленый")