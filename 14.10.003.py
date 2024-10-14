"Write a program to check if a string is a palindrome. A palindrome is a word, phrase, or sequence that reads the same forward and backward"
def is_palindrome(s):
    s = s.replace(" ", "")  # remove spaces
    s = s.lower()  # convert to lowercase
    return s == s[::-1]  # compare with reversed string

input_str = input("Enter a string: ")
if is_palindrome(input_str):
    print(input_str, "is a palindrome")
else:
    print(input_str, "is not a palindrome")
