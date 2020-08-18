"""
Input: string of words seperated by space
Output: string of alphabitacally sorted words
consider lower and upper case letters as the same (such as Apple and apple)
"""

def sort_words(words):
    lst = words.split(" ")
    lst.sort(key=str.lower)
    return " ".join(lst)

if __name__ == "__main__":
    result = sort_words("ORANGE banana apple")
    print(result)