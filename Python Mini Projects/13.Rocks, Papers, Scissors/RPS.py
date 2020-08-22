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
    
    print("*** Welcome to Rock Paper Scissor ***")
    print("to quit: type q")
    print("how to play - Enter r for ROCK | Paper: p | Scissor: s")
    
    while True:
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
            print("You wins!")
        elif result == 2:
            print("Computer wins!")
        else:
            print("It's a draw!")
        
    print("Thanks for playing!")

if __name__ == "__main__":
    rock_paper_scissor()