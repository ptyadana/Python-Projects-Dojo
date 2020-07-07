print('***** Welcome to pig Latin *****')

while True:
    #get sentence
    sentence = input('\nPlease enter a sentence (q: quit): ')
    
    if sentence.strip().lower() == 'q':
        break

    #split into words
    words = sentence.lower().split()
    
    new_words = []

    #loop them and convert them into pig latin
    for word in words:
        if word[0] in 'aeiou':
                new_word = word + 'yay'
                new_words.append(new_word)
        else:
            vowel_index = 0

            for letter in word:
                if letter not in 'aeiou':
                    vowel_index += 1
                else:
                    break

            consonant_part = word[:vowel_index]
            rest_part = word[vowel_index:]
            new_word = rest_part + consonant_part + 'ay'
            new_words.append(new_word)
    

    print(new_words)
    #combine the words back to sentence
    result = " ".join(new_words)

    #display back to user
    print(f"\n {result}")