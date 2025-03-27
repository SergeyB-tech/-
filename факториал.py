def factorial_iterative(n):
    if n < 0:
        return "Факториал отрицательного числа не определён"
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Ввод числа от пользователя
number = int(input("Введите число: "))
print(f"{number}! = {factorial_iterative(number)}")