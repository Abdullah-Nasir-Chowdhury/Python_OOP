"""You need to have an underscore before a class name to make it private!"""
class _Private:
    def __init__(self, name):
        self.name = name

class NotPrivate:
    def __init__(self, name):
        self.name = name
        self.priv = _Private(name)

    def _display(self):
        print("Hellow")

    def display(self):
        print("Hi")