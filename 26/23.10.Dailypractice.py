# functions
# Types of arguments
 
# 1.positional arguments
##   >> positional arguments are values you pass to a function
##   >> the first argument goes to the first parameter and the second to the second parameter
##  >> it will the value based on the postion of given arguments
 
def sum(a,b):
    print(a)
    print(b)
    print(a*b)
sum(2,4)
 
def sum(b,a):
    print(a)
    print(b)
    print(a*b)
 
sum(2,4)  
 
## based on the given postion the arguments will be taken
 
def name (name1,name2):
    print(name1)
    print(name2)
    return (name1+name2)
print(name("Munna ","Kanna"))
 
 
def name (name2,name1,name3):
    print(name1)
    print(name2)
    print(name3)
    return (name1+name2+name3)
print(name("Munna ","Naga ","Kanna"))
 
 
 
#keyword arguments:
#    >>Keyword arguments lets us to pass values to a function using the parameter names
##  >> paramter="value"
 
def greet(name,msg):
    print(name,msg)
greet(name="Munna",msg="Happy Birthday")
 
 
def greet(msg,name):
    print(name,msg)
greet(name="Munna",msg="Happy Birthday")
 
# because we assigined the parameter to the value so if we change the
## def parameter also no problem
 
 
def add(a,b):
    print(a)
    print(b)
    return (a+b)
print(add(a=80,b=9))
 
def add(b,a):
    print(a)
    print(b)
    return (a+b)
print(add(a=80,b=9))
 
 
## variable lenght arguments:
##   >Variable length arguments allow you to pass a variable number of arguments to a function
 
def factorial(*n):
    f = []
    for i in n:
        if i < 0:
            return i  
        fact = 1
        for i in range(1,i+1):
            fact *= i
            f.append(fact)
    return f
 
print(factorial(2, 4, 5))
 
 
 
## variable keyword length arguments:
##     >> it will store in the from of dictinary
#Variable keyword arguments allow you to pass a variable number of keyword arguments to a function
# it will store the elemnts in the key value pari
 
def vegetables(**l):
    for k,v in l.items():
        print(k,"-",v)
    print(sum(l.values()))
 
vegetables(carrot=45,beetroot=50,cucumber=30,onion=70,tamota=60)
 
 
## default arguments:
# Default arguments allow you to specify default values for function parameters
 
"""def append_to(a,l=None):
    l=[]
    if l is None:
        l.append(a)
    return l
print(a.append_to(1))
print(a.append_to(2))
print(a.append_to(3))
print(a.append_to(4)) """  
 
def append_to(a, l=None):
    if l is None:
        l = []
    l.append(a)  
    return l
l1=[]
print(append_to(1,l1))  
print(append_to(2,l1))  
print(append_to(3,l1))  
print(append_to(4,l1))  