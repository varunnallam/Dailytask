"Write a program that prints the multiplication table for a given number"
def print_multiplication_table(n):
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")

num = int(input("Enter a number: "))
print_multiplication_table(num)