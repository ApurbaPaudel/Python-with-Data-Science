#multiplication table using for loop
#2 x 1 =2
#2 x 2 =4
#till 10 esari nikalna paryo
num=2
for i in range(1,11):
    print(f'{num} x {i} = {num*i}')

#WHILE LOOP= condition true huda samma chalxa
#syntax:
#while condition:comparison or relational operator use
    #block of code
# while 3>2:
#     print('hello') #infinity samma janxa

i=0 #first iteration
while i<5:
    print('hello')
    i+=1 #i=i+1 iteration step up

#pep8=python enhancement prosol=standard way of writing code

#multiplication table using while loop
num=int(input('enter number'))
i=1
while i<11:
    print(f'{num} x {i}={num*i}')
    i+=1

#control statement:it controls the flow of execution
#pass, break,continue

#pass
for i in range(10):
    pass # space secure aile for loop ma kei nalekhna ko lagi but tyo vanda tala ko kura execute hunxa
print('hello')

#break= terminates the execution whenever it comes
i=0
while i<8:
    print(i)
    if i==4:
        break #i ko value 4 vayesi terminate hunxa loop
    i+=1

#continue
for i in range(1,10):
    if i%2==0:
        continue
    print(i) #condition stop garera mathi bata loop start hunxa, even aayesi mathi janxa thus odd matra print hunxa

#game using while loop 
#secret game
import random
secret=random.randint(1,10)
guess=''
limit=5
i=0
while i<limit:
    guess=int(input('enter your guess number: '))
    if guess==secret:
        print('you won')
        print('Do you want to play again?')
        choice=input('enter your choice')
        if choice=='yes':
            continue 
        else:
            break
    i+=1
else:
    print(f'Your limit is over,the secret number was {secret}')





