#operators
#Arithmetic opertors
x=5
y=2
print(x+y)
print(x-y)
print(x*y)
print(x/y)
print(int(x/y))
print(x**y)
print(x//y)

#Assignment  Operators
x=5
x=x+3
print(x)
x+=3
print(x)
x-=3
print(x)
x/=3 
print(x)

#Compafison operators
x=5
y=3
print(x==y)
print(x!=y)
print(x>y)
print(x<y)
print(x>=y)
print(x<=y)

#Logic Opertor
x=10
y=5
print(x>9 and y>5)
print(x>9 and y>8)

#identity Operator
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x
# y=x
print(x is z)
# returns True because z is the same object as x
print(x is y)
# returns False because x is not the same object as y, even if they have the same content
print(x == y)
# to demonstrate the difference betweeen "is" and "==": this comparison returns True because x is equal to y

x = ["apple", "banana"]
y = ["apple", "banana"]
z = x
print(x is not z)
# returns False because z is the same object as x
print(x is not y)
# returns True because x is not the same object as y, even if they have the same content
print(x != y)
# to demonstrate the difference betweeen "is not" and "!=": this comparison returns False because x is equal to y

#Membership operator
x = ["bala", "arun"]
print("arun" in x)
# returns True because a sequence with the value "banana" is in the list
print("Shanmugam" not in x)
