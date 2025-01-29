#ABSTRACTION=data and methods hide
#abstract class: yo bhitra hunxa abstract method, declare hunxa but is not implemented
# from abc import ABC,abstractmethod #abc=module,ABC=abstract class
# class A(ABC):
#     @abstractmethod
#     def show(self): #concrete method
#         pass 
#     #declare matra vako yo mathi ko abstract banako
#     def display(self): #inference(interface) method
#         print('hello')
# class B(A):
#     def show(self):
#         print('hi')
#     def hello(self):
#         print('sipalaya')
# b=B.show()
# b.show()


#Exception handling: try,except,finally
# def show():
#     print(a) #yo error le aru tala ko code lai farak naparna exception handling
# show()

# print('hello')

#raise=reserved word(error raise garxa)
# a=int(input('Enter your number:'))
# if a<0:
#     raise ValueError('No negative number allowed')
# print(a)

#Error types:
#syntax error: code error
#runtime error: run garesi matra dekhini
#logical error: ans ma 6 chaiyexa but print(2+3) garney

#Runtime error types
#1 Name error:
# def show():
#     print (a)
# show() #a not defined

#2 TypeError:
# def show(a):
#     print(a)
# show() #formal arg dexa but actual arg dexaina

#3 ValueError:
# def show():
#     print(int('rita'))
# show() #type milena data ko so

#4 ZeroDivisionError:undefined
# def show():
#     print(4/0)
# show()

#5 Index Error
# def show():
#     a='rita'
#     print(a[8]) #8 index samma string nai xaina so error
# show()

#try=test a block of code
# try:
#     def show():
#         print (a)
#     show() #esma error xa ki nai test garxa try le
# except:
#     print('this is error') #try le test garera except ma msg dinxa
# print('hello') #mathi ko error le farak pardena because of exception handling

# try:
#     def show(a):
#         print(a)
#     show()
# except TypeError: #test garda typeerror vayo vane
#     print('this is TypeError')
# except ValueError:
#     print('This is value error')
# except IndexError:
#     print('this is index error')
# except:
#     print('other error')

#finally=it however executes any code
# def show():
#     print('hello')
#     return 2
#     print('hello')  #yo print hunna but finally use garesi hunxa

# def show():
#     try:
#         print('2'+2) #TypeError
#         print('hi')
#     except:
#         print('this is error')
#         return 'hello'
#     finally:
#         print('sipalaya')
# show()


#MODULE:file that stores function, variable, class
#two types: user defined, inbuilt

#Userdefined module:

