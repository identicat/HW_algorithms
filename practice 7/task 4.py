from random import randint

team = ()
my_group = ["Абраменко", "Бурдейная", "Гиносян", "Григорьева", "Гафуров",
            "Добров", "Ершов", "Закарейшвили", "Кюлян", "Капкайкина"]
other_group = ["Смирнов", "Иванов", "Петров", "Сидоров", "Васильев",
               "Михайлов", "Фёдоров", "Кузнецов", "Никитин", "Орлов"]

print("Моя группа:", ", ".join(my_group))
print("Другая группа:", ", ".join(other_group))

for i in range(5):
    index = randint(0, len(my_group)-1)
    team += (my_group.pop(index),)

for i in range(5):
    index = randint(0, len(other_group)-1)
    team += (other_group.pop(index),)

sorted_team = tuple(sorted(team))

print("Команда:", ", ".join(team))
print("Количество участников команды:", len(team))
print("Отсортированная команда:", ", ".join(sorted_team))

if "Иванов" in team:
    print("Студент Иванов входит в команду")
    print("Фамилия встречается", team.count("Иванов"), "раз")
else:
    print("Студент Иванов не входит в команду")

