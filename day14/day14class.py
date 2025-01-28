#instance method:variable lai baira bata access garna object.variable
#class:ClassName.variable


#class method
#define and initialize using cls parameter

class Student:
    school='sns'
    def __init__(self):
        self.name='apu'
        self.age=22
    def show(self):
        print(self.name,self.age)
    @classmethod
    def display(cls,pr):
        cls.school=pr
        print(f'my school name is {cls.school}')
a=Student()
a.display('ambition')

b=Student()
print(Student.school)

c=Student()
print(Student.school)

#@classmethod lekheko vara clas ko mathi, a b c sab ma change hunchha

#static method
class A:
    @staticmethod #class,instance duitai ko kaam garxa
    def show(a,b):
        print(a+b)
a=A()
a.show(2,3)


#Fundamentals of OOP
#inheritance
#polymorphism
#encapsulation
#abstraction

#1 INHERITANCE=class inherits another class and share attributes and methods
#parent/base class
#derived/child class

#Types:
#1 Single inheritance: 
class A: #base
    def feature1(self):
        print('I have feature 1')
class B(A): #derived class,B le A lai inherit garyo
    def feature2(self):
        print('I have feature 2')

b=B()
b.feature2()
b.feature1()

#2 multilevel inheritance
#A-B-C
#A(Grandparent),B(child of A,parent of C), C(child of B)
class A:
    def feature1(self):
        print('Feature1')
class B(A):
    def feature2(self):
        print('feature2')
class C(B):
    def feature3(self):
        print('feature3')
c=C()
c.feature1()
c.feature2()
c.feature3()

#3 Multiple Inheritance=2 parents,1 child
class A: #parent
    def feature1(self):
        print('Feature1')
class B: #parent
    def feature2(self):
        print('feature2')
class C(A,B): #child
    def feature3(self):
        print('feature3')
c=C()
c.feature1()
c.feature2()
c.feature3()

#Hierarchical inheritance=1 parent, 2 child
class A: #parent
    def feature1(self):
        print('Feature1')
class B(A): #parent
    def feature2(self):
        print('feature2')
class C(A): #child
    def feature3(self):
        print('feature3')

b=B()
c=C()
b.feature1()
b.feature2()
c.feature3()
c.feature1()

#Hybrid Inheritance=all combined


#POLYMORPHISM=one thing behaving in a different way
#duck type:
class MyClass:
    def show(self): #method
        print('hello')
class YourClass:
    def show(self):
        print('hi')
def display(var): #function
    var.show()
a=MyClass()
b=YourClass()
display(a) #hello
display(b) #hi


#normal method
# a=MyClass() #object for myclass
# a.show() #hello print
# b=YourClass()
# b.show()

