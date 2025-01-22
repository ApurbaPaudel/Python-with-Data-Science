# #decorator= denoted by @,function that takes another function's argument and add some features and return added features in new function
#1 
def show():
    print('hello')
    return 'apu'
print(show())

# #2 Everything in python is object
def show():
    print('hello')
a=show #show vanni function lai a vanni object ma rakheko
a() #vanesi esari call garna paiyo

# #3 nested function
def outer():
    def inner():
        print('i am inner function')
    print('i am outer function')
    inner()
outer() 

# #4 A function can take another function as argument
def outer(a):
    def inner():
        print('i am inner')
        a()
    inner()
    print('i am outer')
def show():
    print('i am outside')
outer(show)

#use method
def outer(a):
    def inner():
        print('i am inner')
        a()
    return inner
@outer
def show():
    print('i am outside')
show()

#OOP=Object Oriented Programming 
#diff between oop and pop: pop uses function and procedure, oop uses classes and object, code reusablity easy in oop, data secure, encapsulation
#OOP uses classes and object
#class= blueprint or template for creating object, contains attributes and methods
#object=instance of class
#attributes=represents variable that holds data
#method= similar to function

#syntax:
# class ClassName:
#     #attributes and methods
# object=ClassName()

class Student:
    def __init__(self,name,age): #init=constructor:initialize current object and variables
        self.name=name
        self.age=age
    def show(self):
        print(self.name,self.age)
a=Student('apurba','22')
print(a.name)
a.show()

#types of methods and attributes
#attribute
#1 instance 
#2 class
#3 static

#method
#1 instance
#2 class
#3 static

#Instance method
#particular or individual defined and initialized with the help of self parameter
#each object has its own variable file
class A:
    def __init__(self):
        self.name='apurba'
        self.age=22
    def show(self):
        print(self.name,self.age)
a=A()
a.name='rita' #a ma matra change huni vayo
a.show()
b=A()
b.show()









