#1 Program that asks the user to enter a number and check whether the number is odd or even.
a=int(input('Enter a number:'))
rem= a % 2
if rem==0:
    print('The number is even')
else:
    print('The number is odd')

#2 Write a program that takes score as input and assigns a grade based on the following criteria:
#90 and above:Grade A
#80-89: Grade B
#70-79:Grade C
#Below 70:Grade D
score=int(input('Enter your score: '))
if score>=90:
    print('Your grade is A')
elif score>=80 and score<=89:
    print('Your grade is B')
elif score>=70 and score<=79:
    print('Your grade is C')
else:
    print('Your grade is D')

#3 WAP to check if a person is eligible to vote.The eligibility age is 18 or above.
age=int(input('Enter your age: '))
if age>=18:
    print('You are eligible to vote.')
else:
    print('You are not eligible to vote.')

#4 WAP that takes 3 numbers as input and prints the largest among them.
a=float(input('Enter first number: '))
b=float(input('Enter second number: '))
c=float(input('Enter third number: '))
if a>b and a>c:
    print('The largest number is:',a)
elif b>a and b>c:
    print('The largest number is:',b)
else:
    print('The largest number is:',c)

#5 Write a program to check if a given year is a leap year or not. A year is leap year if:It is divisible by 100 OR it is divisible by 40.
year=int(input('Enter year: '))
if (year%4==0 and year%100!=0) or year%40==0:
    print(f'{year} is a leap year.')
else:
    print(f'{year} is not a leap year.')


#6 WAP to implement a simple calculator.The program should:
#Ask the user for two numbers,
#Ask the user to choose an operation(add,subtract,multiply,divide)
#Perform the choosen operation and print the result.
num1=float(input('Enter first number: '))
num2=float(input('Enter second number: '))
choose=input('Choose an operation: ')
if choose=='add':
    sum=num1+num2
    print(f'sum is {sum}')
elif choose=='subtract':
    sub=num1-num2
    print(f'difference is {sub}')
elif choose=='multiply':
    prod=num1*num2
    print(f'product is {prod}')
elif choose=='divide':
    div=num1/num2
    print(f'quotient is {div}')
else:
    print('Error')

#7 Write a program to print numbers from 1 to 100.
#If a number is divisible by 3,print 'Fizz'
#If divisible by 5, print Buzz
#If divisible by both,print 'FizzBuzz'
#otherwise print the number itself
for i in range(1,101):
    if i %3 ==0 and i %5==0:
        print('FizzBuzz')
    elif i%3==0:
        print('Fizz')
    elif i%5==0:
        print('Buzz')
    else:
        print(i)


#8 Given two variables x=15 and y=20,use conditional statements to print which variable is larger or if they are equal.
x=15
y=20
if x>y:
    print('x is larger')
elif x<y:
    print('y is larger')
else:
    print('x and y are equal')

#9 Given a variable num=7, use a conditional statement to check if the number is even or odd and print the result.
num=7
if num%2==0:
    print('7 is even')
else:
    print('7 is odd')

#10 WAP to check whether a given number is divisible by 7 or not
num=int(input('Enter a number: ')) 
if num%7==0:
    print(f'{num} is divisible by 7')
else:
    print(f'{num} is not divisible by7')

#11 Check if the value 10 is not present in the tuple t=(5,15,20,25)
t=(5,15,20,25)
a=(10 not in t)
if a==True:
    print('10 is not in the tuple')
else:
    print('10 is in the tuple')

#12 Determine if the value 25 is present in the list using a simple conditional statement 
lst=[10,20,30,40,50]
if (25 in lst)==True:
    print('25 is present in the list')
else:
    print('25 is not present in the list')

#13 Check if the value 100 exists in the set
s={50,75,100,125}
r=(100 in s)
if r==True:
    print('100 is present in the set')
else:
    print('100 is not present in the set.')









