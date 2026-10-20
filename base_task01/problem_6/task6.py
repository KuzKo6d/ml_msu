def check(x: str, file: str) -> None:
    words = x.lower().split()

    word_counts = {}
    for word in words:
        word_counts[word] = word_counts.get(word, 0) + 1

    sorted_words = sorted(word_counts.keys())

    with open(file, 'w', encoding='utf-8') as f:
        for word in sorted_words:
            f.write(f"{word} {word_counts[word]}\n")
