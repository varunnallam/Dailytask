## variables in oop:
 
# types of variables:
## 1.instance variables:
##    >>declarations:
#          >>variable that changes from object to object
#          >>it is created by self keywords
#         >> we can create instance variables inside of constructor and instance method
#
#     >>accesing :
#         >>we can access instance variable class by using self keyword
#         >>we can access outside of the class  using ORV(object refrence variable)
#
 
class emp:
    def __init__(self):
        self.name="Varun"
        self.salary=20000
 
    def dispaly(self,age,id):
        self.age=age
        self.id=id
        print(self.name)
        print(self.salary)
       
 
e=emp()
e.dispaly(10,101)
print(e.name)
print(e.age)
 
 
 
 
class collage:
    def __init__(self,name,group,rollno,floorno,blockno):
        self.name=name
        self.branch="BSC"
        self.rollno=rollno
        self.floorno=floorno
        self.blockno=blockno
 
    def display(self):
        print(self.branch)
        print(self.name)
        print(self.rollno)
        print(self.floorno)
        print(self.blockno)
 
c=collage("Munna","BSC",734,10,15)
c.display()
 
c1=collage("Varun","Mscs",734,10,15)
c1.display()
 
 
 
 
class Boy:
    def __init__(self,name,age):
        self.name=name
        self.age=age
 
    def c(self):
        print(self.name)
        print(self.age)
 
c1=Boy("Kanna",1.0)
c1.c()
c2=Boy("Munna",2.4)
c2.c()        
 
 
 
 
#static variable:
#   >>declaration:
#        >>in static variable is not changing object to object
#       >>we can declare a static variable inside the class directly
#       >>inside the constructor ,instance methode using classname
#       >>outside of class using class name
#       >>inside the class methose using class variable
#
#    >>accessing :
#         >>using class name we can access inside the constructor and instance method
#         >>outside of a class using classname and ORV
#         >>inside of the class method using class variable
#  
#
 
class collage:
    collagename="DNR collage"  ##we can declare a static variable inside the class directly
    def __init__(self,name,branch,rollno):
       
        self.name=name
        self.rollno=rollno
       
        collage.branch="Bsc"  
       
        print(collage.branch) 
   
    def d(self):
        collage.section="section c"
        print(self.name)
        print(self.rollno)
       
 
s=collage("Munna","BSC",734)
print(collage.collagename)
 
collage.age=22   
s.d()  
print(collage.age)  
 
 
 
 
 
class dog:
    dogbread="Dabourman"
    def __init__(self,name,age):
        self.name=name
        self.age=age
        dog.legs="4 legs"
 
    def c(self):
        dog.eyes="2 eyes"
        print(self.name)
        print(self.age)
s=dog("Roxy",5.5)
s.c()
print(dog.dogbread)
print(dog.legs)
print(dog.eyes)
 
 