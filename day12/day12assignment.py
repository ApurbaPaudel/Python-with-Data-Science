#1 Given a list of integers [1,2,3,4,5] use map to create a new list where each element is squared
n=[1,2,3,4,5]
a=lambda n:n**2
b=map(a,n)
print(list(b))

#2 From the list [10,15,20,25,30] use filter to get a new list containing only numbers divisible by 10
n=[10,15,20,25,30]
a=lambda n:n%2==0
b=filter(a,n)
print(list(b))

#3 Use reduce to calculate the product of all numbers in the list [1,2,3,4,5]
n=[1,2,3,4,5]
from functools import reduce 
def product(x,y):
    return x*y
a=reduce(product,n)
print(a)

