countries = ['UK', 'USA', 'India', 'Australia', 4, True]

# Print Entire List
print(countries)

# Print desired Index
print(countries[2])

# Print mth element of nth item list[n][m]
print(countries[2][0])

# Print only desired range index [n:m] m is not included
print(countries[1:3])
print(countries[1:])
print(countries[:3])

# Print type of variable
print(type(countries))

# Replace item in list
countries[3] = 'China'
print(countries)

# Lenght of the List
print('Lenght of List : ', len(countries)) 

# Type of items in lists
print(type(countries[5]))

# List constructor
countries2 = list(('UK', 'USA', 'India', 'Australia', 4, True))

list1 = [1, 2, 3, 4, 5]
list2 = ['apple', 'banana', 'mango', 'orange']

# Add list2 to list1
list1.extend(list2)
list1.append('cherries')
list1.insert(6, 'cheeku')
list1.remove('banana')
print(list1)

# list1.clear()
# print(list1)

# index of item in list
print('Index of Mango in list2 : ', list2.index('mango'))

# Count number of times item appear in list
print('Number of times Mango appear in list2  : ', list2.count('mango'))

# Sort List
list3 = [5, 4, 45, 1, 2, 3, 4, 5]
list3.sort()
print(list3)

# Reverse list
list2.reverse()
print(list2)

# Duplicate List
list4 = list2.copy()
print('List2 Copy : ', list4)

# Remove last value from list
list4.pop()
print(list4)

# Delete value in list
del list4[0]
print(list4)

# Delete entire List
del list4
print(list4)