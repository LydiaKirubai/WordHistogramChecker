def word_histogram(text):
    words = text.lower().split()
    histogram = {}

    for word in words:
        word = word.strip('.,!?;:()[]"\'')
        histogram[word] = histogram.get(word, 0) + 1

    return histogram


text = "The quick brown fox jumps over the lazy dog. The dog was not amused."
hist = word_histogram(text)

for word, count in hist.items():
    print(f"{word}: {'*' * count} ({count})")
