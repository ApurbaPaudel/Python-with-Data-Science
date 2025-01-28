#1 Create a parent class person with attributes name and age.
#Create a child class Student that inherits person and adds an attribute grade. Display the details using a method.
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def show(self):
        print('Name:',self.name)
        print('Age:',self.age)
class Student(Person):
    def __init__(self,name,age,grade):
        super().__init__(name,age)
        self.grade=grade
    def show(self):
        super().show()
        print('Grade:',self.grade)
s=Student('Apurba',22,'A')
s.show()

#2 Implement multiple inheritance where ClassA and ClassB have methods methodA() and methodB(), respectively. The child class ClassC should inherit both and call methods from both parents
class A:
    def __init__(self):
        self.name='apurba'
    def methodA(self):
        print('Name:',self.name)
class B:
    def __init__(self):
        self.age=22
    def methodB(self):
        print('Age:',self.age)
class C(A,B):
    def __init__(self):
        self.rollno=5
        A.__init__(self)
        B.__init__(self)
    def methodC(self):
        print('Rollno:',self.rollno)
c=C()
c.methodA()
c.methodB()
c.methodC()

#3 Use super() method in a child class to call the parent class constructor and method
class Par:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def show(self):
        print('Name:',self.name)
        print('Age:',self.age)
class Std(Par):
    def __init__(self,name,age,roll):
        super().__init__(name,age)
        self.roll=roll
    def show(self):
        super().show()
        print('Rollno:',self.roll)
c=Std('Apurba',22,5)
c.show()

#4 Write a function that takes a list of shapes (Circles,Square,etc) and calls their area method
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

#5 Create a class Student with private attributes name and grade. Write methods to set and get the values of these attributes.
class Student:
    def __init__(self):
        self.__name=None
        self.__grade=None
    def setValues(self,name,grade):
        self.__name=name
        self.__grade=grade
    def getValues(self):
        print(f'name={self.__name}')
        print(f'grade={self.__grade}')
s=Student()
s.setValues('Apurba','A')
s.getValues()

#6 Write a class Car with private attributes make and year. Add methods to update the year only if it is greater than the current value
class Car:
    def __init__(self,make,year):
        self.make=make
        self.year=year
    def update(self,new_year):
        print(self.make)
        if new_year>self.year:
            print(new_year)
        else:
            print(self.year)
c=Car('Maruti',2001)
c.update(2000)

#7 Write a class BankAccount with private attriutes acc_num and balance.Add methods to:
#deposit money(validate that the amount is positive)
#withdrawmoney(ensure sufficient balance)
#view the current balance
class BankAccount:
    def __init__(self,__acc_num,__balance):
        self.__acc_num=__acc_num
        self.__balance=__balance
    def deposit(self,amount):
        if amount>0:
            self.__balance+=amount
        else:
            return 'enter a valid amount to deposit'
    def withdraw(self,amount):
        if amount>self.__balance:
            return 'Insufficient balance'
        else:
            self.__balance-=amount
    def view(self):
        print('Your balance is:',self.__balance)
a=BankAccount(1234,147181)
a.deposit(10000)
a.withdraw(100000)
a.view()

#8 Implement a class Employee with a private attribute salary and methods to:
#set the salary(with the condition that it must be greater than zero)
#get the salary

class Employee:
    def __init__(self):
        self.__salary=None
    def setSalary(self,salary):
        if salary<0:
            print('Salary must be greater than zero')
        else:
            self.__salary=salary
    def getSalary(self):
        return self.__salary
e=Employee()
e.setSalary(20000)
print('Your salary is:',e.getSalary())


