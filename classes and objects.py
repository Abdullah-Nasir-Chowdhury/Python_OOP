# # objects
# # anything is an object in python.
# x = 5
# y = 'string'
# # see that int and string are both classes
# print(type(x))
# print(type(y))



# create your own class:

# class, instance, attribute, methods
# python class names are started by CapitalLetters and no spaces by convention
# function names are done by small letters and underscores.
class Human(object):
    # This is a Class Attribute, These are common in all human
    species = 'Homo sapiens'

    # initialize the objects state by assigning the values of the objects properties
    def __init__(self, name, age, weight):
        print('Nice you made a Human class')
    # These are called Instance Attributes and vary from human to human:
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

# This is an object of class Human, also known as an Instance or Human Class Instance:
tim = Human('Tim', 54, 75)
# Creating an instance of a class is called instantiation, as you have done above.

# The object of class Human is using the method speak:
tim.speak()

# The object of class Human is using the mehod change_name:
tim.change_age(5)
tim.speak()

# So, the class is human()
# methods are functions defined within the class, such as speak, change_age
# Instance is the object of the class human()

# Here, the instance tim is changing it's class instance species!
tim.species = 'No homo!'
print(tim.species)

# Now, tim is a very weird human, but this is Python..

# Key takeaway is that classes are mutable in python just like lists
# but strings and tuples are immutable in python.