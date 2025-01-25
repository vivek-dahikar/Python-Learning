#ARITHMATIC
#+	Addition	x + y	
#-	Subtraction	x - y	
#*	Multiplication	x * y	
#/	Division	x / y	
#%	Modulus	x % y	(for reminder)
#**	Exponentiation	x ** y 	print(5**3)= 5*3 5*3 5*3 
#//	Floor division	x // y give integer..it will remove value after decimal

a = 10
b = 27

print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b)
print(a**b)
print(a//b)
print(10/3)
print(10//3) 

# ASSINMENT OPERATOR

# =	x   = 5	         x = 5	
# +=	x += 3	     x = x + 3	
# -=	x -= 3	     x = x - 3	
# *=	x *= 3	     x = x * 3	
# /=	x /= 3	     x = x / 3	
# %=	x %= 3	     x = x % 3	
# //=	x //= 3	     x = x // 3	
# **=	x **= 3	     x = x ** 3	
# &=	x &= 3	     x = x & 3	
# |=	x |= 3	     x = x | 3	
# ^=	x ^= 3	     x = x ^ 3	
# >>=	x >>= 3	     x = x >> 3	
# <<=	x <<= 3	     x = x << 

# some example
x=5
print(x)

x=x+5
print(x)

x+=5
print(x)

x-=5
print(x)

#comparison 

#==	Equal	x == y	
#!=	Not equal	x != y	
#>	Greater than	x > y	
#<	Less than	x < y	
#>=	Greater than or equal to	x >= y	
#<=	Less than or equal to	x <= y


#logical 
# and 	Returns True if both statements are true	x < 5 and  x < 10	
# or	Returns True if one of the statements is true	x < 5 or x < 4	
# not	Reverse the result, returns False if the result is true	not (x < 5 and x < 10)

x=10
y=20

print(x==10 and x<y and x==y) # each value shld be true
print(x==10 and x<y and x==y) # any value shld be true
print (not x!=10) # not revert the condition..if it true it will makeit false vice versa


# MEMBERSHIP (MOST USABLE)

# in 	    Returns True if a sequence with the specified value is present in the object	    x in y	
# not in	Returns True if a sequence with the specified value is not present in the object	x not in y

string1="hello world"
print('H' in string1) #false (case sensitive)
print('h' in string1) #true
print('v' in string1) #true

l=[10,20,30]
print(50 in l) #true
print(50 not in l) #false

#IDENTITY OPERATOR 

#is 	    Returns true if both variables are the same object	     x is y	 
#is not	    Returns true if both variables are not the same object	 x is not y

X=20
Y=20
print(x)
print(y)


print(X is y,x==y)
print(X is not y,x==y)

#bitwise 

# & 	AND	       Sets each bit to 1 if both bits are 1
# |	    OR	       Sets each bit to 1 if one of two bits is 1
#  ^	XOR	       Sets each bit to 1 if only one of two bits is 1
# ~ 	NOT    	   Inverts all the bits
# <<	Zero       fill left shift	Shift left by pushing zeros in from the right and let the leftmost bits fall off
# >>	Signed     right shift	Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off
