#
# Example file for working with classes
#

class Person():
  def greet(self):
    print("Hello...")

  def walk(self, direction):
    print(f"I am walking towards {direction}")

class Programmer(Person):
  def code(self, language):
    print(f"I am coding in {language}")

def main():
  person = Person()
  person.greet()
  person.walk("East")

  jack = Programmer()
  jack.greet()
  jack.walk("West")
  jack.code("python")
  
if __name__ == "__main__":
  main()
