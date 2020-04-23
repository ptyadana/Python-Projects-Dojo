# Question: Create an English to Portuguese translation program.

# The program takes a word from the user as input and translates it using the following dictionary 
# as a vocabulary source.

d = dict(weather = "clima", earth = "terra", rain = "chuva") 

# Expected output: 
# Enter word: earth
# terra

# Answer:
def vocab(word):
    return d[word]
    
try:
    user_input = input('Enter word: ')
    print(vocab(user_input))
except:
    print('Invalid input. Please use avaliable words only.')

# Explanation:
# It's good to create a function as the above code shows so that the code is more organized in case you need to expand it and add more features later. 
# The function simply gets the word string from the input  function, queries the dictionary and prints out the result. Of course we are forced to use only the words we have in the dictionary. If you want to make this a more real life translator you would need a complete dictionary and you would also want to store it in a file instead of keeping it inside the script. 