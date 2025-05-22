class Restaurant():
    def __init__(self, restaurant_name, cuisine_type, rating=1):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.rating = rating

    def describe_restaurant(self):
        print(f"Название ресторана: {self.restaurant_name}")
        print(f"Тип кухни: {self.cuisine_type}")

    def open_restaurant(self):
        print(f"Ресторан {self.restaurant_name} открыт!")

    def update_rating(self, new_rating):
        self.rating = new_rating
        print(f"Рейтинг ресторана {self.restaurant_name} обновлен: {self.rating}")


newRestaurant1 = Restaurant("Tetto", "Итальянская")
newRestaurant2 = Restaurant("Пхали Хинкали", "Грузинская")
newRestaurant3 = Restaurant("Ukusno", "Сербская")

print(newRestaurant1.restaurant_name)
print(newRestaurant1.cuisine_type)

newRestaurant1.describe_restaurant()
newRestaurant1.open_restaurant()

newRestaurant2.describe_restaurant()
newRestaurant3.describe_restaurant()

newRestaurant1.update_rating(4.4)

