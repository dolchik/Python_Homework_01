# Задача 1: Найдите сумму цифр трехзначного числа.
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

numb = int(input('Введите трехзначное число: '))

if numb > 99 and numb < 1000:
    digit1 = int(numb / 100)
    digit2 = int(numb / 10 % 10)
    digit3 = int(numb % 10)
    result = digit1 + digit2 + digit3
    print(result)
else:
    print('Некорректное число')