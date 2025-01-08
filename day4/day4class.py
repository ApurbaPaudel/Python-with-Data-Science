a='hello'
print('sipalaya',a)#calling variable
#formatted string
print(f'sipalaya{a}')

#escape method
a='my name \t is apu' #for space
print(a)
#\n for line break

#SET DATA TYPE
#1 set=data structure,mutable,doesnot allow duplicate value,unordered
a={1}#representation is curly bracket
print(type(a)) #khali rakhe dict type aauxa
a=set() #esari ni lekhna milxa

a={4,3,5,7,1,3,2,'hello','world'}
print(a) #random position ma print hunxa so unordered

print(len(a))
a=[1,2,3,4,4,4,4,'hello','hello']
b=set(a) #removes duplicate value of set a
print(b)

#set methods
a={2,4,3,1,7,8,'hello','world'}
#add=data add in set,single data matra add garna milxa
a.add(56)
print(a) #random position ma aauxa

#multiple data add
#update method
a.update({23,5,6,7,8})#set nai banara rakhna parxa
print(a)

#delete methods
#1 pop
#removes first value agi ko output ma aako first value
a.pop()
print(a)

#2 remove=particular value remove
a.remove('hello')
print(a)

#3 discard
a.discard(23)
print(a)

#diff between remove and discard
#remove ma navako data halyo vane error dekhinxa,discard ma navako data halyo vane error dekhaunna j xa paila tei set print hunxa

#4 clear=clear contents, puts empty set
a.clear()
print(a)

#5 del 
#del a #set nai udxa
print(a)


#set other methods
a={1,2,3,4}
b={2,4,6,8}

#1 union
var=a.union(b)
print(var)

#2 intersection
var1=a.intersection(b)
print(var1)

#3 difference (A-B)and (B-A) are not same
var2=a.difference(b) #A-B
print(var2)

var3=b.difference(a) #B-A
print(var3)

#4 symmetric_difference
#intersection bahek aru
var4=a.symmetric_difference(b)
print(var4)

#5 subset,superset,disjoint yo xa ki nai check garni methods
a={1,2,3,4}
b={2,4}

#issubset
var7=b.issubset(a) #is b subset of a
print(var7) #True

#issuperset
var5=a.issuperset(b)
print(var5) #True

#isdisjoint
var9=a.isdisjoint(b)
print(var9) #False

a=set({1,2,3}) #esari set represent garna pani milxa
print(a)

#frozen set=immutable,kei methods garna mildaina
a=frozenset({1,2,3,4,5})
print(type(a)) #frozenset
#union,intersection haru chai grna milxa
b=a.intersection({2,4,6,8})
print(b)
#likewise union pani garna milxa











