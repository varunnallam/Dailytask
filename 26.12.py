"write a program that counts the number even and odd number in list" 
n = [22,55,77,99,100,11,33,55]
even_count = 0
even_number=[]
odd_count = 0
odd_number=[]
for i in n:
    if i % 2 == 0:
        even_number.append(i)
        even_count += 1  
    else:
        odd_number.append(i)
        odd_count += 1
print(even_count)
print(even_number)
print(odd_number)
print(odd_count)