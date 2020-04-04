line = "Ra,da!?>r"
newLine = ""
if not line.isalpha():      # ISALPHA checks to see if the characters are in the alphabet
    for char in line:
        if char.isalpha():
            newLine += char

print(line)
print(newLine)

