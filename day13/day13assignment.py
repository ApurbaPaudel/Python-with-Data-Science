#1 Create a function describe_animal() that takes an object of any class and calls its sound() method. Define classes Cat and Bird with their own implementations of the sound() method. Pass objects of both classes to describe_animal()
class Cat:
    def sound(self):
        return 'meow'

class Bird:
    def sound(self):
        return 'chirp'

def describe_animal(animal):
    print(animal.sound())

cat=Cat()
describe_animal(cat)
bird=Bird()
describe_animal(bird)

#2 Define a base class Shape with a method area(). Create two derived classes Circle and Rectangle that implement the area() method differently. Instantiate objects of both classes and call their area() methods.
class Shape:
    def area(self):
        pass
class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return 3.14*self.radius**2
class Rectangle(Shape):
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def area(self):
        return self.length*self.breadth
circle=Circle(5)
print('Area of circle is:',circle.area())

rectangle=Rectangle(4,6)
print('Area of rectangle is:',rectangle.area())



        


   




    
