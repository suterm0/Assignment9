# Michael Suter
# Assignment 9 & 10 - checking to see if a string is the same reversable
# 3/31/20


def punctuation_check(punc_string):
    string = ''
    if not punc_string.isalpha():
        for char in punc_string:
            if char.isalpha():
                string += char
        print(string)
        return string
    #The method was returning nothing in the string was already alpha, so fixed that
    return punc_string

def palindrome_check(string):
    string = string.lower()
    length = int(len(string))   # gets the number of characters in the string
    if length == 0 or length == 1:
        return print("This is a palindrome,", True)
    elif string[0] != string[-1]:  # if first [0] and last letter [`]are not the same then its not a palindrome
        return print("This is not a palindrome,", False)
    else:
        return palindrome_check(string[1:-1]))

# You need to get the input from the user in a loop so it can happen multiple times    
print("Type your word to see if it is a palindrome")
punc_string = input(">")
punctuations = ''' !/?@#$;,()-[]{}<>./%^:'"&*_~ '''
 
    
# Your punctuation check returns a value
value = punctuation_check(punc_string)
result = palindrome_check(value)
print(result)
