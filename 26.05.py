" write a program to check if is a string is palindrome "
n="madam"
rev=""
temp=n 
for i in n:
    rev=i+rev
if temp==rev:
    print("palindrome")
else:
    print("not palindrome")