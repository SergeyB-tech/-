# Генератор паролей
Наша задача — разработать программу, которая будет генерировать случайные пароли на основе заданных пользователем параметров.
Программа должна быть простой в использовании и предоставлять пользователю возможность настраивать следующие параметры:


  # 1.	Длина пароля:
  пользователь должен иметь возможность выбрать длину генерируемого пароля.
  
  # 2.	Типы символов: 
  программа должна позволять пользователю выбирать, какие символы использовать для генерации пароля:
  
o	Заглавные буквы (A-Z)

o	Строчные буквы (a-z)

o	Цифры (0-9)

o	Специальные символы (!@#$%^&*)

# Функциональные требования:

●	Генерация пароля: реализовать функцию, которая будет генерировать пароль на основе выбранных параметров.

●	Интерфейс: создать простой текстовый интерфейс, который позволит пользователю вводить параметры генерации и получать сгенерированный пароль.

●	Валидация ввода: обеспечить проверку правильности введённых данных (например, длина пароля должна быть положительным целым числом).

# Технические требования:

●	Программа должна быть написана на Python.

●	Используйте стандартные библиотеки для генерации случайных чисел и работы с символами.

●	Структура кода должна быть ясной и понятной, с использованием функций для основных логических блоков.

# Игра угадай число

```Особенности реализации:```

```Основные требования:```

Компьютер загадывает случайное число (используется random.randint())

Пользователь вводит догадки через консоль

Программа подсказывает "больше/меньше"

Ведется счетчик попыток

При угадывании выводится поздравление с количеством попыток

```Дополнительные функции:```

Выбор уровня сложности (легкий 1-50, средний 1-100, сложный 1-200)

Пользовательский диапазон - можно задать любые числа

Повторная игра - после завершения можно сыграть еще раз без перезапуска программы

Обработка ошибок - защита от неверного ввода чисел

```Улучшения:```

Четкое разделение кода на функции

Поддержка русского и английского ввода (да/нет)

Информативные сообщения для пользователя

Проверка корректности вводимых данных

```Как играть:```

1.Запустите программу

2.Выберите уровень сложности

3.Вводите числа, получайте подсказки

4.Когда угадаете - получите статистику

5.По желанию сыграйте еще раз

Программа работает в любой среде с Python 3 и использует только стандартные библиотеки.
