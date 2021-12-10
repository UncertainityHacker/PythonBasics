a = 2
b = 3

if a<b :
    print(b, ' is greater than ',a)
elif a>b:
    print(a,'is grater than equal to ',b)
else :
    print('a is equal to b')

a='Tim'
b='Tim'

if a>b or a<b :
    print('a is not equal to b')
else :
    print('a is equal to b')

# Divisibility check
num = int(input('Enter a number to check divisibility by 3: '))
if num%3==0:
    print('It is Divisible by 3')
else:
    print('Not Divisible by 3')