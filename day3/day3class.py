#sequence data type
#1 LIST= data structure store all variable together, it is mutable(changeble), allow duplicate
#a=12
#b-90.78
#c='hello'
a=[12,34.90,'hello','sita']
print(type(a))
print(a)

#indexing=position of data
#syntax:variable_name[index]
print(a[2])
print(a[-1])

#slicing=accessing the part of the list
#syntax:variable[start:end:step]
print(a[0:3:1])

#for hello h
print(a[2][0]) #index ko indexing
print(a[2][0:3:1]) #hel
print(a[::]) #all
print(a[::-1]) #reverse

#allow duplicate
a=[12,12,12,'hello','hello','sita']
print(a)
#list allows duplicate value
print(len(a)) #kati ota xa list ma

#list methods(mutable)
#1 append method
a=[12,34.89,'hello','tina']
a.append(34) #adds data to the list
print(a)
#34 add hunxa list ko last ma=ordered vaninxa so list lai
#multiple value add
#a.append([34,89,'hello'])
print(a) #list bhitra list aauxa, so append le only single data add

#for multiple,
#2 extend method
a.extend([12,45.98,'tina'])#list banarai halna parxa
print(a)

#bich ma add garna last ma haina
#3 insert(randomly inserting in any index)
a.insert(2,78)
print(a) #2 ma 78 janxa aru 1 1 sarxa
#single data matra add insert le pani

#deleting data methods
#1 pop
#LIFO=Last In First Out
a.pop(5) #5 index ma vako remove, khali rakhe last ma vako out
print(a)

#2 remove
a.remove('hello') #removes hello from the list
print(a)

#3 sabai data ekaichoti remove=clear
a.clear()
#empty list rakhxa

del a #list nai hatauxa

#sort and sorted
#data sorting(asc,desc)
a=[6,4,8,2,3,4,2,3,1]
a.sort() #ascending
print(a)
a.sort(reverse=True)#descending
print(a)
#string ko length anusar sort
a=['banana','apple','pear']
a.sort(key=len)#esma ni asc and desc hunxa

#sorted
b=sorted(a)
print(b)

#diff between sort and sorted
#sort le same mai garxa tesmai add hunxa, sorted le sorted value lai new list ma halxa

#2 TUPLE
#sequence data type, data structure,immutable,allows duplicate values
a=(12,34.67,'hello','tina')#representation
print(type(a))
print(a)
print(len(a))
#indexing,slicing same as in list []ko thau ma ()

#tuple is immutable
#append or others methods use garna mildena,method nai xaina
del a #milxa

#diff between tuple and list
#mutable,immutable, performace of tuple is faster than list





