def check_even_odd(number):
    """Определяет, является ли число четным или нечетным."""
    if number % 2 == 0:
        return "Четное"
    else:
        return "Нечетное"

# Пример использования функции
num = int(input("Введите число: "))
result = check_even_odd(num)
print(f"Число {num} - {result}.")