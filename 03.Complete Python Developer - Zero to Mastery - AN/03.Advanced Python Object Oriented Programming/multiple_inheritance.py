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

    def check_arrows(self):
        print(f"attacking with arrows. arrows left: {self.arrows}")

    def run(self):
        print("run really really fast.")

class HybridBorg(Wizard, Archer):
    def __init__(self, name, power, arrows):
        Wizard.__init__(self, name, power)
        Archer.__init__(self, name, arrows)

hb1 = HybridBorg("hb1", 50, 200)
hb1.sign_in()
print(hb1.power)
hb1.attack()
hb1.check_arrows()
hb1.run()