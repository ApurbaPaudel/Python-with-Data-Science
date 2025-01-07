#1 Given a list my_list[10,20,30,40,50] access the third element and store it in a variable third_element
my_list=[10,20,30,40,50] 
third_element=my_list[2]
print(third_element)

#2 Create a new list containing the first three elements of the list my_list
my_list=[10,20,30,40,50]
new_list=my_list[:3:]
print(new_list)

#3 Convert the str='apple,banana,cherry' to a list of fruits
str='apple,banana,cherry'
fruits=str.split(',')
print(fruits)

#4 Replicate the list my_list=[1,2,3] three times to form a new list [1,2,3,1,2,3]
my_list=[1,2,3]
my_list.extend([1,2,3])
print(my_list)

#5 List a=['hello',45.67,89.90,45,45,'apple','orange']
#add value 34 to the list
a=['hello',45.67,89.90,45,45,'apple','orange']
a.append(34)
print(a)
#add multiple value to the list
a.extend(['hi',100])
print(a)
#using slicing extract app from the given list
print(a[5][0:3:1])
#remove random value from the list(45)
a.remove(45)
print(a)
#remove all data from the list
a.clear()
print(a)

#6 Given two list a and b add these two list in third list and print the third list
a=[10,'nice',20,'maths']
b=[30,'bad',40,'english']
c=a+b
print(c)

#7 Given two tuple1 and tuple 2 concatenate them to form a new tuple
a=(10,20,30,40,50)
b=(60,70,80,90,)
c=a+b
print(c)

#8 Given the tuple my_tuple, slice the tuple to get the last three elements
my_tuple=(10,20,30,40,50)
print(my_tuple[2::1])

#9 Find the length of the tuple my_tuple=['a','b','c','d']
my_tuple=['a','b','c','d']
print(len(my_tuple))

#10 Given a list a=[3,5,32,4,52,13,4,6,71] sort in ascending and descending order using both method
a=[3,5,32,4,52,13,4,6,71]
a.sort()#ascending
print(a) 
a.sort(reverse=True) #descending
print(a)

#sorted
b=sorted(a)#ascending
print(b)
c=sorted(a,reverse=True) #descending
print(c)
