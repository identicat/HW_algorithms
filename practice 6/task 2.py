def div_100(number):
    try:
        res = 100 / number
        print(res)
    except TypeError:
        print("Ошибка. Некорректный ввод числа")
    except ZeroDivisionError:
        print("Ошибка. Деление на ноль")


num = input("Введите число: ")
div_100(num)