n=input("enter:")
print(n)

l=n.split() #convert string to list after space
print(l)

l=[]
for a in range(1,4):
    n=input("enter value"+ str(a) + ":" )
    l.append(n)
    print(l)