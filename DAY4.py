##  how to check if something belongs to some class or not 

p = isinstance(10,float)
print(p)

q = isinstance(5.787,int)
print(q)

r = isinstance("ant" , str)
print(r)

s = isinstance("35698.9a", str)
print(s)

##  operations :-

a= 3+4
print("the value of a is " , 3+4)
print("the sum of 3 and 4 is " , 3+4)
b = 3-4
print("The value of b is" , 3-4)
print("the difference os 3 and 4 is ", 3-4)
c=3*4
print("the value of c is " , 3*4)
print("the product of 3 and 4 is " , 3*4)
d= 28/4
print("the value of d is " , 28/4)
print("the quotient when 28 is divided by 4 is", 28/4)
e= 36/5
f = isinstance(e , int)
print(f) ## false
h = 36//5 ## // gives the remainder
i=isinstance(h,int)
print(i)
a ="mango "+" banana" ## for no space btw the two words in otput , just don't put spaces.
print(a)
b = "mango"+"banana"
print(b)
c = "abcabc"*6## writes the things that many times as we want.
print(c)

#  comparison operators (they give the values either as true or as false )


a  = (13 >7)
print(a)
b= (13<6)
print(b)
c = (13>=5)
print(c)
d = (13<=8)
print(d)
e =(7==7)
print(e)
f =(6==7)
print(f)
g = (10!=11)
print(g)

## for strings :- basically which comes in the dictionary first 

## empty strings are falsy while the ones havimg something are truthy

h = "ab"<"a"
print(h) # gives false
h = "ab"=="ab"
print(h) ## true