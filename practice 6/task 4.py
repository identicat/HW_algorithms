def happy(num):
    if len(num) != 6:
        return None
    half_1 = int(num[0]) + int(num[1]) + int(num[2])
    half_2 = int(num[3]) + int(num[4]) + int(num[5])
    return half_1 == half_2


ticket = input("Введите номер билета: ")
if happy(ticket) is True:
    print("Билет счастливый")
elif happy(ticket) is False:
    print("Билет не счастливый")
else:
    print("Некорректный ввод номера")