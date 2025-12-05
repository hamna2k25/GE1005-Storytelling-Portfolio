def count_words(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        text = f.read().lower()
    words = text.split()
    freq = {}
    for w in words:
        freq[w] = freq.get(w, 0) + 1
    return freq

if __name__ == "__main__":
    file = "Stories/Story1.md"
    frequencies = count_words(file)
    print("Word Frequency in your story:\n")
    for word, count in frequencies.items():
        print(f"{word}: {count}")
