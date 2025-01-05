#text data type= string
#string= collection of 1 or more character it is denoted by quotation (',"")
a='''welcome
i read in sipalaya
i am from pkr''' #multiple line triple quotation
print(a)

a='my name is apu'
#len()=length of character
print(len(a))

#character
#indexing=character position 0 bata suru hunxa space ganinxa
#syntax:variable_name[index]
print(a[-1])

#slicing=accessing the part of the string
#syntax:variable_name[start:end:step]
print(a[3:7:1])#end value ma plus 1 lekhna parxa, step rakhena vane by default 1 bujxa
#reverse
print(a[6:2:-1]) #end ma minus 1 garni reverse ma
print(a[2:]) #2 dekhi paxi ko sabai print
print(a[:7]) #0 to 6 samma print
print(a[::]) #all
print(a[::-1]) #all reverse

#string methods
#string is immutable= original value does not change
#1 upper() #uppercase banauna
a='my name is APU'
a.upper() 
print(a) #cannot because immutable
#so
b=a.upper()
print(b)

#2 lower() #lowercase banauna
c=b.lower()
print(c)

#3 swapcase() #lower to upper and vise versa
d=a.swapcase()
print(d)

#4 capitalize makes first letter capital and other lower
e=a.capitalize()
print(e)

#5 count()
b=a.count('a') #a vanni kati ota xa count
print(b)

#6 find() #tyo character kun index ma xa vanera find
b=a.find('U')
print(b)

#replace
b=a.replace('APU','hi') #replace APU with hi
print(b)

#strip()
a='ewel come'
print(a)
b=a.strip() #agadi ra paxadi ko space hatauxa
print(b)
c=a.strip('w') #agadi or paxadi vako matra hatauxa
print(c)
d=a.removesuffix('e') #paxadi ko matra remove
print(d)
e=a.removeprefix('e') #agadi ko matra remoxe
print(e)

#split
a="orane apple pears"
b=a.split() #list ko form ma rakhna ko lai
print(b)

c="orange,apple,pear"
d=c.split(',') #yha j xa tyo le xuttauxa
print(d)

#center=kunai character lai center ma rakhni kaam
a="my name is apu"
b=a.center(70,'&') #70 character ko bich ma rakhxa 35 35 garera
print(b)

print(a[-1])










