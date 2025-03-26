import re
from collections import Counter

def analyze_text(file_path):
    """
    Анализирует текстовый файл и возвращает статистику:
    - количество слов, предложений, символов
    - частоту встречаемости слов
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()
    except FileNotFoundError:
        print(f"Ошибка: файл '{file_path}' не найден.")
        return None
    except Exception as e:
        print(f"Ошибка при чтении файла: {e}")
        return None

    # Подсчет символов (включая пробелы и знаки препинания)
    char_count = len(text)
    
    # Подсчет предложений (грубое приближение по точкам, вопросительным и восклицательным знакам)
    sentences = re.split(r'[.!?]+', text)
    sentence_count = len([s for s in sentences if s.strip() != ''])
    
    # Подсчет слов (разделение по всем не-буквенным символам)
    words = re.findall(r'\b[а-яА-Яa-zA-Z]+\b', text.lower())
    word_count = len(words)
    
    # Подсчет частоты слов
    word_freq = Counter(words)
    most_common_words = word_freq.most_common(10)  # Топ-10 самых частых слов
    
    return {
        'char_count': char_count,
        'word_count': word_count,
        'sentence_count': sentence_count,
        'most_common_words': most_common_words
    }

def print_statistics(stats):
    """Выводит статистику в удобочитаемом формате"""
    if not stats:
        return
    
    print("\n=== Статистика анализа текста ===")
    print(f"Общее количество символов: {stats['char_count']}")
    print(f"Общее количество слов: {stats['word_count']}")
    print(f"Общее количество предложений: {stats['sentence_count']}")
    
    print("\nТоп-10 самых частых слов:")
    for word, count in stats['most_common_words']:
        print(f"  {word}: {count} раз")

if __name__ == "__main__":
    # Запрос пути к файлу у пользователя
    file_path = input("Введите путь к текстовому файлу: ")
    
    # Анализ файла и вывод статистики
    stats = analyze_text(file_path)
    if stats:
        print_statistics(stats)