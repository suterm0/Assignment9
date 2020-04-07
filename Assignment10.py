# Michael Suter
# Assignment 9 & 10 - checking to see if a string is the same reversable
# 3/31/20


def choice():
    answer = int(input("1 to check for a palindrome, 2 to exit!>"))
    while answer != 1 and 2:
        choice()
    if answer == 1:
        punc_string = input("enter your string>")
        return punc_string
    else:
        if answer == 2:
            exit()


def punctuation_check(punc_string):
    string = ''
    if not punc_string.isalpha():
        for char in punc_string:
            if char.isalpha():
                string += char
        print(string)
        return string
    else:
        string = punc_string
        return string


def palindrome_check(string):
    string = string.lower()
    length = int(len(string))   # gets the number of characters in the string
    if length == 0 or length == 1:
        return print("This is a palindrome,", True)
    elif string[0] != string[-1]:  # if first [0] and last letter [`]are not the same then its not a palindrome
        return print("This is not a palindrome,", False)
    else:
        return palindrome_check(string[1:-1])


# You need to get the input from the user in a loop so it can happen multiple times

print("Type your word to see if it is a palindrome")
punctuations = ''' !/?@#$;,()-[]{}<>./%^:'"&*_~ '''
 
    
# Your punctuation check returns a value
i = choice()
value = punctuation_check(i)
result = palindrome_check(value)
print(result)
