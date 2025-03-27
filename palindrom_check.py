import re

def is_palindrome(s):
    """Проверяет, является ли строка палиндромом (игнорирует регистр, пробелы и знаки препинания)."""
    s = re.sub(r'[^a-zа-яё]', '', s.lower())  # Удаляем всё, кроме букв
    return s == s[::-1]

# Пример использования
string = input("Введите строку: ")
if is_palindrome(string):
    print(f"Строка '{string}' — палиндром!")
else:
    print(f"Строка '{string}' — не палиндром.")