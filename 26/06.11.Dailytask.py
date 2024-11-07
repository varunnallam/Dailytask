##inheritance:
## >> it is an a parent to child class
 
## single:
# >>class inheriting from only one parent class
 
 
class p:
    def m1(self):
        print("this is instance method parent classes")
 
class c(p):
    def m2(self):
        print("this child class instace method")
 
c=c()
c.m1()
c.m2()
 
 
class teacher:
    def __init__(self):
        self.t_name=input("enter your t_name")
        self.t_subject=input("enter your subject:")
        print(self.t_name)
        print(self.t_subject)
 
class student(teacher):
    def s1(self):
        self.s_name=input("enter your s_name:")
        self.s_id=int(input("enter your id_num:"))
        self.s_marks=int(input("enter your math:"))
        print(self.s_name)
        print(self.s_marks)
        print(self.s_id)
 
s=student()
s.s1()
 
 
 
 
## multiple:
##         >>inheriting properties and methods from multiple classes to single class ot the same class
 
 
class f:
    def m1(self):
        self.nature="AMAZING"
 
class m:
    def m2(self):
        self.nature1="WORLD"
 
class c(m,f):
    def m3(self):
        print(self.nature)
        print(self.nature1)
 
c=c()
c.m1()
c.m2()
c.m3()
 
 
class shop1:
    def m1(self):
        self.product1=input("enter your product1 name:")
        self.p1_price=int(input("enter your p1_price:"))
 
class shop2:
    def m2(self):
        self.product2=input("enter your product1 name:")
        self.p2_price=int(input("enter your p2_price:"))
 
class S(shop1,shop2):
    def m3(self):
        print(self.product1)
        print(self.p1_price)
        print(self.product2)
        print(self.p2_price)
 
s=S()
s.m1()
s.m2()
s.m3()
 
 
 
## multilevel:
## >>inheriting properties and methods from multilevel classes to single class
 
 
class gf:
    def m1(self):
        self.land=5
 
class f(gf):
    def m2(self):
        print(self.land)
        self.land=100
 
class c(f):
    def m3(self):
        print(self.land)
        self.land=10
        print(self.land)
 
c=c()
c.m1()
c.m2()
c.m3()
 
 
class goverment:
    def m1(self):
        self.g_name_collage=input("enter your g_c_name:")
        self.g_fee_collage=int(input("enter your g_fee_collage:"))
 
class grade1_p_collage(goverment):
    def g1(self):
        self.g1_p_name_collage=input("enter your g1_p_name_collage:")
        self.g1_p_fee_collage=int(input("enter your g1_p_fee_collage:"))
 
class grade2(grade1_p_collage):
    def g2(self):
        self.g2_p_name_collage=input("enter your g2_p_name_collage:")
        self.g2_p_fee_collage=int(input("enter your g2_p_fee_collage:"))
 
g=grade2()
g.m1()
g.g1()
g.g2()      
 
 
 
 
## hyarchical:
##         >>inheriting properties and methods from single classes the multiple classes
#          >>single class to two child class
 
class p:
    def __init__(self):
        self.land=100
 
class c1(p):
    def m1(self):
        print("child_1",self.land-10)
 
class c2(p):
    def m2(self):
        print("child_2",self.land-10)
 
c1=c1()
c1.m1()
c2=c2()
c2.m2()        
 
 
class supermarket:
    def __init__(self):
        self.apples=int(input("enter no_of apples"))
        self.oranges=int(input("enter no_of oranges"))
 
class grades1(supermarket):
    def g1(self):
        self.apple=self.apples//3
        self.orange=self.oranges//4
        print(self.orange)
        print(self.apple)
 
class grades2(supermarket):
    def g2(self):
        self.apple=self.apples//2
        self.orange=self.oranges//5
        print(self.apple)
        print(self.orange)
 
g = grades1()
g.g1()
 
g2=grades2()
g2=g2()
 
 
 
 
## hybrid:
#         >> using more than one type of inheritance inside the class
 
class vehicle:
    def m1(self):
        print("this is vehicle class")
 
class bike(vehicle):
    def m2(self):
        print("this is a bike class")
 
class car(bike,vehicle):
    def m3(self):
        print("this is a car class")
 
b=bike()
b.m1()
b.m2()
 
 
c=car()
c.m1()
c.m2()
c.m3()
 
 
 
class filpkart:
    def m(self):
        self.order_no=int(input("enter order no:"))
        print(self.order_no)
 
class phone(filpkart):
    def m1(self):
        self.p_name=input("enter p_name:")
        self.p_price=int(input("enter p_price:"))
        print(self.p_name)
        print(self.p_price)
 
 
class book(phone,filpkart):
    def m3(self):
        self.b_name=input("enter book name:")
        self.b_price=int(input("enter book price:"))
        print(self.b_name)
        print(self.b_price)
 
b=book()
b.m()
b.m1()
b.m3()       