from random import randint

mas = [randint(1, 10) for i in range(5)]
number = int(input("Введите число от 1 до 10: "))
print("Исходный список:", mas)
print("Ваше число:", number)

if number in mas:
    print("Поздравляю, Вы угадали число!")
else:
    print("Нет такого числа!")