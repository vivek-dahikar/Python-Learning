# In Python, object-oriented Programming (OOPs) is a programming paradigm that uses objects and classes in programming. It aims to implement real-world entities like inheritance, polymorphisms, encapsulation, etc. in the programming. The main concept of OOPs is to bind the data and the functions that work on that together as a single unit so that no other part of the code can access this data.

# OOPs Concepts in Python
# Class
# Objects
# Polymorphism
# Encapsulation
# Inheritance
# Data Abstraction

#no space classnaeme|camel case

class DemoClass:
    a=10
    
    def sumvalue(self): #need to put 1 arg. if we creates func inside a class | creating methods(method is same like fucn)
        print(20+30)
    
demoobject=DemoClass()  #object
demo=DemoClass() #can create multiple objetct in single class | object creates outside of class
demoobject.sumvalue() #calling fucn ithrough object
print(demo.a)
print(demoobject.a)


#self and passing arg
class MyDemo:
    a=80
    def myvalue(self): #cant create a variable or cant use it without self
        # print(self.a)
        self.c=self.a*self.a
        print(self.c)

    def myvalue1(self,a,b):
        print(a+b)

obj=MyDemo()
obj.myvalue()
obj.myvalue1(20,30)


#constructor = main diff. is tht we need to call method bt dont need to call constructor
class MyCont:
    a=10
    def __init__(self):  #in it keyword to create constructor
        print("welcome to barsana")
       
obj=MyCont()   #no need to call constructor weit auto get call on creating obj.


#inheritance
# Inheritance allows us to define a class that inherits all the methods and properties from another class. 
# Parent class is the class being inherited from, also called base class.
#  Child class is the class that inherits from another class, also called derived class.

#single inheritance :-

class A:
    def display(self): #can use any variable of this class using self
        print("welcome to barsana")

class B(A):                                          #calling a class in B
    def displayB(self):
        print("welcome to vvn") 

class C(B):                           #a inside b and b inside c so its MULTIPLE INHERITANCE
    def displayc(self):
        print("welcome to gokul")
        

    
obj=C()
obj.display()
obj.displayB()
obj.displayc()


class x:
    def display(self): 
        print("welcome to barsana")

class y:                                          
    def displayB(self):
        print("welcome to vvn") 

class Z(x,y):                                   #multilevel inheritance
    def displayc(self):
        print("welcome to gokul")
    
obj=Z()
obj.display()
obj.displayB()
obj.displayc()


#encapsulation (getter setter)
class Student:
    def __init__(self):
        self._name=""
    def getname(self):
        return self._name
    def setname(self,name):
        self._name=name

obj=Student()
obj.setname("vivek")
name=obj.getname()
print(name)


# Encapsulation is used to restrict access to methods and variables. In encapsulation, code and data are wrapped together within a single unit from being modified by accident.
# Encapsulation is a mechanism of wrapping the data (variables) and code acting on the data (methods) together as a single unit.
# In encapsulation, the variables of a class will be hidden from other classes, and can be accessed only through the methods of their current class.

class School:
    __name="radhe" #private variable using _ _ |
    def __init__(self):
        print(self.__name)  #can use inside class but cant accesible outside
        self.__displayinfo() #calling private method
    def __displayinfo(self):  #private function
        print("welcpme to barsana")


obj=School()
# print(obj.__name) #not accesible bcz of private 



# Polymorphism  
# The word polymorphism means having many forms. In programming, polymorphism means the same function name (but different signatures) being used for different types. 
# The key difference is the data types and number of arguments used in function.

#exam
l=[10,20,30,40]
print(len(l))
s="welcome"
print(len(s))

# Polymorphism ; overloading = same fucn but different output on the basis of parametere

class Vvn:
    def displayin(self,age=''):
        print("welcome to barsana"+ age)

obj=Vvn()
obj.displayin()
obj.displayin('my age')

# Polymorphism ; overiding = child overighting same fucn of parent

class Gokul:
    def displayin(self):
        print("welcome to barsana")
        
class Mathura(Gokul): #inheritance
    def displayin(self):
        super().displayin() #super fucn for calling same fucn of parent
        print("welcome to vvn")    
obj=Mathura()
obj.displayin()




