name = 'Kush'
age = 24

print('Hello World')
print('Welcome')

# Use age directly as int
print('My name is ' + name + ' and my age is',age)

# Convert int to string & print
print('My name is ' + name + ' and my age is ' + str(age))

# Escape sequence \
print('This is \'\\\' an escape Sequence')

# String as arr
print('Using string as array name[1] : '+ name[1])

# Convert to Uppercase
print('Converted to UpperCase : ' , name.upper())

# Convert to LowerCase
print('Converted to LowerCase : ' , name.lower())

# Check ifUpper
print('Check if Upper : ' , name.isupper())

# Check ifLower
print('Check if Lower : ' , name.islower())

# Lenght of 
print('Length of name is : ', len(name))

# Print Index of any letter
print('Print Index of letter U :', name.index('u'))

# Replace any letter
print('Replacing letter h with k :', name.replace('h','k'))

# Playing with numbers
print('We can perform arithematic operations 24 + 36 = ', 24 + 36)
