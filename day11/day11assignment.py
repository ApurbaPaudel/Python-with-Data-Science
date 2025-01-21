#1 Create a function that takes two numbers as input and returns their sum
a=int(input('enter first number'))
b=int(input('enter second number'))
def add(a,b):
    return a+b
print(add(a,b))

#2 Write a function factorial that computes the factorial of a number using recursion
n=int(input('enter a number'))
def factorial(n):
    if n==0 or n==1:
        return 1
    return n*factorial(n-1)
print(factorial(n))

#3 Define a function that checks whether a given string is a palindrome.
def palindrome(str):
    string=str.lower()
    return string==string[::-1]
print(palindrome('madam')) #True
print(palindrome('hello')) #False

#4 Write a function max_of_three that takes three numbers and returns the largest of the three.
a=int(input('enter a number'))
b=int(input('enter second number'))
c=int(input('enter third number'))
def maximum(a,b,c):
    return max(a,b,c)
print(maximum(a,b,c))

#5 Create a function that takes a number as input and returns True if the number is prime otherwise false
def num(n):
    if n<=1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True
print(num(5)) #True
print(num(10)) #False

#6 Write a function fibonacci that takes a number n and returns the first n terms of the Fibonacci sequence as a list.	
n=int(input('enter number'))
def fibonacci(n):
    if n<=0:
        return[]
    elif n==1:
        return[0]
    elif n==2:
        return[0,1]
    fib_sequence=[0,1]
    for i in range(n-2):
        fib_sequence.append(fib_sequence[-1]+fib_sequence[-2])
    return fib_sequence
print(fibonacci(n))

#7 Define a function count_vowels that takes a string as input and counts the number of vowels in the string.
a=input('enter a string')
def count_vowels(a):
    vowels='aeiouAEIOU'
    count=0
    for i in a:
        if i in vowels:
            count+=1
    return count
print(count_vowels(a))

#8 Write a function that takes a string and returns the reversed string.
str=input('enter a string')
def rev(str):
    return str[::-1]
print(rev(str))

#9 Write a function that takes a list and returns a new list with duplicates removed.
def rem_dup(list):
    return (set(list))
list=[1,2,2,3,4,4,5]
print(rem_dup(list))

#10 Write a function sort_list that takes a list of numbers and returns the list sorted in ascending order.
list=[4,5,2,3,1]
def sort_list(list):
    return sorted(list)
print(sort_list(list))




