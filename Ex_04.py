# Задача 4: Требуется определить, можно ли от шоколадки размером n × m 
# долек отломить k долек, если разрешается сделать один разлом 
# по прямой между дольками (то есть разломить шоколадку на два прямоугольника).
n = int(input('Введите количество долек по длине шоколадки:'))
m = int(input('Введите количество долек по ширине шоколадки: '))
k = int(input('Введите сколько долек вы хотите отломить: '))

if k < m * n and (k % m == 0 or k % n == 0):
    print('Да, столько долек отломить можно')
else:
    print('Нет, так нельзя отломить')