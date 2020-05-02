class Person():
    def __init__(self, name):
        self.name = name

    def say_hello(self):
        print(f'I am Hello {self.name}')


class Student(Person):
    def __init__(self, name, school):
        super().__init__(name)
        self.school = school

    def sing_school_song(self):
        print(f'Ode to {self.school}')

    def say_hello(self):
        super().say_hello()
        print('and I am a student too.')

    def __str__(self):
        return f'{self.name} attends {self.school}'


student = Student('Richard', 'NUS')
student.say_hello()
student.sing_school_song()
print(student)

#what are you?
# print(f'Is it a student? {isinstance(student, Student)}')
# print(f'Is is a person? {isinstance(student, Person)}')
# print(f'Is Student a Person? {issubclass(Student, Person)}')