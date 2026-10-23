
def is_palindrome(s):
    return s == s[::-1]

input_name= input("Enter your name : ")

if is_palindrome(input_name ):
    print("Palindrome")
else:
    print("Not a palindrome")
