from PIL import Image, ImageFilter
import os

folder = 'imgs filter'
os.makedirs(folder, exist_ok=True)

for i in range(1, 6):
    img = Image.open(f'imgs/{i}.jpg')
    filtered_img = img.filter(ImageFilter.SHARPEN)
    filtered_img.save(os.path.join(folder, f'{i} filter.jpg'))

print("Изображения сохранены")