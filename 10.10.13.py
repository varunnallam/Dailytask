"Write a Python program to demonstrate how changes in a list's alias affect both lists, while changes in a cloned list do not."
original_list = [1, 2, 3, 4, 5]
alias = original_list
clone = original_list.copy()
original_list.append(6)
print("Original List:", original_list)
print("Alias:", alias)
print("Clone:", clone)
alias.append(7)
alias.append(7)
print("Original List:", original_list)
print("Alias:", alias)
print("Clone:", clone)
clone.append(8)
print("Original List:", original_list)
print("Alias:", alias)
print("Clone:", clone)