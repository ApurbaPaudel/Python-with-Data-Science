#iterator= object that contain countable number of values
def show(n):
    return n+2
n=2 #esma 2 ko thau ma list diyo vane mildena
print(show(n))

#map, filter, reduce
# map()=inbuilt function that takes function and iterator, each element ma function apply garxa
# syntax: map(function,iterator)
def show(n):
    return n+2
n=[1,2,3,4,5]
b=map(show,n)
print(b) #object form ma aauxa
print(list(b)) #each element ma function apply garera list mai output aauxa

#using lambda function
a=lambda n:n+2
b=[1,2,3,4]
c=map(a,b)
print(list(c))

#filter()=inbuilt function that takes function and iterator and it process according to condition
#syntax: filter(function,iterator)

def show(n):
    if n%2==0:
        return n
n=[1,2,3,4,5]
b=filter(show,n)
print(list(b))

#using lambda function
a=lambda n:n%2==0
x=[1,2,3,4,5]
y=filter(a,x)
print(list(y))

#next
n=[1,2,3,4]
print(list(filter(lambda x:x%2==0,n)))

#reduce()=inbuilt function that takes function and iterator,gives answer in single value
from functools import reduce
n=[1,2,3,4]
def sum(x,y):
    return x+y
b=reduce(sum,n)
print(b)

n=[1,2,3,4]
print(reduce(lambda x,y:x+y,n))

#list comprehensive=shorter syntax

# normal
a=[1,2,3,4]
b=[]
for i in a:
    b.append(i+2)
print(b)

# list comprehensive
a=[1,2,3,4]
b=[]
[b.append(i+2)for i in a]
print(b)

a=['sita','hari','ram','shyam']
b=[len(i) for i in a]
print(b)

a=['sita','hari','ram','shyam']
b=[f'{i}:{len(i)}' for i in a]
print(b)

a=[
    'youtube.com',
    'facebook.com',
    'whatsapp.com'
]
a=[i.strip('.com')for i in a]
print(a)
#or
a=[i.removesuffix('.com') for i in a]
print(a)








