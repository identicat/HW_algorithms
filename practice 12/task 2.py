import json


with open('products.json', 'r', encoding='utf-8') as file:
    data = json.load(file)


n = int(input('Введите количество продуктов, которое вы хотите добавить: '))
for i in range(n):
    name = input("Введите название продукта: ")
    price = int(input("Введите цену: "))
    weight = int(input("Введите вес: "))
    available_input = input("В наличии? (да/нет): ").strip().lower()
    if available_input == "да":
        available = True
    else:
        available = False

    new_product = {
        "name": name,
        "price": price,
        "available": available,
        "weight": weight
    }
    data["products"].append(new_product)


with open('products.json', 'w', encoding='utf-8') as file:
    json.dump(data, file, ensure_ascii=False, indent=2)


for product in data['products']:
    print(f"\nНазвание: {product['name']}")
    print(f"Цена: {product['price']}")
    print(f"Вес: {product['weight']}")
    if product['available']:
        print("В наличии")
    else:
        print("Нет в наличии!")

