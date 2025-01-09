#map data type
#1 dictionary=key value pair,data structure,mutable
#representation
a={}
print(type(a))
#or
a=dict()
a={
    'name':'amisha',
    'age':20
}
print(a)
print(len(a))
print(a.keys()) #keys nikalxa
print(a.values()) #value nikalna
print(a.items()) #key value pair nikalxa
a=dict(name='amisha',age=20) #other method of representation

#assessing dictionary values
#indexing and get method
print(a['name'])#key deko, esko value aauxa
print(a['age'])#indexing method
print(a.get('name')) #get method

#diff between get and indexing
#navako key halda:indexing ma error dekhauxa,get ma chai error nadekhai 'none' vanera dekhauxa

#adding value in dictionary
#1 indexing method
a['address']='kathmandu'
a['email']='apu'
print(a)

#2 for multiple key value pair add
#update method
b={
    'email':'apu@gmail',
    'address':'ktm'
    
    
}
a.update(b) #a ma b lai thapni
print(a)

#delete data
del a['name']
print(a)

#pop
a.pop('email')
print(a)

#popitem
a.popitem() #last ko pair hatauxa
print(a)

#nested dictionary
#dict bhitra dict
a={
    'emp1':{
        'name':'apu',
        'age':'23',

    },
    'emp2':{
        'name':'fatima',
        'address':'ktm'
    }
}
print(a['emp1']['name']) #accessing apu
#changing name
a['emp2']['name']='rita'
print(a)

a={
    'name':'amisha',
    'age': 89

}
b={
    'age':56
}
a.update(b)
print(a) #56 auaxa kina vane b update le override garisakyo

#create a dictionary that takes student marks in 5 subjects and print its average marks/percentage
marks={
    'science':45,
    'maths':50,
    'nepali':40,
    'social': 50,
    'physics': 30
}
a=sum(marks.values())
b=len(marks)
print(f'your marks is {a/b}')

#binary data type
#bytes and byte array=used for memory management

#bytes=generates sequence of numbers, binary datatype,range=0 to 255,immutable
a=bytes([1,2,3,4,5])
print(type(a))
print(a[1])
print(a) #object form/binary form ma aauxa

#day 3 class xuteko:
a=[1,2,3,'hello','world']
a[0]='hi'
print(a) #so list is mutable

#bytes ma mildena so immutable

a=bytes([1,2,3,4,5]) #255 vanda dherai garna mildena

#bytearray=it generates sequence of numbers,0 to 255, it is mutable
a=bytearray([1,2,3,4,5])
print(type(a))
print(a)#object or binary form ma aauxa
print(a[2]) #index 2 ma vako print

#mutable
a[0]=6
print(a)

#boolean data type
a=True #1 ni vanina
print(type(a)) #bool
#false lai 0 ni vaninxa
#bit ma kaam garda

#none date type=absence of values
#a=
print(a) #error hunxa
a=None
print(type(a)) #NoneType 






