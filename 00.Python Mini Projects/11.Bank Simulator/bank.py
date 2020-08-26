class Account:
    def __init__(self, name, balance, min_balance):
        self.name = name
        self.balance = balance
        self.min_balance = min_balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance - amount >= self.min_balance:
            self.balance -= amount
        else:
            print("No Sufficient Funds!")

    def show_statement(self):
        print(f"Balance: $ {float(self.balance)}")



class Current(Account):
    def __init__(self, name, balance):
        super().__init__(name, balance, min_balance=-1000)

    def __str__(self):
        return f"{self.name}'s Current account is $ {self.balance}"

class Saving(Account):
    def __init__(self, name, balance):
        super().__init__(name, balance, min_balance=0)

    def __str__(self):
        return f"{self.name}'s Saving account is $ {self.balance}"


def main():
    c1 = Current("Richard", 500)
    print(c1)
    c1.deposit(100)
    c1.withdraw(50)
    c1.show_statement()
    c1.withdraw(500)
    c1.show_statement()
    c1.withdraw(100)
    c1.show_statement()

    s1 = Saving("Vivian", 1000)
    print(s1)
    s1.deposit(200)
    s1.withdraw(50)
    s1.show_statement()
    s1.withdraw(100)
    s1.show_statement()
    s1.withdraw(500)


if __name__ == "__main__":
    main()