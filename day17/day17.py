#import from folder:
# from foldername.filename import function

#Inbuilt module:
#1 random
import random
a=random.choice(['apple','orange','pineapple']) #yo madhya euta dinxa
print (a)
b=random.randint(1,4) #yo bich ko euta number dinxa
print(b)
a=[1,2,3,4,5]
random.shuffle(a) #position shuffle garxa 
print(a)

#2 calendar
import calendar #given month ko sabai date aauxa
a=calendar.month(2025,2)
print(a)

#3 Keyword=reserve keyword haru list ko from ma dinxa
import keyword
a=keyword.kwlist
print(a)

#4 time: 
import time
a=time.ctime() #ctime=current time only
print(a)
b=time.localtime() #gives allll
print(b)

#5 datetime
import datetime
a=datetime.datetime.now()
print(a)

#6 math
import math
a=math.sqrt(36) #square root
print(a)
b=math.factorial(5)
print(b)
e=math.radians(30)
c=math.sin(e) #should be changed to radian
print(c)
d=math.cos(e)
print(d)
g=math.ceil(23.678) #decimal hatayera 1 step mathi ok value dinxa
print(g)
h=math.floor(45.78) #decimal hatauxa
print(h)

#or
from math import sqrt
a=sqrt(36)
print(a)

# from math import * #imports all methods of math

from math import sqrt as b #alising=method ko naam lengthy vako vara
a=b(36)
print(a)

#filehandling:
#file=collection of data
#two types of file: 
#binary file: machine readable (.mp3,.jpg,.png)
#text file: .txt,.csv (human readable)

#filehandling:operations performed on file like create, read, write, append
#1 opening the file
#2 operation=mode
#3 close (cache error nagarna)

#open file syntax:
# open('filename','mode')
# create=x,read=r,write=w,append=a
f=open('msg.txt','w')
# f=open('msg.txt','r')
# a=f.read(5) #reads acc to stated characters
# b=f.readline() #reads one line
# c=f.readlines() #reads all line in list form
# print(c)
print(f.write('i am from pkr')) #over write
# print(f.write('hello')) #append ma yha write lekhni mathi matra a lekhni over write hunna
f.close()




