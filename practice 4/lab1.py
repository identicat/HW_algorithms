pass1 = input("Введите пароль: ")
if len(pass1) < 8:
    pass1 = input("Пароль должен содержать не менее 8 символов: ")
pass2 = input("Повторите пароль: ")
if pass1 == pass2:
    print("Пароль принят")
else:
    print("Пароль не принят")