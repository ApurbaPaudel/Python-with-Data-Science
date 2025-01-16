#1 Write a program to print the squares of numbers from 1 to 10 using a for loop
for i in range(1,11):
    print(i**2)

#2 Write a program to print all even numbers between 1 and 20 using a for loop
for i in range(1,21):
    if i%2==0:
        print(i)

#3 Write a program to calculate the sum of even numbers from 1 to 50 using a for loop.
sum=0
for i in range(1,51):
    sum+=i
print('The sum of numbers from 1 to 50 is:',sum)

#4 Write a program to calculate the sum of all odd numbers between 1 and 100 using a for loop.
odd_sum=0
for i in range(1, 101, 2):
    odd_sum+=i
print('The sum of odd numbers from 1 to 100 is:',odd_sum)

#5 Write a program to find the largest number in a list [2,8,1,16,5,23,7] using for loop
list=[2,8,1,16,5,23,7]
largest=list[0]
for num in list:
    if num>largest:
        largest=num
print('The largest number in the list is:',largest)

#6 Write a program that uses a while loop to print numbers from 1 to 10.
i=1
while i<=10:
    print(i,end=' ') 
    i+=1

#7 Write a program to calculate the sum of numbers from 1 to 50 using a while loop
sum=0
i=1
while i<=50:
    sum=sum+i
    i+=1
print('The sum of numbers from 1 to 50 is:',sum)

#8 Write a program that prints all even numbers between 1 and 20 using a while loop
i=1
while i<=20:
    if i%2==0:
        print(i)
    i+=1

#9 Write a program that uses a while loop to print numbers from 10 to 1 in reverse order
i=10
while i>=1:
    print(i)
    i-=1

#10 Write a program that keeps taking input from the user and stops only when the user types 'stop'
while True:
    user=input('enter the input')
    if user=='stop':
        break

#11 Write a program to print the multiplication table of 5 using a while loop.
num=5
i=1
while i<=10:
    print(f'{num}x{i}={num*i}')
    i+=1

#12 Write a program to print the square of numbers from 1 to 10 using a while loop.
i=1
while i<=10:
    print(i**2)
    i+=1

#13 Write a program to calculate the sum of all odd numbers between 1 and 30 using a while loop.
i=1
sum=0
while i<=30:
    if i%2!=0:
        sum=sum+i
    i=i+1
print('The sum is:',sum)

    




    

