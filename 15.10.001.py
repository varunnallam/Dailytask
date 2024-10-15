##tuple
## >> it is orderd collection of element and also immutable
#  >we cannot change the tuple elements
t=()
print(type(t))
t=(1,2,3,45,5)
print(t)
print(type(t))
 
 
t=tuple("Munna")
print(t)
 
#output
# ('M', 'u', 'n', 'n', 'a')
 
## we can also give the tuple element with the single element aslo
t=(20)
print(type(t))
 ## we get the int as an output
 ## so we have to use the comma in the end of the elememt
 
 
t=(20,)
print(type(t))
## here we get the ouput as tuple
 
## we can accesing element from tuple also
## here we can acces the elements by using of index and sciling aslo
 
 
t=(1,2,3,4,5,6,7,8,9)
print(t[2])  ## by using indexing
print(t[6])
print(t[3:6]) ## by using sciling
print(t[4:7])
 
#output
#3
#7
#(4, 5, 6)
#(5, 6, 7)
 
 
t=("Munna","Raju","Rama","Sita")
print(t[3])
print(t[2:3])
print(t[2:3+1])
 
##output
##sita
#('Rama',)
#('Rama', 'sita')
 
 
## and we can also take different data types in tuple()
t=("Munna",20,33.33,False,True,10,10)
## we can also use duplicate in the tuple
print(type(t))
print(t[4])
print(t[1:4])
 
#output
#True
#(20, 33.33, False)
 
## method in tuple
## >> count()
##        >> count is used for count the elements in
#               tuple
#   >> by using the count we can also find the higest
#          frequency of elementst
t=("Munna",20,33.33,False,True,20,30,True)
print(t.count(20))
print(t.count(True))
print(t.count(33.33))
 
## output
#2
#2
#1
#1
#4
 
## >> index()
 
t=("Munna",20,33.33,False,True,20,30,True)
print(t.index(20))
print(t.index(True))
 
#output
 # 1
 # 4
 
## we can also check the element is present in the tuple or not
t=(1,2,3,5,4,5,6,7,5,8)
print(t.count(5))
print(t.count(4))
 
## we can get the higest frequency of thge elements by using count()
 
 
#output
#3
#1
 
##operations of tuple :
# > we two operations in tuple addition and repetation
#addition
t=(1,2,3,4)
t1=(5,6,7,8)
print(t+t1)
## by using the additions operator we can the two tuples
#output
#(1, 2, 3, 4, 5, 6, 7, 8)
 
 
# repetation
t=("Munna","Ravi")
t1=("Shiva","ram")
print(t+t1)
print(t*2)
 
#output
#('Munna', 'Ravi', 'Shiva', 'ram')
#('Munna', 'Ravi', 'Munna', 'Ravi')
 
##nested tuple
 
t=(1,2,3,4,(5,6,7))
print(t[4][1])
print(t[2:4])
print(t[1:5])
 
#output
#6
#(3, 4)
#(2, 3, 4, (5, 6, 7))
 
## packing and unpacking of tuple elements
# packing >Packing a tuple means creating a tuple by
#               grouping multiple values together
p=(33.3,44.4,22.2,55.5,77.7)
(e,d,c,b,a)=p
print(a)
print(c)
print(e)
 
# unpacking>>Unpacking a tuple means extracting its values
#                into individual variables
 
#output
#77.7
#22.2
#33.3
 
## modifing pf tuple elements
# we can modify the tuple by using typecasting
 
t=("Munna",20,"Rama",30,101)
l=list(t)
print(l)
print(l.append(True))
print(l)
print(l.index("Munna"))
print(l.pop())
t=tuple(l)
print(t)
 
#output
#['Munna', 20, 'Rama', 30, 101]
#['Munna', 20, 'Rama', 30, 101, True]
#0
#True
#('Munna', 20, 'Rama', 30, 101)