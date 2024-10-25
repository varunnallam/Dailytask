# Modules:
##      >> collections of variables annd class and functions
#   function  is a block of reuseble ccode excecutes whenever we call the function
##      >> each and every .py extension file are know as modules
 
##   >>customised modules
#    >builtin modules
 
## builtin modules:
#     >> math,datatime,random,fonktools
 
 
# datatime modules:
#    >the datetime module in Python is a powerful and flexible tool for working with dates and times.
 
import datetime
print(dir(datetime))
 
##output
#['MAXYEAR', 'MINYEAR', 'UTC', '__all__', '__builtins__', '__cached__', '__doc__',
# '__file__', '__loader__', '__name__', '__package__', '__spec__', 'date', 'datetime',
# 'datetime_CAPI', 'sys', 'time', 'timedelta', 'timezone', 'tzinfo']
 
from datetime import date
import datetime
 
print(date.today())
 
##>>it represents a date (year, month, day)
 
print(datetime.datetime.now())
 
##>>it represents a time (hour, minute, second, microsecond)
 
 
## random modules:
###      >> The random module in Python is used for generating random numbers and
#                >performing random selections
 
import random
print(dir(random))
 
#output
##  >_floor, _sqrt, random , randrange, _ceil , randint , choice,choices,exp
 
from random import random
import random
for i in range (1,10):
    print(random.random())   
 
for i in range (1,10):
    print(random.randint(200,500))   #it will generator random number based on between the given sequence
 
for i in range (1,10):
    print(random.randrange(300,700))  #it will generator random numbers in the given range
 
print("------")  
 
 
## choice
#   >>it will choose random interger in the given range
##  >> expects a sequence (like a list or tuple)
 
for i in range(1,10):
    print(random.choice(range(1,100)))
 
## choices
# > the  function is used to select multiple random numbers from a sequence,
#     >>and it returns a list of those random numbers
   
for i in range(1,10):
    print(random.choices(range(1,100)))
 
 
 ## gauss:
#  >The random.gauss() function generates random numbers based on a Gaussian distribution.
#     >The first argument is the mean, and the second argument is the standard deviation.
for i in range (1,10):
    print(random.gauss(300,700))
 
 
# math
## >> the math module in Python provides a number of mathematical functions
 
import math
 
print(dir(math))
 
 
# floor:
#    >> it will return the lower nearest interger in the given element
 
print(math.floor(22.95))
def add(a,b):
    return a+b
 
l=add(20.8,23.67)
print(math.floor(l))
 
print("------")
## ceil
## >> it will return the upper nearest interger in the given elment
 
print(math.ceil(22.95))
 
 
def add(a,b):
    return a+b
 
l=add(20.8,23.67)
print(math.ceil(l))
 
 
##pow:
## >> it is used to raise a number to a specified power
 
print(math.pow(22.95,78))
 
# fsum():
#  >  it is function is used for sum of a sequence of numbers
#  > and we have to take it as list from
 
r=math.fsum([1,3,6,8,9])
print(r)
 
#gamma
#     >> it will given the factorial function of the elements
print(math.gamma(20))
 
 
print(math.factorial(10))
 
 
print(math.sqrt(6))