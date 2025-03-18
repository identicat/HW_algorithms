from random import randint

correct = 0
mistake = 0

while correct < 3 and mistake < 3:
    a = randint(1, 10)
    b = randint(1, 10)
    expr = str(a) + " + " + str(b) + " = "
    res_user = input(str(a) + " + " + str(b) + " = ")
    if res_user.isdigit() and int(res_user) == a + b:
        print("Правильно!")
        correct += 1
    else:
        print("Ответ неверный")
        mistake += 1

print("Игра окончена. Правильных ответов: " + str(correct))