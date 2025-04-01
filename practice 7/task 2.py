from random import randint

mas = [randint(1,10) for i in range(10)]
fl = False
print(mas)

for i in mas:
    if mas.count(i) > 1:
        fl = True
        print(str(i)+":", mas.count(i),)
        break

if not fl:
    print("Повторов нет")