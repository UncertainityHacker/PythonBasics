i = 0
while i<10:
    print(i)
    i+=1

while i>=0:
    print(i)
    i-=1

for letter in 'Hello':
    print(letter)

list1 = [21, 2, 3, 4, 5]

for num in list1:
    print(num)

my_dict = {
    'name' : 'Harry',
    'name' : 'Peter',
    'nationality':'Indian',
    'age':25,
    'friend': ['Rock', 'John', 'Code']
}

for key in my_dict:
    print(key)

for key,values in my_dict.items():
    print(key ,':', values)

for i in range(3):
    print(i)

for i in range(4,8):
    print(i)