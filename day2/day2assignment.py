#1 extract the first 5 characters of the string"HelloWorld" using slicing
a="HelloWorld"
print(a[:5:1])

#2 slice and extract last 4 characters
b="PythonProgramming"
print(b[-4:])

#3 slice to get every second character starting from the first
c="abcdefg"
print(c[1::2])

#4 reverse the string 'Palindrome' using slicing
d='Palindrome'
print(d[::-1])

#5 Result of slicing operation s[3:] if s='DataScience'
s='DataScience'
print(s[3:])
#ans: aScience

#6 Extract every second character in revese order from the string
f='abcdefgh'
print(f[-2::-2])

#7 Extract 'Intelli' without slicing from 'ArtificialIntelligence'
g= 'ArtificialIntelligence'
print(g[10:17])

#8 str1='Hello' and str2= 'World',concatenate them to form a new string 'HelloWorld'
str1='Hello'
str2='World'
h=str1+str2
print(h)

#9 Extract the substring 'loWor' from the string str="HelloWorld" using slicing
str='HelloWorld'
print(str[3:8:1])

#10 Convert the string str="apple,banana,cherry" to a list of fruits
j= "apple,banana,cherry"
k=j.split(',')
print(k)

#11 a="my name is rita" use all method of string give
a="my name is rita"
b=a.upper()
print(b)
c=b.lower()
print(c)

a="mY name is rITA"
f=a.swapcase()
print(f)

a="my name is rita"
z=a.capitalize()
print(z)

s=a.count('a')
print(s)

t=a.find('r')
print(t)

v=a.replace('rita','apu')
print(v)

a=' my name is rita '
b=a.strip()
print(b)

a='mmy name is ritaa'
c=a.removeprefix('m')
print(c)
d=a.removesuffix('a')
print(d)

#12 assign the value 10 to a variable called x and print its value
x=10
print(x)

#13 Given three numbers x=12,y=15 and z=10, calculate and print their average
x=12
y=10
z=10
a=(x+y+z)/3
print(a)

#14 Given P,R and T, calculate the simple interest using the formula SI=(P*T*R)/100 and print the result
P=10000
R=10
T=12
SI=(P*T*R)/100
print(SI)

#15 Given two strings str1="Hello" and str2="World", concatenate them with a space in between and print the result(adding)
str1='Hello'
str2='World'
str= str1+' '+str2
print(str)

#16 Given a string str= 'PythonProgramming', find and print the length of the string
str='PythonProgramming'
s=len(str)
print(s)

#17 Given a string str='HelloWorld' extract and print the substring 'World' using slicing
str='HelloWorld'
print(str[5::1])

#18 Convert the string str='python' to uppercase and print the result.
str='python'
r=str.upper()
print(r)

#19 Convert the string str='PYTHON' to lowercase and print the result
str='PYTHON'
l=str.lower()
print(l)

#20 Reverse the string str='Python' and print the result
str='Python'
print(str[5::-1])








