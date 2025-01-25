# 2 types 1.mutable = can change its state or contents  2. immutable = cant change

# mutable data type
# *list
# *dictionary
# *byte array



# immutable data type

# int
# float
# complex
# string 
# tuple
# set

#x = "Hello World"	                            str	
#x = 20	                                        int	
#x = 20.5	                                    float	
#x = 1j	                                       complex	
#x = ["apple", "banana", "cherry"]	           list	
#x = ("apple", "banana", "cherry")	           tuple	
#x = range(6)	                               range	
#x = {"name" : "John", "age" : 36}	           dictionary
#x = {"apple", "banana", "cherry"}	           set	
#x = frozenset({"apple", "banana", "cherry"})   frozenset	
#x = True	                                   bool	
#x = b"Hello"	                               bytes	
#x = bytearray(5)	                           bytearray	
#x = memoryview(bytes(5))	                   memoryview	
#x = None	                                   NoneType



                  # Number = int,Float,Complex nmber
a=5
print(a,type(a)) #int

a=5.5 
print(a,type(a)) #float

a=2+5j
print(a,type(a)) #complex

                 #string collection of one or more character(' '," ",""" """)

s ="this is string"
print(s,type(s))

s = """ this
 is string"""  #triple cout will display the output as written in any formate
print(s,type(s))
 
                    #List = list is an ordered sequence of items ( [] ) | most used datatype in py

l = [10,"a",5.5]
l[2]=10   #mutable
print(l,type(l))
            
                  #Tuple = is an ordered sequence of items as a list defined as = () |basic diffe is faster thn list and immutable
t=(10,"a",50) #if their is single value thn it is not a tuple
print(t,type(t))
  
                 #Dictionary = unordered key-value pair (key should b unique,value can b same) |mutable

d={
    'course' : 'python',
    'name' : 'vivek'
}  
print(d['course'])              
print(d,type(d))
                          
                #set = unordered collection of item.every set element is unique | immutable defined as = {}

s={1,2,1}
print(s,type(s))