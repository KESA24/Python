# Strings in python, any text in the program
# Add a new line
print("Giraffe\nAcademy")

# Add a special character e.g quotes

print("Giraff\"Academy")

# String variables
phrase = "GiraffeAcademy"
print(phrase)

# Concatenation
phrase = "Giraffe Academy"
print(phrase + " is cool")

# Functions used with strings
print(phrase.lower())
print(phrase.isupper())
print(phrase.upper())

# Checking length
print(len(phrase))

# Return one character, python starts from 01234
print(phrase[0])
print(phrase[3])

# Index function
print(phrase.index("G"))
print(phrase.index("Academy"))

# Replace
print(phrase.replace("Giraffe", "Elephant"))
