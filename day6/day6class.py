#OPERATOR
#symbol that performs operations between operands
# a+b

#1 Arithmetic operator

a=4
b=9
print(a+b) #addition
print(a-b) #subtract
print(a*b) #multiply
print(a/b) #divide
print(a%b) #modulos
print(a//b) #floor #decimal hatayera whole number matra rakhxa
print(a**b) #power
#ceil le decimal hatayera ek step mathi garauxa

#2 Relation or comparison operator
a=7
b=9
print(a<b)
print(a>b)
print(a<=b)
print(a>=b)
print(a==b)
print(a!=b) #not equal to

#3 Assignment operator
a=6 #=
a=a+1 
a+=1
#both are same, +=,-=,all= are operators
#a*=4 is same as a=a*4


#4 Logical operator
#and,or,not
a=True #1
b=False #0
#and=both true then return true
#or=either or both true, will be true
#not=opposite return
print(a and b)
print(a or b)
print(not a)
print(not b)

#5 Membership operator
#(in,not in)
a='my name is apu'
print('my'in a)
print('My'in a)
print('amisha'not in a)

#6 identity operator(is,is not)
a=[1,2,3]
b=[1,2,3]
#memory ma kun address ma basexa a ra b
print(id(a))
print(id(b)) 
print(a is b) #False
print(a==b) #True
#diff between is and ==: == le exact value herxa, is le chai memory address herxa(memory address tracker)

#7 Bitwise operator
#it takes integer value and converts it into binary, performs operation in bit
# &(and) |(or) ~negation, ^XOR
a=12
# 8 4 2 1
# 1 1 0 0
b=13
# 8 4 2 1
# 1 1 0 1
print(a & b) #12 #1100
print( a | b) #13 #1101
print(~a) #2's complement: value lai 1 le badauxa ra negative bnauxa, 1's complement le value lai invert garxa 0 to 1 and vice versa
print(~b)
#xor ^ exclusive or: diff vayo vane true, same vayo vane false
print(a ^ b)


#INPUT
#input(): inbuilt fuction, it takes data from user
a=input('Enter your number')
print(a)
print(type(a)) #string type: input string type ko hunxa

#for integer date,typecasting
a=int(input('Enter')) #int bahek float and other type ni esari






