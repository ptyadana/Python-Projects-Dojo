import random

CHOICE = ["Rock", "Paper", "Scissor"]
DRAW = 0
WIN = 1
LOSE = 2

def get_result(user_choice, computer_choice):
    if user_choice == "R" and computer_choice.startswith("P"):
        return 2
    elif user_choice == "R" and computer_choice.startswith("S"):
        return 1
    elif user_choice == "P" and computer_choice.startswith("R"):
        return 1
    elif user_choice == "P" and computer_choice.startswith("S"):
        return 2
    elif user_choice == "S" and computer_choice.startswith("R"):
        return 2
    elif user_choice == "S" and computer_choice.startswith("P"):
        return 1
    else:
        return 0

def rock_paper_scissor():
    user_wins = 0
    computer_wins = 0
    number_of_wins = 3

    print("*** Welcome to Rock Paper Scissor ***")
    print("to quit: type q")
    print("how to play - Enter r for ROCK | Paper: p | Scissor: s")
    
    while user_wins < number_of_wins and computer_wins < number_of_wins:
        computer_choice = random.choice(CHOICE)

        user_choice = input("\nEnter your choice: ").upper()

        if user_choice not in ["R", "P", "S", "Q"]:
            print("you enter invalid choice. please try again.")
            continue
        
        if user_choice == "Q":
            break

        print(f"Computer plays: {computer_choice}")
        
        result = get_result(user_choice, computer_choice)
        if result == 1:
            user_wins +=1
            print("You wins!")
        elif result == 2:
            computer_wins +=1
            print("Computer wins!")
        else:
            print("It's a draw!")
        print(f"Your Score: {user_wins} vs Computer Score: {computer_wins}")


    print("\nThanks for playing!")
    print("\n--- Final Score ---")
    print(f"Your Score: {user_wins} vs Computer Score: {computer_wins}")
    if user_wins > computer_wins:
        print("Congrats.. You win!")
    elif user_wins < computer_wins:
        print("Sorry.. Computer wins!")
    else:
        print("It's a tie!")

if __name__ == "__main__":
    rock_paper_scissor()