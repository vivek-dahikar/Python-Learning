w="hare krishna" #indexing | space also contain index
print(w[6])
print(w[-2])

w="hare krishna" #slicing
print(w[0:7])
print(w[0:7]) 
print(w[0::2]) # 2 increament 

print(w[-1::-2]) # starting from left 2 is increament value

print(w[-1::-1]) # reversing -1 is increament value

# string iteration 

w="radhe shyam"
w=w[-1::-1] #reverse by overighting
t=len(w) #12..last index is 11
print(t)
for a in range(t):
    print(w[a])

b="hare krishna"
t=len(b) #12..last index is 11
print(t)
for a in range(t-1,-1,-1): #t-1 = loop will start from 11 | -1 it willl run till 0 | -1 increament
    print(b[a])

w="welcome to barsana"
for a in w:
    print(a)

    # string function | All string methods returns new values. They do not change the original string.

w="welcome to Barsana"
n=w.lower() #lower
n=w.upper() #upper
n=w.title() #first letter capital of each word
n=w.capitalize() #first letter capital pf first word

print(n)
#find
x="my vrindvan"
v=x.find('vr')  #return index number of first letter he got
v=x.find('v',4) #giving range tht it will check the value from index 4
v=x.find('z',4) # it will return -1 if it will not find the given value
print(v)

#index

c="hari bol"
print(c.index('b',2))  #difference bw index is find tht if value is not present thn it will return error and find will return -1

#isalpha : give true and false if their is letter true and digit thn false

d="radhakrund12"
print(d.isalpha()) # even thier shouldnt be space
print(d.isdigit()) # checks digit
print(d.isalnum()) # checks both al and digit

             #chr() and ord() fucn
#chr() take integer value as argument and gives chracter as string
#ord() vice versa
#    :- The range of ASCII values for uppercase letters A-Z is 65-90, and the range for lowercase letters a-z is 97-122.

a=66
print(chr(a)) #return ASCII value

y='A'
print(ord(y)) #return ASCII value 
                     
 #formating :The format() method formats the specified value(s) and insert them inside the string's placeholder.The placeholder is defined using curly brackets: {}

e="welcome {} to {} gokul".format("hello",20) #value stored in curly brac
print(e)

f="welcome {0} to {1} gokul".format("hello",20) # set hellp in 0 set 1 in 20
print(f)

f="welcome {1} to {0} gokul".format("hello",20) # set hellp in 1 set 0 in 20 (prints accord. to index)
print(f)

f="welcome {a} to {b} gokul".format(a=10,b=20) # set with assigning
print(f)

f="welcome {a:10} to {b} gokul".format(a=10,b=20) # set 10 character space(sets space of character in left)
print(f)

#|for left space > | for right space < | for both side space ^
f="welcome {a:^10} to {b} gokul".format(a=10,b=20) # set 10 character space in left and right (^)
print(f)

f="welcome {a:<10} to {b} gokul".format(a=10,b=20) # set 10 character space in right and right (>) 
print(f)