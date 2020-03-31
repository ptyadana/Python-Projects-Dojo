class User():
    def sign_in(self):
        print("logged in.")

class Wizard(User):

    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        print(f"attacking with the power of {self.power}")

class Archer(User):
    def __init__(self, name, arrows):
        self.name = name
        self.arrows = arrows

    def attack(self):
        print(f"attacking with arrows. arrows leff: {self.arrows}")


wizard1 = Wizard("Merlin",50)
wizard1.sign_in()
wizard1.attack()

archer1 = Archer("Robin", 200)
archer1.sign_in()
archer1.attack()

print("------------")
#isinstance
print(isinstance(wizard1,Wizard))
print(isinstance(wizard1,User))
print(isinstance(wizard1,object))