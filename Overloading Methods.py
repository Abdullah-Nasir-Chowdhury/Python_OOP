class Point():
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        self.coordinates = (self.x,self.y)

    def move(self, x, y):
        self.x += x
        self.y += y

    def __add__(self, p):
        return Point(self.x + p.x, self.y + p.y)

    def __sub__(self, p):
       return Point(self.x - p.x, self.y - p.y)

    def __mul__(self, p):
        return self.x * p.x + self.y * p.y

    # define function for calculation of length
    def length(self, p):
        import math
        return math.sqrt(self.x**2 + self.y**2)

    # check greater than:
    def __gt__(self, p):
        return self.length() > p.length()

    # check greater than or equal to:
    def __ge__(self, p):
        return self.length() >= p.length()

    # check lesser than:
    def __lt__(self, p):
        return self.length() < p.length()

    # check less than or equal to:
    def __le__(self, p):
        return self.length() <= p.length()

    # check equal to:
    def __eq__(self, p):
        return self.x == p.x and self.y == p.y

    def __str__(self):
        return "[" + str(self.x) + ',' + str(self.y) + "]"

p1 = Point(1,2)
p2 = Point(2,3)
p3 = Point(3,4)
p4 = Point(4,5)

p_sum = p1 + p2
p_dif = p1 - p2
p_mult = p1 * p2

print(p_sum)
print(p_dif)
print(p_mult)

print(p1>p2)
print(p1<p2)
print(p1==p2)