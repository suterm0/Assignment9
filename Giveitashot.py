#Michael Suter
# Assignment 9 & 10 - checking to see if a string is the same reversable
#3/31/20

print("Type your word to see if it is a palindrome")
string = input(">")


def palindrome_check(string):
    string.strip()
    string.lower()
    reverse_string = ''.join(reversed(string))  # the '' serves as an empty space to make sure the string is being reversed with no additional characters
    if string == reverse_string:   # checks to see if the reversed string is the same as the normal string
        print(True, "This string is a palindrome")
    else:
        return False


if string == len(string) * string[0]:   # checks to see if the string is 1 character
    print(True)
elif string != len(string) * string[0]: # if it isnt equal to 1 character
    palindrome_check(string)
else:
    print(False)
    exit()

