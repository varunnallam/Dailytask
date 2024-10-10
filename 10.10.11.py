"Create a list of numbers. Assign the list to another variable and modify the original list. Check if the second list also changes. Then, create a copy of the original list and show that modifying the copy does not affect the original list."
fruits = ["apple", "banana", "cherry", "date", "elderberry"]
print("Initial list:", fruits)
print("Reversed list using reverse():", fruits)
reversed_fruits = fruits[::-1]
print("Reversed list using slicing:", reversed_fruits)
