" write a program to check if a number is a Armstrong number "
n = int(input("enter a number:"))
num=n
s=0
while n>0:
    r=n%10
    s=s+r*r*r
    n=n//10
if s==num:
        print(num," Armstrong number")
else:
        print(num, "Not an Armstrong")