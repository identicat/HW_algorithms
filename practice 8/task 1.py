capitals = {"Нидерланды": "Амстердам", "Германия": "Берлин", "Польша": "Варшава", "Австрия": "Вена", "Великобритания": "Лондон"}

for country, capital in capitals.items():
    print(country + " - " + capital)

country = input("\nВведите название страны: ")
if country in capitals.keys():
    capital = capitals.get(country)
    print(country + " - " + capital)
else:
    print("Страна не найдена")

print("\nСтраны в алфавитном порядке:")
for country in sorted(capitals):
    print(country + " - " + capitals[country])
