# Question: Create a function that takes any string as input and returns the number of words for that string.

def words_count(st):
    string_list = st.split(' ')
    return len(string_list)

if __name__ == "__main__":
    result = words_count('I am super awesome')
    print(result)

# Explanation:
# We're using split  here which is a string method that splits a string into several strings given a separator passed inside the brackets. When you don't pass a separator, split  will split a string at white spaces. This will output a list of strings..Applying len  to that list returns the number of list items, so the number of words.