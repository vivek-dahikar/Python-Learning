#sets = unordered| unindex | set()|{} | store unique element(eredicate the duplicate element)|cant iterate with index
s=(10,20,30,40)
print(s)

for a in s:
    print(a)
l=[10,20,30,40]
s=set(l)     #set()=change other deta type to sets
print(s) 

# add()         	Adds an element to the set
# clear()	        Removes all the elements from the set
# copy()	        Returns a copy of the set
# difference()	    Returns a set containing the difference between two or more sets
# difference_update()	Removes the items in this set that are also included in another, specified set
# discard()	            Remove the specified item
# intersection()	    Returns a set, that is the intersection of two or more sets
# intersection_update()	Removes the items in this set that are not present in other, specified set(s)
# isdisjoint()	        Returns whether two sets have a intersection or not
# issubset()	        Returns whether another set contains this set or not
# issuperset()	        Returns whether this set contains another set or not
# pop()	                Removes an element from the set
# remove()	            Removes the specified element
# symmetric_difference()	   Returns a set with the symmetric differences of two sets
# symmetric_difference_update()	inserts the symmetric differences from this set and another
# union()	                     Return a set containing the union of sets
# update()	                     Update the set with another set, or any other iterable