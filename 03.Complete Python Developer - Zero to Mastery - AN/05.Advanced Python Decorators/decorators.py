#In python, function acts like variables and can assign like that easily

def morning():
    print("morning")

say_morning = morning()
print(say_morning)

print("--------------")


say_morning2 = morning
print(say_morning2())

print("--------------")

def hello(func):
    func()

def greet():
    print('greeting everyone!')


hello(greet)