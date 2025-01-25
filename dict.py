#dic = key value pair | linear data type | {} |  store like :
d={
    'name':'radhe',
    'loca':'barsana',
    'kartik':'2months'
}

print(type(d))
f=d['loca'] #accesing value by passing key
print(f)

for n in d:
    print(n) #return key
    print(d[n]) # return value


    #dictionary methods
# clear()	       Removes all the elements from the dictionary
# copy()	       Returns a copy of the dictionary
# fromkeys()	   Returns a dictionary with the specified keys and value
# get()	           Returns the value of the specified key
# items()    	   Returns a list containing a tuple for each key value pair
# keys()	       Returns a list containing the dictionary's keys
# pop()	           Removes the element with the specified key
# popitem()	       Removes the last inserted key-value pair
# setdefault()     Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
# update()	       Updates the dictionary with the specified key-value pairs
# values()	       Returns a list of all the values in the dictionary

d={
    'name':'radhe',
    'loca':'barsana',
    'kartik':'2months'
}

print(d.get('name'))  #Returns the value of the specified key

for a in d.keys(): #Returns keys
 print(a)

for a in d.values(): #Returns the value
  print(a)

for a,b in d.items(): #Returns both
  print(a,b)

d.update({'loca': "vrindavan"})
print(d)

d['loca']="nandgaon" #update if key is  already present
print(d)

d['krisha']="nandgaon" #insert if key is not already present
print(d)

d.clear()
print(d)

#nested dictionary = dict inside dict
 