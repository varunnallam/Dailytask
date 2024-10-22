###list
#1.Write a python program to merge two list?
 
l=[1,2,3,4,5,6]
l1=[7,8,9,10,11,12,15]
merge=l+l1
print(merge)
 
#output
#[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 15]
 
#2.Write a python program to delete element of given index in list ?
 
l=[1,2,3,4,5,6]
del l[0]
del l[4]
print(l)
# del keyword also remove the specifi index position
# removing >> pop() in these are taking that specfic index position
l.pop(1)
print(l)
 
#3.Write a pytho program to delete given element from the list?
l=[1,2,13,14,1,5,16]
l.remove(13)
print(l)
 
#output
#[1, 2, 14, 1, 5, 16]
 
#4.Write a python programe to check if the two list are having atleast one common element?
 
l=[1,2,3,4,5]
l1=[2,56,7,9]
common_element=set(l)&set(l1)
if common_element:
    print("it is having commo elements")
else:
    print("not present")  
 
#output
#it is having commo elements
 
# 5.  Write a python program to remove  specified column from the nestedlist?
 
l= [[1, 2, 3], [2, 4, 5], [1, 1, 1]]
del l[1][0:2+1]
del l[2][0:2+1]
print(l)
 
#output
#[[1, 2, 3], [], []]
 
 
#6.Write python program to convert a list of integers into single integer ?
 
l=[1,2,3,4,5]
s=""
for i in l:
   s+=str(i)
print(s)
 
#output
##12345
 
 # 7.Write  a python programe to remove duplicates from the list ?
l=[1,2,3,4,2,5,7,3,8,1]
s=set(l)
print(s)
l=list(s)
print(l)
 
#output
#{1, 2, 3, 4, 5, 7, 8}
#[1, 2, 3, 4, 5, 7, 8]
 
 
#set()
#1.Write a program to create a set.
s=(x for x in range(1,11))
print(s)
print(set(s))
 
#output
#<generator object <genexpr> at 0x00000196B02F8520>
#{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
 
#2.Write program to iterate over sets.
 
s={1,2,3,4,5}
for i in s:
    print(i)
 
#3.Write a Python program to add member to a set.
 
s={1,2,3,4,5}
s.add(56)
print(s)
 
#output
#{1, 2, 3, 4, 5, 56}
 
#4.Write a Python program to remove item from a given set.
 
s={1,2,3,4,5,6}
s.remove(4)
print(s)
#output
#{1, 2, 3, 5, 6}
 
#5.Write a python program to create a intersection of set ?
 
s={1,2,3,4,3,2}
s1={5,6,7,8,2,4,3}
print(s.intersection(s1))
 
#output
#{2, 3, 4}
 
#6.Write a python program to createa unionof set ?
 
s={1,2,3,4,5}
s1={6,7,8,9,2,4}
print(s.union(s1))
 
#output
#{1, 2, 3, 4, 5, 6, 7, 8, 9}
 
#7.Write a python program to create set differance ?
 
s={1,2,3,4,5}
s1={6,7,8,9,2,5}
print(s.difference(s1))
 
#output
#{1, 3, 4}
 
#8.Write a python program to create a symmetric defferance ?
 
s={1,4,5,6,7}
s1={2,7,9,10,2,5}
print(s.symmetric_difference(s1))
 
#output
#{1, 2, 4, 6, 9, 10}
 
#9.write a python program to find max and min values in a set?
 
s={0,1,2,3,4,5,6}
max_v=0
min_v=0
for i in s:
    if i>max_v:
        max_v=i
    if i<min_v:
        min_v=i    
print(max_v)
print(min_v)    
 
 
# 10.Given two Python sets, write a Python program to update the first set with items that
# exist only in the first set and not in the second set.
 
s={1,2,3,4,5}
s1={6,7,8,9,1,2,3,4}
s.difference_update(s1)
s.add(10)
print(s)
 
#output
#{10, 5}
 
#11.Write a Python program to remove items 10, 20, 30 from the following set at once.?
s={1,2,10,20,30}
s1={10,20,30}
print(s.difference(s1))  
 
#output
#{1, 2}
 
#12.Check if two sets have any elements in common. If yes, display the common elements?
 
s={1,2,3,4}
s1={1,2,3,4}
s2=s.intersection(s1)
if (s==s1):
    print("yes",s2)
 
#output
# yes {1, 2, 3, 4}    
 
 
#13.Update set1 by adding items from set2, except common items?
s={1,2,3,4,5}
s2={6,7,8,9,2,3}
print(s.symmetric_difference(s2))
 
#output
#{1, 4, 5, 6, 7, 8, 9}
 
 
#14.Remove items from set1 that are not common to both set1 and set2?
 
s={1,2,3,4}
s1={3,4,5,6,7}
print(s.difference(s1))
 
#output
#{1, 2}
 
 
##Tuple()
#1.How do you create a empty tuple on python
t=()
print(t)
print(type(t))
 
#2.Write a python program to unpack atuple into several variables ?
 
ft=("apple","orange","mango","banana","pineapple","custedapple")
a,b,c,d,e,f=ft
print(a,c)
print(b,d)
print(c,e)
print(f,e)
 
#output
##apple mango
#orange banana
#mango pineapple
#custedapple pineapple
 
#3.write a python program to add an item to the tuple ?
 
t=(1,2,3,4,5)
l=list(t)
l.append(6)
l.append(10)
print(l)
t=tuple(l)
print(t)
 
#output
#[1, 2, 3, 4, 5, 6, 10]
#(1, 2, 3, 4, 5, 6, 10)
#4.Write a python proram to convert tuple into a string ?
t=("Munna",1,2,43,33.3)
print(str(t))
 
#output
#('Munna', 1, 2, 43, 33.3)
 
#5.Write a python program to find most frequent element in tuple ?
t=(1,2,3,4,5,6,2,4,1,2)
most_frequent=0
max_count=0
for i in t:
    count=t.count(i)
    if count > max_count:
        most_frequent=i
print(most_frequent)        
     
 
 
## Dictinary:
 
#1.Write a python program to  add a key to a dictionary ?
 
dict={}
dict["name"]="Munna"
print(dict)
 
#ouput
#{'name': 'Munna'}
 
#2 Write a python program to check weather the given value is present in the dictionary or not ?
dict={"name":"Munna","age":25}
value="Munna"
if value in dict.values():
    print("yes")
else:
    print("no")    
 
 
#3 Write a Python script to print a dictionary where the keys are numbers between 1 and 15
# (both included) and the values are the square of the keys.
dict= {i:i**2 for i in range(1,15+1)}
print(dict)
 
#output
#{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100,
# 11: 121, 12: 144, 13: 169, 14: 196, 15: 225}
 
#Sample Dictionary
#{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121,
# 12: 144, 13: 169, 14: 196, 15: 225}
 
 
#4 Write a python program to create a dictionary from the string ?
 
s="Varun"
dict={}
for i in s:
    if i in dict:
        dict[i]=+1
    else:
        dict[i]=+1
print(dict)            
 
#output
#{'v': 1, 'a': 1, 'r': 1, 'u': 1, 'n': 1, 'n'}
 
# 5.Write a python program to combine two dictionaries by adding values of common keys ?

dict1 = {"a": 10, "b": 20, "c": 30}
dict2 = {"b": 40, "c": 50, "d": 60}

for key, value in dict2.items():
    if key in dict1:
        dict1[key] += value
    else:
        dict1[key] = value

print(dict1)
 
#6 Write a python program to merge two python dictionaries ?
 
dict={"name":"Munna"}
dict1={"age":25}
dict.update(dict1)
print(dict)
 
#output
#{'name': 'Munna', 'age': 25}
 
 
#7 Write a Python program to create a dictionary from a string.  
# : Track the count of the letters from the string.
#Sample string : 'skywavessoftwares'
 
s="skywavessoftwares"
dict={}
for i in s:
    if i in dict:
        dict[i]=dict[i]+1
    else:
        dict[i]=+1
print(dict)