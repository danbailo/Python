string = str(input("Enter the string:"))

string = string.casefold()

reverse_str = reversed(string)

if list(string)==list(reverse_str):
    print("It is a palindrome string")
else:
    print("No, it is not a palindrome string")