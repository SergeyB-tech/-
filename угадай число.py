import random

def choose_difficulty():
    """Выбор уровня сложности"""
    print("\nВыберите уровень сложности:")
    print("1. Легкий (1-50)")
    print("2. Средний (1-100)")
    print("3. Сложный (1-200)")
    print("4. Пользовательский диапазон")
    
    while True:
        choice = input("Ваш выбор (1-4): ")
        if choice in ('1', '2', '3', '4'):
            if choice == '1':
                return 1, 50
            elif choice == '2':
                return 1, 100
            elif choice == '3':
                return 1, 200
            else:
                while True:
                    try:
                        min_num = int(input("Введите минимальное число: "))
                        max_num = int(input("Введите максимальное число: "))
                        if max_num > min_num:
                            return min_num, max_num
                        print("Максимальное число должно быть больше минимального!")
                    except ValueError:
                        print("Пожалуйста, введите целые числа!")
        else:
            print("Пожалуйста, выберите вариант от 1 до 4")

def play_game(min_num, max_num):
    """Основная логика игры"""
    secret_number = random.randint(min_num, max_num)
    attempts = 0
    
    print(f"\nЯ загадал число от {min_num} до {max_num}. Попробуй угадать!")
    
    while True:
        try:
            guess = int(input("Твоя догадка: "))
            attempts += 1
            
            if guess < secret_number:
                print("Мое число больше!")
            elif guess > secret_number:
                print("Мое число меньше!")
            else:
                print(f"\nПоздравляю! Ты угадал за {attempts} попыток!")
                return attempts
        except ValueError:
            print("Пожалуйста, введите целое число!")

def main():
    """Основная функция программы"""
    print("=== Игра 'Угадай число' ===")
    
    while True:
        min_num, max_num = choose_difficulty()
        play_game(min_num, max_num)
        
        if input("\nХочешь сыграть еще? (да/нет): ").lower() not in ('да', 'д', 'yes', 'y'):
            print("\nСпасибо за игру! До встречи!")
            break

if __name__ == "__main__":
    main()