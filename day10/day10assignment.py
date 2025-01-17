#1 Write a python function called print_square that takes a number as an argument and prints the square of that number
a=int(input('enter a number'))
def print_square(a):
    print(a**2)
print_square(a)

#2 Write a python function called print_list_elements that takes a list as an argument and prints each element in the list one by one
list=[1,2,3,4,5]
def print_list_elements(list):
    for i in list:
        print(i,end=' ')
print_list_elements(list)

#3 Write a python function called multiply_by_two that takes a number as an argument and prints the number multiplied by 2
num=int(input('enter a number'))
def multiply_by_two(num):
    print(num*2)
multiply_by_two(num)

#4 Make a calculator by using function where each operator has its own function
num1=int(input('enter first number'))
num2=int(input('enter second number'))
choice=input('enter your choice')
if choice=='add':
    def add(num1,num2):
        print(num1+num2)
    add(num1,num2)
elif choice=='subtract':
    def sub(num1,num2):
        print(num1-num2)
    sub(num1,num2)
elif choice=='multiply':
    def prod(num1,num2):
        print(num1*num2)
    prod(num1,num2)
elif choice=='division':
    def div(num1,num2):
        print(num1/num2)
    div(num1,num2)
else:
    print('Invalid choice of operation')

#5 Write a program to create a function that takes two arguments, name and age and print their value
name=input('enter your name')
age=int(input('enter your age'))
def a(name,age):
    print('Your name is:',name)
    print('Your age is:',age)
a(name,age)

#6 Write a program to create function func1() to accept a variable length of arguments and print their value.
def func1(*args):
    print('Values are:')
    for i in args:
        print(i)
func1(1,2,3)
func1('h','e','l')
func1(5,6,7)

#7 Write a program to create function calculation() such that it can accept two variables and calculate addition and subtraction
a=int(input('enter first number'))
b=int(input('enter second number'))
def calculation(a,b):
    print(f'The sum is {a-b}')
    print(f'The difference is {a+b}')
calculation(a,b)


    


        


