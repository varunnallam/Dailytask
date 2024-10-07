"Python Program to check if two Strings are Anagram"
s="nani"
s1="nagu"
if set(s)==set(s1) and len(s)==len(s1):
    print("anagram")
else:
    print("not")