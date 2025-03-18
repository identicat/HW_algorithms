def isdiv_3(number):
    return number % 3 == 0


num = int(input("Введите число: "))
if isdiv_3(num):
    print("Число делится на 3")
else:
    print("Число не делится на 3")