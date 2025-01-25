# In Python, we sometimes need to save the object on the disk for later use. This can be done by using Python pickle
# The Pickle dump() and dumps() functions are used to serialize an object. The only difference between them is that dump() writes the data to a file, while dumps() represents it as a byte object. 

# Similarly, load() reads pickled objects from a file, whereas loads() deserializes them from a bytes-like object.

#dumb

import pickle

l=[10,20,30,40]
file=open("writeDETA.txt","wb")  #wb = write binary
pickle.dump(l,file)  #dumb=store data

file.close()

file=open("writeDETA.txt","rb")  #read binary
l=pickle.load(file) #load the store data

print(l)

