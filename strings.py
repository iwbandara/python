# Working with Strings in Python

word = '   hello world !!!'

print(word)

# Remove whitespace from str
word = word.strip()

# Capitalize first letter of the first word
word = word.capitalize()

print(word)

# Capitalize first letter of each word
word = word.title()

print(word)

# Alternatively can combine all above methods to a single line
word =  '   hello world !!!'.strip().title()

print(word)

# Split a string 

name = input('Type your first name and last name')

first, last = name.split(' ')

print(f'Hello, {first}')
