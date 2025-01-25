#stack
# A stack is a linear data structure that stores items in a Last-In/First-Out (LIFO) or First-In/Last-Out (FILO) manner.
#  In stack, a new element is added at one end and an element is removed from that end only. 
# The insert and delete operations are often called push and pop.

# The functions associated with stack are:

# empty() –           Returns whether the stack is empty – Time Complexity: O(1)
# size() –            Returns the size of the stack – Time Complexity: O(1)
# top() / peek() –    Returns a reference to the topmost element of the stack – Time Complexity: O(1)
# push(a) –           Inserts the element ‘a’ at the top of the stack – Time Complexity: O(1)
# pop() –             Deletes the topmost element of the stack – Time Complexity: O(1)

# l=[]
# while True:
#     c=int(input('''
#           1 Push
#           2 pop
#           3 peek
#           4 display
#           5 exit

#             '''))
#     if c==1:
#         n=input("enter the value:-")
#         l.append(n)  #push
#         print(l)
#     elif c==2:
#         if len(l)==0:
#             print("empty list")
#         else:    
#             p=l.pop() #delete last element
#             print(p)
#             print(l)
#     elif c==3:
#         if len(l)==0:
#             print("empty list")   
#         else:
#             print("last value",l[-1])  #peek value
#     elif c==4:
#         print("display stack",l)
#     elif c==5:
#         break  #exit

#     else :
#         print("invalid opr")



#Queue
# Like stack, queue is a linear data structure that stores items in First In First Out (FIFO) manner.
# With a queue the least recently added item is removed first.
# A good example of queue is any queue of consumers for a resource where the consumer that came first is served first.


l=[]
while True:
    c=int(input('''
          1 Push element
          2 pop first element
          3 front element
          4 last element
          5 display queue
          6 exit element

            '''))
    if c==1:
        n=input("enter the value:-")
        l.append(n)  #push
        print(l)
    elif c==2:
        if len(l)==0:
            print("empty list")
        else:    
            del l[0]   #delete first element
            print(l)
    elif c==3:
        if len(l)==0:
            print("empty list")   
        else:
            print("first value",l[0])  #peek value
    elif c==4:
        if len(l)==0:
            print("empty list")  
        else:
            print("last",l[-1])
    elif c==5:
        print("display queue:",l)

    elif c==6:
        break
        
    else :
        print("invalid opr") #exit

