seat = int(input("Введите номер места в плацкартном вагоне: "))
if 37 <= seat <= 54:
    if seat % 2 == 0:
        print("Боковое, верхнее")
    else:
        print("Боковое, нижнее")
elif 1 <= seat <= 36:
    if seat % 2 == 0:
        print("В купе, верхнее")
    else:
        print("В купе, нижнее")
else:
    print("Места с таким номером нет")