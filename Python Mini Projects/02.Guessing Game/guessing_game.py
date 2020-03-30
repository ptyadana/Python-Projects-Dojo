import random

def main():
    print("***** Welcome to Guessing Game *****")
    
    generated_number = random.randint(1,20)
    continue_game = "Y"
    count = 0
    
    try:
        while continue_game == "Y":

            result = ""
            while("Correct" not in result):
                user_number = input("\nEnter an integer between 1 and 20 : ")
                count+=1

                if user_number != "":
                    result = check_guess(int(user_number), generated_number, count)
                    print(result)            

            continue_game = input("Would you like to play another game? (Y/N)")

    except Exception:
        print("You have provided invalid input. The game will quit now !")

def check_guess(user_number,generated_number,count):
    """ check user guess number against with genrated number """
    if(user_number == generated_number):
        return f"Great Job! The Correct number is {generated_number}. You have made {count} guesses.\n"
    elif(user_number > generated_number):
        return "The number you guessed was too high.\n"
    else:
        return "The number you guessed was too low.\n"

if __name__ == "__main__":
    main()