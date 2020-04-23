# Question: Create a function that takes a text file as input and returns the number 
# of words contained in the text file. Please take into consideration that some words 
# can be separated by a comma with no space. For example "Hi,it's me." 
# would need to be counted as three words. 
# For your convenience, you can use the text file in the attachment.

# Answer: My solution
def word_count(filepath):
    with open(filepath,'r') as file:
        content = file.read()
        string_list = content.split(' ')
        return len(string_list) + content.count(',')

result = word_count('37_words2.txt')
print(result)


# Answer 1: 
def count_words(filepath):
    with open(filepath, 'r') as file:
        text = file.read()
    text = text.replace(",", " ")
    string_list = text.split(" ")
    return len(string_list)

print(count_words("37_words2.txt"))

# Explanation 1:
# This solution is like the solution of the previous exercise with the difference that before splitting we are replacing all commas with a space which will let the split method count the number of words.


# Answer 2: 
import re

def count_words_re(filepath):
    with open(filepath, 'r') as file:
        text = file.read()
    string_list = re.split(',| ',text)
    return len(string_list)

print(count_words_re("37_words2.txt"))

# Explanation 2:
# This alternative solution uses the built-in re  module which provides regular expression matching operations. We're using the split method of that module and the expression ",| " is meant to replace commas with spaces. Using methods from the re  module can be more appropriate than Python built-in methods when string operations are complicated. However, for this simple scenario the re  module could be skipped.
