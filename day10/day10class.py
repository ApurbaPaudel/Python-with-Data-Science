# #atm machine
balance=20000
pin=1234
pin1=int(input('enter your pin'))
if pin==pin1:
    while True:
        print('Welcome to atm')
        print('1.Check balance')
        print('2.deposit')
        print('3.withdraw')
        print('4.exit')
        choice=int(input('enter your choice'))
        if choice==1:
            print(f'Your balace is {balance}')
        elif choice==2:
            amount=float(input('enter amount to deposit'))
            if amount>0:
                balance=balance+amount
                print('Your new amount is:',balance)
            else:
                print('Enter valid amount')
        elif choice==3:
            amount=float(input('enter your amount to withdraw'))
            if 0<amount<=balance:
                balance=balance-amount
                print('Your new balance is:',balance)
            elif amount > balance:
                print('Insufficient balance')
        elif choice==4:
            print('Thanks for visiting')
        break


#function=block of code that executes whenever it is called
#two types of function

#1 Inbuilt function/precoded/predefined
# print(),input(),len(),type(),sum(),set(),max(),min()

print(min([False,2,1,4,5,6])) #min value=false since false=0
print(max([-0.0,0.0])) #both are equal so suru ma vako lai max vanera aauxa output


#2 iser defined function
#syntax:
# def function_name():
    #block of codes
#function_name()

def show():
    print('hello')
show() #function call
# #function use: for code reusability, divides code into blocks

def display():
    a=4
    b=6
    print(a+b)
display()

# #using argument(parameter)
# def show(argument=formal arg):
#     #block
# show(argument=actual arg)
a=int(input('enter first number'))
b=int(input('enter second number')) #function baira lina parxa user bata input
def show(a,b):
    print(a+b)
show(3,4) #mathi nai user bata magyo vane yha ni a b lekhe hunxa natra chai actual number lekhni

#types of variable in function
#1 Local variable
#Function bhitra declare vako
#2 Global variable
#Function baira define vako

x='python' #global
def show():
    a='datascience' #local
    print(a)
print(x)
show()


