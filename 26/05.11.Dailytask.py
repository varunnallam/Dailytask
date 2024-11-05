#All variables and methods:
 
class ATM:
    ATMname="IDFC"  ##static variable
    def __init__(self,name):
        self.name=name       ## instnace variable
 
    def m1(self,branch):
        self.branch=branch   ## instance variable
        print(self.name)
        print(self,branch)
 
    @classmethod
    def m2(cls):
        cls.acc_no=23656732467   # static variable
        print(cls.acc_no)
    @staticmethod
    def m3() :
        ph_no=82455677542      ##local variable  
        print(ph_no)
 
b=ATM("munna")
print(b.ATMname)
b.m1("jntu")
b.m2()
b.m3()
 
 
 
class fruits:
    fruitsname="varmas"
    def __init__(self,trees):
        self.trees=trees
 
    def s1(self,totaltrees):
        self.totaltrees=totaltrees
        print(self.trees)
        print(self.totaltrees)
 
   
    @classmethod
    def s2(cls):
        cls.total_mango_tree = 20  
        print(cls.total_mango_tree)  
 
   
    @staticmethod
    def s3():
        total_orange_trees=30
        print(total_orange_trees)        
 
 
g=fruits("Rare fruits")
g.s1(150)
g.s2()
g.s3()
 
 
 
 
#nested classes:
#  > the class inside the class
#  >The nested class can be accessed only through the outer class
#  >Nested classes are typically used when the inner class is relevant only to the outer class
 
class outerside:
    def __init__(self):
        print("outerclass constructor")
    def display(self):
        print("outer class instance method")
    class innerclass:
        def __init__(self):
            print("innerclass constructor")
        def display(self):
            print("innerclass instance method")
 
    i=innerclass()
    i.display()
         
 
o=outerside()
o.display()
i=o.innerclass()
i.display()  
 
 
 
##nested classes
 
class employe:
    def __init__(self, name):
        self.name = name
        self.employement = self.employement()  
        self.department = self.department()  
 
    def s1(self, id):
        self.id = id
        print( self.name)
        print(self.id)
 
    class employement:
        def __init__(self):  
            self.salary = 30000
 
        def s2(self):
            print(self.salary)
 
    class department:
        def __init__(self):  
            self.dep = "HR"
 
        def s3(self):
            print(self.dep)
 
e = employe("MUNNA")
e.s1(10)  
e.employement.s2()  
e.department.s3()
 
 
class tickets:
    def __init__(self,name):
        self.name=name
        self.startingloc=self.startingloc()
        self.endingloc=self.endingloc()
 
    def s1(self,price):
        self.price=price
        print(self.name)
        print(self.price)
 
    class startingloc:
        def __init__(self):
            self.s_location="JNTU"
            self.s_station="JNTU_station"
 
        def s2(self):
            print(self.s_location)
            print(self.s_station)
 
    class endingloc:
        def __init__(self):
            self.e_location="hyderabad"  
            self.e_station="KPHB_station"
 
        def s3(self):
            print(self.e_location)
            print(self.e_station)  
 
t=tickets("MUNNA")                      
t.s1(55)
t.startingloc.s2()
t.endingloc.s3()
