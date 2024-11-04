#Instance method:
# >we can declaring and accessing a instance variable inside a method
# >while declaring instance method have to pass self as an first paramater
# >we can acces thses instance method using orv or classname
 
 
###instance method:
 
class colours:
    def __init__(self,red,orange,pink):
        self.red=red
        self.orange=orange
        self.pink=pink
 
    def m(self,totalprice):
        self.totalprice=totalprice
        print(self.red)
        print(self.orange)
        print(self.pink)  
        print(self.totalprice)
 
f=colours(2,2,2)
f.m(200)  
 
 
class cat:
    def __init__(self,name,age):
 
        self.name=name
        self.age=age
 
    def m(self,bread):
        self.bread=bread
        print(self.name)
        print(self.age)
        print(self.bread)  
 
d=[]
m1=int(input("enter a number of:")) 
for i in range(m1):
    name=input("enter a name:")
    age=int(input("enter a age:"))
 
    cat=cat(name,age)
    d.append(cat)
 
for cat in d:
    cat.m("snooze")      
 
 
 
class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
 
    def wish(self):
        print(self.name)
        print(self.age)
 
    def introduce(self):
        self.wish()
        print("Nice to meet you")
 
person= person("Munna", 23)
person.introduce()
 
 
 
 
 
 
#class method:
#  >inside the class method have  to use only static variable
# >while declaring class method have to pass @class method
# >while declaring class method have to pass cls as first parameter
# > using cls keyword we can declare and can access the data in side class method
 
class dog:
    totalprice=2000
    @classmethod
    def m(cls,dabour,labour,husky):
        cls.shopname="varmas"
        print(dabour)
        print(labour)
        print(husky)
        print(dog.totalprice)
        print(cls.shopname)
 
p=dog()
p.m(3,2,4)              
 
 
 
class college:
    branch="Bsc"
    @classmethod
    def m(cls,name,rollno):
        cls.collagename="DNR"
        print(name)
        print(rollno)
        print(cls.branch)
        print(cls.collagename)
 
c=college
c.m ("Munna",734)      
 
 
class Mobilestore:
    price=20000
    @classmethod
    def m(cls,name,rating):
        cls.companyname="Satya"
        print(name)
        print(rating)
        print(cls.companyname)
        print(cls.price)
 
f=Mobilestore()
f.m("Iphone","15")
 
 
 
##static method:
#  >>we are not using instance and static variable
#  >we are not passing any paramter like self or cls
# >we have to pass @staticmethod decorate
# >we can access static method using class anem and cls variable
       
 
class add:
    @staticmethod  
    def m():
        a=5
        b=8
        print(a+b)
   
a1=add()
a1.m()
 
 
 
class college:
    @staticmethod
    def m():
        name="Munna"
        age=23
        phone_no=6527899678
        roll_no=846
        return name,age,phone_no,roll_no
 
b=college()
print(b.m())    
 
 
 
class fruits:
    @staticmethod
    def m():
        apple=2
        banana=3
        orange=4
        dragon=5
        totaliteams=apple+banana+orange+dragon
 
        return totaliteams
v=fruits()
print(v.m())

 

 
 

