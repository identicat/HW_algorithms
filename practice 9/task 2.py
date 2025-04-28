from PIL import Image, ImageOps

img = Image.open('img/babuleh.jpg')

img_small = img.resize((img.width // 3, img.height // 3))
img_small.save('img/babuleh small.jpg')

mirror_hor = ImageOps.mirror(img)
mirror_hor.save('img/babuleh mirror horizontal.jpg')

mirror_vert = ImageOps.flip(img)
mirror_vert.save('img/babuleh mirror vertical.jpg')

print("Изображения сохранены")