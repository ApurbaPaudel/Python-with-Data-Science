#Polymorphism types:
#method overloading= eutai class ma same name gareko method jati ni huna payo but parameters must be different

class A:
    def show(self):
        print('hello')
    def show(self,a,b):
        print(a+b)
    def show(self,a,b,c):
        print(a+b+c)
            
a=A()
a.show(2,3,5)
#show method le mathi ko show lai overload garyo

#method overriding:
class A:
    def show(self):
        print('i am parent')
class B(A):
    def show(self):
        super().show() #parent class pani print garna ko lagi
        print('i am child class')
b=B()
b.show() #only b ko dekhauxa
#super()=method that access parent class method

#operator overloading:
a='3'
b='4'
print(a+b)
#string huda concatenate, int huda add garxa same operator le
 #dunder function= double underscore: method
print(int.__add__(1,2))
print(str.__add__('1','2'))

class MyClass:
    def __init__(self,a):
        self.a=a
    def __add__(self,other):
        return self.a+other.b
class YourClass:
    def __init__(self,b):
        self.b=b
a=MyClass(4)
b=YourClass(5)
print(a+b)

#other dunder functions=add,sub,mul,lt(less than),gt(greater than)


# ENCAPSULATION=binding attribute and method in a single unit
class Person:
    def __init__(self):
        self.name='apu'
    def show(self):
        print(self.name)
ob=Person()
print(ob.name)
#esari baira bata access garna namilna ko lagi encapsulation done.

#Encapsulation is done by using access modifier
#public, private and protected
#private=access within same class only
#protected=access within same class and its subclass
 #double underscore=attribute lai private banauna

class Person:
    def __init__(self):
        self.__name='apurba' #name is private attribute
    def show(self):
        print(self.__name)
a=Person()
#print(a.__name) #so baira bata access hunna
a.show() #esari chai milxa
#if show method lai nai private garayo vane tyo pani baira bata access garna mildemaw

#protectd is single under score






