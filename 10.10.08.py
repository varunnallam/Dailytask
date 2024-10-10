"Remove all occurrences of the number 3 from a list of integers."
numbers = [1, 2, 3, 4, 3, 5, 3, 6]
print("Initial list:", numbers)
numbers = [num for num in numbers if num != 3]
print("Updated list:", numbers)
