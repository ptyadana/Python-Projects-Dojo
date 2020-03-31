#OOP
class PlayerCharacter:
    def __init__(self,name="Anonymous",age=0):
        #attributes or Class states
        self.name = name
        self.age = age

    def run(self):
        print("running")

    #classmethod can be used without instantiating the class
    #can directly call
    @classmethod
    def add(cls,num1,num2): #class, argu1, argu2
        return num1+num2

    # OR can even create a new object by directly calling this method
    @classmethod
    def multiplication(cls,num1,num2):
        return cls('Teddy',num1 * num2)

    @staticmethod
    def substraction(num1,num2):
        return num1-num2

    def __str__(self):
        return self.name

#instantitate
player1 = PlayerCharacter("Cindy",20)
player2 = PlayerCharacter("Tommy",28)
player3 = PlayerCharacter()
print(player1)
print(player2.age)
player1.attack = 50
print(player1.attack)
print(player3)

print("-----------------")
result = player1.add(1,2)
print(result)

result = PlayerCharacter.add(30,50)
print(result)

print("-----------------")
#new player got created from this class method with default name Teddy and age of (num1*num2)
player4 = PlayerCharacter.multiplication(1,5)
print(player4)
print(player4.age)

print("-----------------")
#using static method, no need to instantitate the class
result = PlayerCharacter.substraction(20,1)
print(result)