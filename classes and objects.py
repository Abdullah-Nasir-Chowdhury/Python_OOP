# # objects
# # anything is an object in python.
# x = 5
# y = 'string'
# # see that int and string are both classes
# print(type(x))
# print(type(y))



# create your own class:

# class, instance, attribute, methods
class Human(object):
    # This is an instance:
    def __init__(self, name, age, weight):
        print('Nice you made a Human class')
    # This is an attribute:
        self.name = name
        self.age = age
        self.weight = weight

    # This is a method of class Human:
    def speak(self):
        print("Hi I am", self.name, 'and I am', self.age, 'years old')

    # This is a method of class Human:
    def change_age(self, age):
        self.age = age

    # This is a method of class Human:
    def add_weight(self, weight):
        self.weight = weight


tim = Human('Tim', 54)
tim.speak()
tim.change_age(5)
tim.speak()