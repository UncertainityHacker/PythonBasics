# Stores data in form of key:Value pairs. They are mutable unlike tuples. Duplicates(keys) are not allowed, most recent value will be considered

my_dict = {
    'name' : 'Harry',
    'name' : 'Peter',
    'nationality':'Indian',
    'age':25,
    'friend': ['Rock', 'John', 'Code']
}

print(my_dict)

# Get Value of key
print(my_dict['name'])

# Len of dict
print(len(my_dict))

print(my_dict['friend'])