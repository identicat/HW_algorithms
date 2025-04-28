from PIL import Image

img = Image.open('card/card.jpg')
img_cropped = img.crop((15, 260, 720, 330))
img_cropped.save('card/card text.jpg')

print("Изображение сохранено")