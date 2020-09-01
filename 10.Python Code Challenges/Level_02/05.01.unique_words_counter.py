"""
Count the number of unique words and how often each occurs
Input: path to text file
Output: total number of words in the file, top 20 most frequent words   
"""

import re


def unique_words_counter(file_path):

    unique_dict = {}
    with open(file_path, "r", encoding="utf-8") as file:

        all_words = re.findall(r"[0-9a-zA-Z-']+", file.read())
        all_words = [word.upper() for word in all_words]

        for word in all_words:
            count = unique_dict.get(word, 0) + 1
            unique_dict[word] = count

    # sort the dict
    sorted_words = sorted(
        unique_dict.items(), key=lambda item: item[1], reverse=True)

    print("\nTotal Words: ", len(all_words))
    print(f"Total Unique Words: {len(unique_dict)}")
    print("Top 20 words: ")

    for i in range(20):
        word, count = sorted_words[i]
        print(f"{word} : {count}")


if __name__ == "__main__":
    file_path = "data/shakespeare.txt"
    unique_words_counter(file_path)
