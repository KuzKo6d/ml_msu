def check(x: str, file: str) -> None:
    # Переводим все слова в нижний регистр для подсчета без учета регистра
    words = x.lower().split()

    # Подсчитываем количество вхождений каждого слова
    word_counts = {}
    for word in words:
        word_counts[word] = word_counts.get(word, 0) + 1

    # Сортируем уникальные слова по алфавиту
    sorted_words = sorted(word_counts.keys())

    # Записываем результат в файл построчно
    with open(file, 'w', encoding='utf-8') as f:
        for word in sorted_words:
            f.write(f"{word} {word_counts[word]}\n")