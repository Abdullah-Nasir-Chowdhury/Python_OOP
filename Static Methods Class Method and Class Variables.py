class Dog:
    # class variable:
    dogs = []

    def __init__(self, name):
        name = self.name
        self.dogs.append(self)

    @classmethod
    def num_dogs(cls):
        return len(cls.dogs)

    @staticmethod
    def bark(n):
        # bark n times
        for _ in range(n):
            print("bark!")