def one(number):
    total = 0
    for i in range(number + 1):
        x = i*i
        total += x
    return total
def two(number):
    total = 0
    for i in range(number + 1):
        total += i
    total *= total
    return total
def main(number):
    x = one(number)
    y = two(number)
    y -= x
    return y
print(
    """Сумма квадратов первых десяти натуральных чисел равна

12 + 22 + ... + 102 = 385
Квадрат суммы первых десяти натуральных чисел равен

(1 + 2 + ... + 10)2 = 552 = 3025
Следовательно, разность между суммой квадратов и квадратом суммы
первых десяти натуральных чисел составляет 3025 − 385 = 2640.

Найдите разность между суммой квадратов и квадратом суммы первых X натуральных чисел.
"""
)
print(main(int(input("Введите число X: "))))