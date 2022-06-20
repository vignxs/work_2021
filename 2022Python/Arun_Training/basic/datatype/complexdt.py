#list
from inspect import stack


a=[1 ,2 ,3]
print(len(a)) 
#adding element
a.append(4)
a.insert(1,5)
print(a)
#removal 
a.remove(1)
print(a)
#reverse
a.reverse()
print(a)
#indexing
a.index(3)
print(a)

#stack
stack =[6]
stack.append(8)
stack.insert(1,7)
print(stack)

#set
b = {1,3,3,5,7,9} #not support duplicate values
print(b)

