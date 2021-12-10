def foo():
    print('Hello World')

foo()

# Passing the variables when amount is not known
def foo1(*names):
    print('Welcome ' + names[1])
    
foo1('John', 'Tim', 'Harry')