" write a program that takes a number as input and prints the some of its digits "
n = int(input("enter a number:"))
digits = 0
digit_sum = 0
temp = n  
while temp > 0:
    digit = temp % 10  
    digit_sum += digit  
    digits += 1         
    temp //= 10         
 
print(digits)
print(digit_sum)
