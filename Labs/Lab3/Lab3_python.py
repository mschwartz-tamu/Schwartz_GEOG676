# create classes
class Shape():
    def __init__(self):
        pass

class Rectangle(Shape):
    def __init__(self, l, w):
        self.length = l
        self.width = w
    def getArea(self):
        return self.length * self.width

class Circle(Shape):
    def __init__(self, r):
        self.radius = r
    def getArea(self):
        return 3.14 * self.radius * self.radius
    
class Triangle(Shape): 
    def __init__(self, b, h):
        self.base = b
        self.height = h
    def getArea(self):
        return 0.5 * self.base * self.height

# read text file
file = open(r'C:\Users\mschwartz95\Documents\Lab3_shapes.txt', 'r')
lines = file.readlines()
file.close()

for line in lines:
    components = line.split(',')
    shape = components[0]

    if shape == 'Rectangle':
        rct = Rectangle(int(components[1]), int(components[2]))
        print('Area of the Rectangle is: ', rct.getArea())
    elif shape == 'Circle':
        crl = Circle(int(components[1]))
        print('Area of the Circle is: ', crl.getArea())
    elif shape == 'Triangle':
        tri = Triangle(int(components[1]), int(components[2]))
        print('Area of the Triangle is: ', tri.getArea())
    else:
        pass
