#types of argument
#1 positional argument
#2 keyword argument
#3 default argument
#4 arbitrary argument

#1 positional argument
def show(name,address):
    print(f'my name is {name}')
    print(f'my address is {address}')
show('rita','pokhara') # position anusar value rakhna parxa

#2 keyword argument
def show(name,address):
    print(f'my name is {name}')
    print(f'my address is {address}')
show(name='rita',address='pokhara') #keyword and values together, position doesnt matter

#3 default argument
def show(name,address,age=45):#age is default argument, last wala lai matra default dina painxa
    print(f'my name is {name}')
    print(f'my address is {address}')
    print(f'my age is {age}')
show(name='rita',address='pokhara') #yha pani age diyo vane yha kai value print hunxa.

#4 arbitrary argument=variable length argument
#two types: arbitrary position and arbitrary keyword

#arbitrary position: denoted by *
def show(*n): #sabai value lin ako lai astrick
    print(n)
show(1,2,3,4)

#arbitrary keyword: denoted by **
def show(*a,**n): #using both position and keyword
    print(a)
    for i,j in n.items(): #i ma keys, j ma values
        print(i,j)
show(1,2,3,4,name='apu',age=22)

#return function=exit the function and returns the value
def show(n):
    print('hello') #linxa
    return n**4 #yha bata function exit hunxa
    print('hello') #yo linna kina vane return le function exit garera aafno value matra dinxa
print(show(2)) #return use garda call garni bela sadhai print lekhna parxa

#lambda function=anonymous function, doesnt have identity
#syntax: lambda argument:expression
a=lambda x,y,z:x*y/z+2
print(a(5,2,4))



import sys
print(sys.getrecursionlimit()) #1000 is set by python
print(sys.setrecursionlimit(45)) #3000 banauxa

#recursion function=function calling itself
def display():
    print('hello')
    display() #function bhitrai func lai call
display()

#base case(stop case), recursion case
def show(n):
    if n==10: #base case
        return
    print('hello',n)
    show(n+1)  #recursion case
show(0)

#factorial=n*(n-1)!
def show(n):
    if n==1 or n==0:
        return 1
    return n*show(n-1)
print(show(5))


    





