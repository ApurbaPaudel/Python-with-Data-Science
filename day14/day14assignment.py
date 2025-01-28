#1Create a class called Person with attributes name and age. Create an instance of the class and print the name and age of the person.
class person:
    def __init__(self):
        self.name='Apurba'
        self.age=22
    def show(self):
        print(self.name,self.age)
a=person()
a.show()

#2 Add a method greet to the Person class that prints a greeting message including the person's name.
class person:
    def __init__(self):
        self.name='Apurba'
        self.age=22
    def greet(self):
        print(f'Good morning! I am {self.name}')
a=person()
a.greet()

#3 Write a function that takes a list of shapes(Circle,Square etc) and calls their area()method, demonstrating polymorphism.
class Circle:
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return 3.14*self.radius**2
class Square:
    def __init__(self,length):
        self.length=length
    def area(self):
        return self.length**2
class Rectangle:
    def __init__(self,l,b):
        self.l=l
        self.b=b
    def area(self):
        return self.l*self.b
def calculate_area(shapes):
    for shape in shapes:
        print(f'The area is:{shape.area()}')
circle=Circle(5)
square=Square(4)
rectangle=Rectangle(4,3)
shapes=[circle,square,rectangle]
calculate_area(shapes)

#4 Create a function describe_animal() that takes an object of any class and calls its sound() method. Define classes Cat and Bird with their own implementations of the sound() method. Pass objects of both classes to describe_animal().
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

#5 Define a base class Shape with a method area(). Create two derived classes Circle and Rectangle that implement the area() method differently. Instantiate objects of both classes and call their area() methods.
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

