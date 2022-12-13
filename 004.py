# Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них.

# print(max(int(input()), int(input()), int(input()), int(input()), int(input())))

a = int(input())
maxx = a
for i in range(4):
    a = int(input())
    if a > maxx:
        maxx = a
print(f'{maxx} - максимальное число')

