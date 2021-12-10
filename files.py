# r - read, w - write, a - append, r+ - read & write
file = open('test.txt','r')

print(file.readable())
print(file.readline())
print(file.readlines())

file.close()

file = open('test.txt','r')
for lines in file.readlines():
    print(lines)

file.close()

file = open('test.txt','w')

file.write('Hello World')

file.close()