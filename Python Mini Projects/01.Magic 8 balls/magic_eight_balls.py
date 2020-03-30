import random
import configparser


def main():
    user_answer = 'Y'

    print("******* Welcome to Magic 8 Balls *******")

    while user_answer == 'Y':

        question = input("What would you like to know? please ask me your question.\n")

        if question == "":
            print("Seem like you have nothing to ask. Good bye!")
            user_answer = "N"
        else:
            answer_number = random.randint(1,20)

            answer = get_answer(answer_number)
            print(answer)

            #ask user to whether he/she likes to answer more question.
            user_answer = input("Would you like to ask again? (Y/N) : ")

#function to get answer
def get_answer(answer_number):
    
    #load the properties file
    config = configparser.RawConfigParser()
    config.read('answers.properties')

    """give the magic 8 balls answers """
    if answer_number == 1:
            answer = config.get('AnswersSection','answer1')
    elif answer_number == 2:
        answer = config.get('AnswersSection','answer2')
    elif answer_number == 3:
        answer = config.get('AnswersSection','answer3')
    elif answer_number == 4:
        answer = config.get('AnswersSection','answer4')
    elif answer_number == 5:
        answer = config.get('AnswersSection','answer5')
    elif answer_number == 6:
        answer = config.get('AnswersSection','answer6')
    elif answer_number == 7:
        answer = config.get('AnswersSection','answer7')
    elif answer_number == 8:
        answer = config.get('AnswersSection','answer8')
    elif answer_number == 9:
        answer = config.get('AnswersSection','answer9')
    elif answer_number == 10:
        answer = config.get('AnswersSection','answer10')
    elif answer_number == 11:
        answer = config.get('AnswersSection','answer11')
    elif answer_number == 12:
        answer = config.get('AnswersSection','answer12')
    elif answer_number == 13:
        answer = config.get('AnswersSection','answer13')
    elif answer_number == 14:
        answer = config.get('AnswersSection','answer14')
    elif answer_number == 15:
        answer = config.get('AnswersSection','answer15')
    elif answer_number == 16:
        answer = config.get('AnswersSection','answer16')
    elif answer_number == 17:
        answer = config.get('AnswersSection','answer17')
    elif answer_number == 18:
        answer = config.get('AnswersSection','answer18')
    elif answer_number == 19:
        answer = config.get('AnswersSection','answer19')  
    else:
        answer = config.get('AnswersSection','answer20')

    return answer

#main
if __name__ == "__main__":
    main()