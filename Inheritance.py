# create a class:
class Human(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        print('Hi, I am', self.name, 'and I am', self.age, 'years old')

class Dog(object):
    def __init(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color

    def speak(self):
        print('Roof')

# Inherit from Dog:
class Cat(Dog):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color
    
    def speak(self):
        print('Meow')

tim = Human('Abdullah', 21)
tim.speak()