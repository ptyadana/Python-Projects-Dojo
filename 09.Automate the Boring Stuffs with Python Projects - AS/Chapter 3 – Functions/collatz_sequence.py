def collatz(number):
    if number % 2 == 0:
        return number // 2
    else: 
        return 3 * number + 1

def main():
        try:
            number = int(input("Enter number:\n"))
            while number != 1:
                number = collatz(number)
                print(number)

        except Exception:
            print("You didn't provide the valid number!")

if __name__ == "__main__":
    main()