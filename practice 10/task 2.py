from PIL import Image

cards = {
    'Новый год': 'new year.jpg',
    'День рождения': 'birthday.jpg',
    'День кошек': 'cat.jpg'
}

holiday = input("Введите название праздника из списка:\nНовый год\nДень рождения\nДень кошек\n")

if holiday in cards:
    img = Image.open(f'cards/{cards[holiday]}')
    img.show()
else:
    print("Такой открытки нет")