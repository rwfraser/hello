import math

internalpi = math.pi

print(f'PI is equal to: {internalpi}')

class Circle:
    def __init__(self, radius=1):
        self.radius = radius

    def getPerimeter(self):
        return 2 * self.radius * math.pi

    def getArea(self):
        return self.radius *self.radius * math.pi

    def setRadius(self, radius):
        self.radius = radius
UserRadius = input("please enter the radius of your Circle")
UserRadius = float(UserRadius)
print(f"Area is: {Circle(UserRadius).getArea()}")