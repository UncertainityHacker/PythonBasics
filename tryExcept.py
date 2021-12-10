try:
    x = int(input('Enter an Inteeger : '))
    print(x)
except: 
    print('Error')
else:
    print('If try block executes then else will be performed')
finally:
    print('When Both Try & Except finishs finally executes')