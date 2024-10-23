##buit_in function:
#    >>function prefrom a wide range of task such as datatype conversions it called built_in functions
##   >> built-in functions to find the length of a string or list without using len()
 
## "len(),max(),min(),print(),count(),int(),sum(),float(),type(),round(),str()
#       input(),all(),sorted()"
 
# without using the len() function find the lenght of list or set
 
l=[1,4,7,9,10,4,6,7,9]
 
#by using sum()  
ts = 0  
for i in l:
    ts += i  
print(ts)  
print(sum(l))
 
#by using round()
##    > nearest interger or specified number of decimal palce
 
print(round(1.34576878,2))
 
#by using len()
l1=0
for i in l:
    l1+=1
print(l1)
print(len(l))
 
#by using max()
max_num=0
for i in l:
    if i>max_num:
        max_num=i
print(max_num)
print(max(l))
 
# by using min()
min_num=0
for i in l:
    if i<min_num:
        min_num=i
print(min_num)
print(min(l))
 
 
## customised function:
#    > we can define your own function by using def keyword
#   >> it also called as structured of defining a custom function
#
#   >> "map,reduce,filter,lambda,recursive"
 
## Recursive
#    >> the fuction that call by itself
def factorial(x):
    if x<0:
        return x
    fact=1
    for i in range(1,x+1):
        fact*=i
    return fact
print(factorial(4))
 
 
##all even number
def even(l):
    l2=[]
    for i in l:
        if i%2==0:
            l2.append(i)
    return l2        
           
l=[1,4,7,9,10,4,6,7,9]
print(even(l))  
 
## all odd numbers
 
def odd(l):
    l2=[]
    for i in l:
        if i%2==1:
            l2.append(i)
    return l2        
           
l=[1,4,7,9,10,4,6,7,9]
print(odd(l))
 
 
# lambda
#   >> Lambda functions in Python are small
#    >>easy to read
#   >>  itcan take any number of arguments but can only have one expression
# syntax
    #  >> lamdba argument : expression
 
l=lambda a:a/a
print(l(8))
 
##   >> in single line we can pass more arguments
 
l=lambda a,b: a/b
print(l(2,8))
 
 
l=lambda a,b: a if a<b else b
print(l(2,8))
 
 
## filter
## >> filter() function is used to filter elements from an iterable
#    >>base on a function that evaluates to True or False
##   >> it will filter the function  and check the sequence of the list
## syantax
#  >> filter(function,sequence)
 
def get_odd(l):
    if l%2==1:
        return True
    else:
        return False
l=[2,5,8,1,9,10,33,66,99]            
s=filter(get_odd,l)
print(list(s))
 
 
 
## map()
##     >> map function based on the given condition every time it will return the new list
#   syantx
#  map(function,sequency)
 
 
l=[2,4,6,8,10]
def sqr(l):
    return l*2
m=map(sqr,l)
print(list(m))    
 
 
 
def add(a,b):
    return a+b
 
a=[12]
b=[34]
m=map(add,a,b)    
print(list(m))
 
## map function by using lambda
num= range(5)  
d= map(lambda x: x * 2, num)
print(list(d))