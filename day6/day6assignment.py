# #1 Write a python program to calculate the area of a rectangle.Take length and width as input and use multiplication.
length=float(input('Enter length of rectangle:'))
breadth=float(input('Enter breadth of the rectangle:'))
area=length*breadth
print('Area of rectangle is:',area)

#2 Create a program to calculate the remainder when 25 is divided by 7.
a=25
b=7
rem=a % b
print('remainder is:',rem)

#3 Write a program to check if a number is greater than, less than or equal to another number.
a=int(input('Enter first number:'))
b=int(input('Enter second number:'))
if a>b:
    print('a is greater')
elif b>a:
    print('b is greater')
else:
    print('a and b are equal')
