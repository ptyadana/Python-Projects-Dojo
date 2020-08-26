def is_question(words):
    questions = ("what","why","how","when","who","which", "whose","where", "is", "are", "do", "did", "does")
    if words.lower().startswith(questions):
        return True
    return False

    # Alternative way
    # questions = ["what","why","how","when","who","which", "whose","where", "is", "are", "do", "did", "does"]
    # first_word = words.split()[0]
    # if first_word.lower() in questions:
    #     return True
    # return False
    


def process_words(word_list):
    processed_list = []

    if word_list:
        for sentence in word_list:
            new_sentence = sentence.capitalize()
            if is_question(new_sentence):
                new_sentence += "?"
            else:
                new_sentence += "."
            processed_list.append(new_sentence)

    else:
        print("Oh..seem like you have nothing to say today!")

    return " ".join(processed_list)

def main():
    print("**** Welcome to Memo *****")
    result_list = []

    while True:
        user_input = input("Say something: ").strip()

        if user_input == 'yipeeyaee':
            break
        
        if user_input:
            result_list.append(user_input)

    processed_sentence = process_words(result_list)
    print("\n" + processed_sentence)


if __name__ == "__main__":
    main()