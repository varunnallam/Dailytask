"Write a program that counts the number of even  numbers in a list"
def count_even(numbers):
    even_count = 0
    for num in numbers:
        if num % 2 == 0:
            even_count += 1
    return even_count

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_count = count_even(numbers)

print("Even numbers:", even_count)