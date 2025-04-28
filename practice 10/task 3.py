from PIL import Image, ImageDraw, ImageFont

cards = {
    'Новый год': {
        'image': 'cards/new year.jpg',
        'text': '{name}, поздравляю!',
        'size': 50,
        'position': (200, 180),
        'text_color': 'white',
    },
    'День рождения': {
        'image': 'cards/birthday.jpg',
        'text': '{name}, поздравляю!',
        'size': 50,
        'position': (250, 15),
        'text_color': '#800000',
    },
    'День кошек': {
        'image': 'cards/cat.jpg',
        'text': '{name},  поздравляю!',
        'size': 70,
        'position': (400, 170),
        'text_color': 'black',
    }
}


def add_text_to_card(card_name, person):
    if card_name not in cards.keys():
        print("Такой карточки нет")
        return

    card = cards.get(card_name)
    img = Image.open(card['image'])
    draw = ImageDraw.Draw(img)

    font = ImageFont.truetype('Arial Bold.ttf', card['size'])
    text = card['text'].format(name=person)
    draw.text(card['position'], text, font=font, fill=card['text_color'])

    img.save(f"cards/{card_name} {text}.jpg")
    print('Открытка сохранена')


card_name = input("Введите название праздника из списка:\nНовый год\nДень рождения\nДень кошек\n")
person_name = input("Введите имя получателя: ")

add_text_to_card(card_name, person_name)