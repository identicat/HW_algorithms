class Restaurant():
    def __init__(self, restaurant_name, cuisine_type, rating=1.0):
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


class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type, rating, location, open_hours):
        super().__init__(restaurant_name, cuisine_type, rating)
        self.flavors_by_type = {"в стаканчике": ["пломбир", "шоколад"],
                                "на палочке": ["ваниль", "шоколад"],
                                "мягкое": ["пломбир", "клубника"]}
        self.location = location
        self.open_hours = open_hours

    def all_flavors(self):
        if not self.flavors_by_type:
            print("Нет доступных вкусов")
        else:
            print("Доступное мороженое:")
            for type, flavors in self.flavors_by_type.items():
                if flavors:
                    print(f"{type}: {', '.join(flavors)}")

    def add_flavor(self):
        type = input("Введите тип мороженого: ").lower()
        flavor = input("Введите вкус мороженого: ").lower()
        if type in self.flavors_by_type:
            if flavor not in self.flavors_by_type[type]:
                self.flavors_by_type[type].append(flavor)
            else:
                print("Такой вкус уже есть")
        else:
            self.flavors_by_type[type] = [flavor]
        print("Вкус добавлен")

    def del_flavor(self):
        type = input("Введите тип мороженого: ").lower()
        flavor = input("Введите вкус мороженого: ").lower()
        if type in self.flavors_by_type:
            if flavor in self.flavors_by_type[type]:
                self.flavors_by_type[type].remove(flavor)
                print("Вкус удален")
        else:
            print(f"Вкус не найден")

    def del_type(self):
        type = input("Введите тип мороженого: ").lower()
        if type in self.flavors_by_type:
            del self.flavors_by_type[type]
            print("Тип удален")
        else:
            print("Тип не найден")

    def check_flavor(self):
        type = input("Введите тип мороженого: ").lower()
        flavor = input("Введите вкус мороженого: ").lower()
        if type in self.flavors_by_type:
            if flavor in self.flavors_by_type[type]:
                print("Мороженое в наличии")
        else:
            print("Мороженого нет в наличии")


NewIceCreamStand = IceCreamStand("Scoops Ahoy", "Мороженое", 4.2, "Hawkins", "9:00 - 20:00")
NewIceCreamStand.all_flavors()




