#integer
a=3
b=6
c=a+b
print(a+b)
print(c)

#float
d=2
e=2.0  #float value be like
print(a/2)
print(e+a)

#complex
f=3+5j
print(type(f))
#type conversion
g=float (5) #convert int to float
h=int (4.0) #convert float to int
print(g)
print(h)

#string 
i = 'arun'
j ="ran"
print(i,j)
#multiline string we can use 3quotes
k ='''hello guys, this is arun
from kallai. i have completed be cse.'''
print(k)
#upper and lower case
print(i.upper())
print(j.upper ())
print(i.lower())
print(j.lower ())
#relace string
print(k.replace("g", "J"))
#concadinate string
l = "Hello"
m= "World"
n = l + " " + m
print(n)
#formate string
age=27
tex= "im arun my age is {}"
print(tex.format(age))
quantity = 3
itemno = 34
price = 49
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))

#booleans
print(10 > 9)
print(10 == 9)
print(10 < 9)
o=345
p=456
if o>p :
   print("o is  greter than p")
else:
   print("o is not greter than p")



