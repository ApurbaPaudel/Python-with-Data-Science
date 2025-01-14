#Conditional statement=making decision based on the value of variable

#syntax
#if condition: comparison or relational operator
    #block of code
#else:
    #block of code
a=67
if a>34:
    print('a is greater')
else:
    print('a is smaller')

a='welcome to our bus'
print(a.center(80,'*'))

age=int(input('enter your age'))
if age<=12:
    print('you have to pay Rs 20')
elif age<=18 and age>12:
    if age==16:
        print('no need to pay')
    else:
        print('You have to pay Rs 50')

else:
    print('You have to pay Rs 80')

#shorthand if, shorthand elseif
#shorthand if= else part navako
a=6
if a>3:print('a is greater')

#shorthand elseif=euta matra if euta matra else
a=6
b=4
print('a is greater') if a>b else print('a is smaller')




