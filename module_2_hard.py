def password(number):
    password1 = ""
    for i in range(1, number):
        for j in range(2, number):
            if j <= i:
                continue
            if number % (i + j) == 0:
                password1 += str(i) + str(j)
        return password1


text = int(input(("Введите число от 3 до 20: ")))
result = password(text)
print("Пароль", result)
