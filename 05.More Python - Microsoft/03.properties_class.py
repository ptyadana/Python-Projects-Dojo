class Presenter():
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        print('in the getter')
        return self.__name

    @name.setter
    def name(self, value):
        print('in the setter')
        self.__name = value

presenter = Presenter('Chris')
presenter.name = 'Christopher'
print(presenter.name)