#mutable | declare in square brac [] | comma seperated multiple value |

l=[1,2,3,"radhe"]
#slicing list
print(l[3],l[1])
print(l[0:4]) #start from 0 index and it will run till 4 | return list
print(l[0::2]) #start from 0 index and increament :: meant it will run till end
print(l[0:1:2]) #it will run till 1 index
print(l[1:]) #start to end
print(l[-1:]) #reverse (increament start from 0 but in reverse start for -1)
print(l[-1::-1]) #reverse with decreament | need to pass 3 argument for decreament

 #iteration
 #same as string

#list comprehension : List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.

#first using append
l=[]
for a in range(1,100):
    l.append(a)
    print(l)
#list comprehension
n=[m for m in range (1,100) if m%2==0 ] #shorter way | if m%2==0 (filter)
print(n)

#list function
# append()	    Adds an element at the end of the list
# clear()	    Removes all the elements from the list
# copy()	    Returns a copy of the list
# count()	    Returns the number of elements with the specified value
# extend()	    Add the elements of a list (or any iterable), to the end of the current list
# index()	    Returns the index of the first element with the specified value
# insert()	    Adds an element at the specified position
# pop()	        Removes the element at the specified position
# remove()	    Removes the first item with the specified value
# reverse()	    Reverses the order of the list
# sort()	    Sorts the list

# del pop remove clear update insert appends extends

l=[10,20,30,50]

del(l[1]) #delete on basis of index no
print()

print(l.pop(2)) #delete on basis of index no and also return which value is deleted
print()

l.remove(30) #delete on basis of value
print()

l.clear() #blank the list
print()

y=[10,20,30,50]
y[1]=90  #update on basis of index
print(y)

y.insert(0,20) # 0 is index and 20 is value
print(y) #insert value in index and tht previous index increases

y.append(20) # 20 is value
print(y) #insert value in last position

y=[10,20,30,50]
n=[50,60] #add new list using append with data type
y.append(n) # 20 is value
print(y) #insert value in last position

y=[10,20,30,50]
n=[50,60] #add new list using extend | add value not data type
y.extend(n) # 20 is value
print(y) #insert value in last position

#count max min sort reverse index
e=[10,20,50,10,10]

c=e.count(10) # times of element is used here #3
print(c)

c=max(e) # max value
print(c)
c=min(e)  # min value
print(c)

f=["hello","world"]
c=max(f) # tells max value in character acc. to alpha.
print(c)

g=[10,20,30,10] #sort = setting value in a way
g.sort()
print(g)


#iterating 2+ list at same time

#zip function
l=[10,20,30,40]
l1=[1,2,3,4]
for a,b in zip(l,l1): #ele. of l will go to a and l1 will go to b | helps to iterate 2 list but it will not take the elem. which is more in any of the list
  print(a,b)

l=[10,20,30,40]
l1=[1,2,3,4]

t=len(l)

for h in range(t):
    print(l[h],l1[h]) #h is index