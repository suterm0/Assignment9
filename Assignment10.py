# Michael Suter
# Assignment 9 & 10 - checking to see if a string is the same reversable
# 3/31/20

print("Type your word to see if it is a palindrome")
punctuations = ''' !/?@#$;,()-[]{}<>./%^:'"&*_~ '''

def choice():
    answer = input("1 to check if palindrome, 2 to exit.>")
    while answer != 1 or 2:
        choice()
    if answer == 1:
        punc_string = input("Enter your word>")
        return punc_string
    else:
        if answer == 2:
            exit()


def punctuation_check(punc_string):
    string = ''
    if punc_string.isalpha():
        for char in punc_string:
            string += char
            return palindrome_check(string)
    if not punc_string.isalpha():
        for char in punc_string:
            if char.isalpha():
                string += char
        print(string)
        return palindrome_check(string)


def palindrome_check(string):
    string = string.lower()
    length = int(len(string))   # gets the number of characters in the string
    if length <= 1:
        return print(True, "This is a palindrome")
    elif string[0] != string[-1]:  # if first [0] and last letter [`]are not the same then its not a palindrome
        return print(False, "This is a palindrome")
    else:
        return palindrome_check(string)



punctuation_check()

