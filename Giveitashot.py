# Michael Suter
# Assignment 9 & 10 - checking to see if a string is the same reversable
# 3/31/20


print("Type your word to see if it is a palindrome")
string = input(">")


def palindrome_check(string):
    string = string.lower()
    string = string.strip()
    length = int(len(string))   # gets the number of characters in the string
    if length == 0 or length == 1:
        return print("This is a palindrome,", True)
    elif string[0] != string[-1]:
        return print("This is not a palindrome,", False)
    else:
        return palindrome_check(string[1:-1])


palindrome_check(string)

