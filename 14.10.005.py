"Python Program to check if two Strings are Anagram"
def are_anagrams(str1, str2):
    # Remove spaces and convert to lowercase
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()

    # Check if sorted strings are equal
    return sorted(str1) == sorted(str2)

str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

if are_anagrams(str1, str2):
    print("The strings are anagrams")
else:
    print("The strings are not anagrams")