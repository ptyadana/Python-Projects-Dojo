class Presenter():
    def __init__(self, name):
        self.name = name

    def say_hello(self):
        print(self.name)

presenter = Presenter('Chris')
presenter.name = 'Christopher'
presenter.say_hello()