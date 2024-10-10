"Write a Python program to demonstrate how changes in a list's alias affect both lists, while changes in a cloned list do not."
numbers = [1, 2, 3, 4, 5]
alias = numbers
numbers.append(6)
print( alias)
clone = numbers.copy()
clone.append(7)
print( numbers)
print( clone) 