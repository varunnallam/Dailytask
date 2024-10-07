"Python program to remove repeated character from string"
s="nani"
s1=set()
r=[]
for i in s:
    if i not in s1:
        s1.add(i)
print(s1)    