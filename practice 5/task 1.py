n = int(input("Введите количество слов: "))
s = ""

for i in range(n):
    word = input("Введите слово: ")
    s = s + word + " "

s = s.rstrip()
print(s)