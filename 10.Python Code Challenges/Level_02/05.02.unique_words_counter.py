import re
from collections import Counter


def unique_words_counter(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        all_words = re.findall(r"[0-9a-zA-Z-']+", file.read())
        all_words = [word.upper() for word in all_words]
        print("Total Words: ", len(all_words))

        words_counter = Counter()
        for word in all_words:
            words_counter[word] += 1

        print("\nTop 20 words:")
        for word in words_counter.most_common(20):
            value, count = word
            print(value, " : ", count)


if __name__ == "__main__":
    unique_words_counter("data/shakespeare.txt")
