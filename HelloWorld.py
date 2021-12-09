from math import *

print('Hello World')
print('Welcome')

name = input('Input Your Name : ')
age = int(input('Enter Your Age : '))

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

# Check if Upper
print('Check if Upper : ' , name.isupper())

# Check if Lower
print('Check if Lower : ' , name.islower())

# Lenght of 
print('Length of name is : ', len(name))

# Print Index of any letter
print('Print Index of letter U :', name.index('u'))

# Replace any letter
print('Replacing letter h with k :', name.replace('h','k'))

# Playing with numbers
print('We can perform arithematic operations 24 + 36 = ', 24 + 36)

# Get Absolute value
print('Absolute value of -5 : ', abs(-5))

# Print Max and Min
num = (4,5,7,54,2)
print(num)
print('Max : ', max(num), '\nMin : ', min(num))

# Round
print('Round 3.2 : ' , round(3.2))

# Binary of a number
print('Binary of 2 : ', bin(2))

# imported functions from math
print('Square root of 100 : ', sqrt(100))