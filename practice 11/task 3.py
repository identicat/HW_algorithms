import csv

sum = 0
products = []

with open('products.csv', encoding='cp1251') as file:
    reader = csv.DictReader(file)
    for row in reader:
        product = row['Продукт']
        k = int(row['Количество'])
        price = int(row['Цена'])
        sum += k * price
        products.append(f'{product} - {k} шт. за {price} руб.')

print('Нужно купить:')
for i in products:
    print(i)
print(f'Итоговая сумма: {sum} руб.')
