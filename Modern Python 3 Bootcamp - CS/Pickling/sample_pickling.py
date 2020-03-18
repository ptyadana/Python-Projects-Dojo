import pickle

class Animal:
	def __init__(self, name, species):
		self.name = name
		self.species = species

	def __repr__(self):
		return f"{self.name} is a {self.species}"

	def make_sound(self, sound):
		print(f"this animal says {sound}")


class Cat(Animal):
	def __init__(self, name, breed, toy):
		super().__init__(name, species="Cat") # Call init on parent class
		self.breed = breed
		self.toy = toy

	def play(self):
		print(f"{self.name} plays with {self.toy}")


conny = Cat("Conny", "Burmese Shorthair", "Yo Yo")

# pickling the object will store the object as binary, so next time you can unpickl it and continue where you left of
# pickling comes from same concept of making something last long and use it later when you need it

# To pickle an object:
# wb: write binary
with open("pets.pickle", "wb") as file:
	pickle.dump(conny, file)

# To unpickle something:
# rb: read binary
# with open("pets.pickle", "rb") as file:
# 	zombie_conny = pickle.load(file)
# 	print(zombie_conny)
# 	print(zombie_conny.play())

