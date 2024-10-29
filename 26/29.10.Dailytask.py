
#1.Define a function called `greet` that takes a name as an argument and prints a
# greeting message like: "Hello, [name]!"
 
def greet(name):
    return(["Hello, " + name + "!"])
name=["Varun"]
print(greet(" ".join(name)))
 
 
 
#2.Write a function `add_numbers` that takes two numbers as arguments and returns their sum.
# Test the function by passing different numbers.
 
def add_number(a,b):
    return a+b
 
print(add_number(73,24))
print(add_number(33,55))
 
 
 
#3.Create a function `is_even` that takes a number as an argument and returns
# `True` if the number is even, and `False` otherwise.
 
def is_even(n):
    if n%2==0:
        return True
    else:
        return False
 
print(is_even(10))            
 
 
#4.Write a function `factorial` that takes a positive integer as input and returns the
# factorial of that number. Remember, `factorial(5)` should return \(5 \times 4 \times 3
# \times 2 \times 1 = 120\).
 
def factorial(n):
    if n==0:
        return 1
    else:
        return(n*factorial(n-1))
 
print(factorial(5))        
       
       
 
 
 
#5.Define a function `find_max` that takes three numbers as input and returns the largest of the three.
#  Test the function with various sets of numbers.
 
 
def find_max(a,b,c):
    if a>b and a>c:
        return ("a is greathan b,c")
    elif b>c and b>a:
        return("b is greathan a,c")
    else:
        return ("c is greathan a,b")
 
print(find_max(1,3,6))
print(find_max(3,5,10))
 
 
 
 
#6.Write a function `count_vowels` that takes a string as input and returns the
# number of vowels (a, e, i, o, u) in the string.
 
def count_vowels(s):
    v = "aeiou"
    count = 0
    for i in s:
        if i in v:
            count += 1  
    return count
 
 
print(count_vowels("Bhimavaram"))  
 
 
 
 
 
#7.Create a function `is_prime` that takes a number as input and returns
# `True` if the number is prime, and `False` otherwise.
 
def is_prime(n):
    if n <= 1:
        return False  
    c = 0
    for i in range(2, n):
        if n % i == 0:
            c += 1    
    return c == 0  
         
print(is_prime(3))
print(is_prime(11))
print(is_prime(9))
print(is_prime(33))
 
 
 
 
 
 
 
 
#8.Write a recursive function `recursive_sum` that takes a positive integer `n` and
# returns the sum of all numbers from 1 to `n`. For example, `recursive_sum(5)`
# should return \(1 + 2 + 3 + 4 + 5 = 15\).
 
def recursive_sum(n):
    sum=0
    for i in range(1,n+1):
        sum=sum+i
    return sum
 
print(recursive_sum(5)) 
 

 
 
 
 
#9.Write a function `calculator` that takes three parameters:
# two numbers and an operator (as a string: `"+"`, `"-"`, `"*"`, `"/"`).
# The function should perform the operation on the two numbers and return the result.
 
 
def calculator(s,s1,s3):
    if s3=="+":
        return s+s1
    elif s3=="-":
        return s-s1
    elif s3=="*":
        return s*s1
    elif s3=="/":
        return s/s1
   
print(calculator("Munna","Kanna","+"))
print(calculator(4,9,"-"))  
print(calculator(3,7,"*"))
print(calculator(6,9,"/"))  
 
 
 
       
#10.Write a function `find_common_elements` that takes two lists as input and
# returns a list of elements that are present in both lists.
 
def find_common_elements(l,l1):
    l3=set(l).intersection(set(l1))
    return l3
l=[1,2,3,4,5]
l1=[2,4,1,6,7]
print(find_common_elements(l,l1))
 
 
 
 
#11.Write a function `reverse_string` that takes a string as input and returns the string reversed.
 
def reverse_string(s):
    s1=s[::-1]
    return s1
print(reverse_string("Munna"))
 
 
 
 
 
 
#12.Write a function `sort_dict_by_value` that takes a dictionary as input and returns a
# list of tuples sorted by the dictionary values in ascending order.
 
 
def sort_dict_by_value(d):
    s=sorted(d.items(), key=lambda item: item[1])
    return s
d={"m":25,"p":15,"c":50,"s":45}
print(sort_dict_by_value(d)) 
 
 