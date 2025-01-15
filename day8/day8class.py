a=int(input('enter your first number:'))
b=int(input('enter your second number:'))
op=input('enter your operator')
if op=='+':
    print(a+b)
elif op=='-':
    print(a-b)
elif op=='*':
    print(a*b)
elif op=='**': #power
    print(a**b)
elif op=='/':
    print(a/b)
else:
    print('invalid operator')

#ROCK PAPER SCISSOR
#Module=file (random: inbuilt model for random variable generator)
import random
print('We are playing rock paper scissor game')
print('Rule: S>P,P>R,R>S')
computer=random.choice(['S','P','R']) #computer le random choose
user=input('Enter your choice')
user=user.upper() #user ko string lai upper ma change
print(user)
print(computer)
if (user=='S' and computer=='P') or (user=='P' and computer=='R') or (user=='R' and computer=='S'):
    print('YOU WON')
elif computer==user:
    print('Draw')
elif user not in ['S','P','R']:
    print('INVALID CHARACTER')
else:
    print('YOU LOSE') 

#even and odd
a=int(input('enter your number: '))
if a%2==0:
    print('even')
else:
    print('odd')

#LOOP=repeating something over and over until particular condition is matched.
a='hello'
#printing hello 10 times
#two types of loop
#for loop and while loop

#For loop
#range:sequence data type,generates numbers in that range
#syntax:range(start,end,step)
a=range(10) #end=10(Single huda),default start=0,default step=1
#end vanda 1 step tala ko print hunxa
print(type(a))
print(a)
a=range(1,10,1)
print(a)
a=range(5,0,-1) #5 4 3 2 1 
print(a[0])

#for loop
#syntax:
for i in range(10): #start=0,end=10 but print till 9,step=1
    print(i) #0 to 9 print hunxa
for i in range(1,10,2):
    print(i,end='*')
    if i==3:
        print('go') #3 ko thau ma go
#for horizontal:print(i.end='')

a=['rita','sita','gita','hari']
for i in a:
    print(i) #rita
    for j in i:
        print(j) #r
















































































































