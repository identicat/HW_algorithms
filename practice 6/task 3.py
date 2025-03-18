from datetime import datetime


def magical(date_str):
    try:
        date = datetime.strptime(date_str, "%d.%m.%Y")
    except ValueError:
        return None

    day = date.day
    month = date.month
    year = date.year % 100

    return day * month == year


date_str = input("Введите дату в формате ДД.ММ.ГГГГ: ")
if magical(date_str) is True:
    print("Дата магическая")
elif magical(date_str) is False:
    print("Дата не магическая")
else:
    print("Некорректный ввод даты")