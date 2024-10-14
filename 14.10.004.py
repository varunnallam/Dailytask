"Write a program that takes a number as input and prints the sum of its digits"
def sum_of_digits(n):
    sum = 0
    while n > 0:
        digit = n % 10
        sum += digit
        n = n // 10
    return sum

num = int(input("Enter a number: "))
print("Sum of digits:", sum_of_digits(num))
