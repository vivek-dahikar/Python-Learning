#simple fucn
# fucn with argument
# return type

def myfucn():
    print("welcome")
myfucn()


def mysum(a,b):
    print(a+b)

mysum(20,10)

def mysum(a,b=1):  #default arg
    print(a+b)

mysum(20)
mysum(20,10) #overight


#return value

def square(x):
    return x*x
s=square(5)   #need to return print
print(s)

#multiple return value
def square(x):
    return x*x,x*2
s=square(5)   #need to return print
print(s)