print('Для завершения игры введите "stop"')
s = ""

while True:
    word = input("Введите слово: ")
    if word.lower() == "stop":
        break
    s = s + word + " "

s = s.rstrip()
print(s)