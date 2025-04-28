from PIL import Image

img = Image.open('img/babuleh.jpg')

img.show()

print(f"Размер изображения: {img.size}")
print(f"Формат изображения: {img.format}")
print(f"Цветовая модель изображения: {img.mode}")