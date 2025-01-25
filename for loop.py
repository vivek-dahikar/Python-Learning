# for loop with range()
#range used for number
range(5) #range here condition is 5  |by default start point 0 | condition <5 (1 less thn value) | by default increament =1

range(1,6) #now by default start point 1 |  condition <6 | by default increament =1

range(1,6,2) # start = 1 |  condition <6 |  increament = 2

# for loop

for n in range(5): 
    print(n)

for n in range(1,6): 
    print(n)

for n in range(1,6,2): 
    print(n)

for n in range(1,11): 
    print("2*",n,"=",2*n)

# for reverse range (need to add 3 condition)

for n in range(10,0,-1):
    print(n)