# Classes in python

class myClass():
    def  __init__(self, name, age):
        self.name = name
        self.age = age

p1 = myClass('John',25)
print(p1.age)
print(p1.name)

del(p1.name)
p1.name = 'Morty'

print(p1.name)

# Inheritance

class person():
    name = 'Rick'
    age = 22

class student(person):
    pass

p2 = student()
print(p2.name)