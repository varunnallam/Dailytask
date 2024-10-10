"Write a Python program that initializes a list with some numbers and:"
l=[l for l in range(1,10+1)]
print(l)
l.append(11)
print(l)
l.insert(2,12)
print(l)
l1=[l1 for l1 in range (1,13+1)]
print(l1)
l.extend(l1)
print(l)