from PIL import Image

img = Image.open('img/babuleh.jpg')
watermark = Image.open('watermark.png')

watermark = watermark.resize((260, 120))
img.paste(watermark, (195, 150), watermark)

img.save('img/babuleh watermark.jpg')

print("Изображение сохранено")