class My_class1:
    x=5
print(My_class1)

class MyClass2:
    x=10
obj1=MyClass2()
print(obj1.x) #object.property

"""init fucntion"""
class Person:
    def __init__(obj1,name,age,city):
        obj1.name = name
        obj1.age = age
        obj1.city = city
        
p1=Person("Aditi",30,"Dehradun")
p2=Person("Aditya",31,"Delhi")

print(p1.name)
print(p1.age) 
print(p1.city)

print(p2.name)
print(p2.age)
print(p2.city)

"""Object Passing"""

class Person:
    def __init__(obj2,name,age): #Assignment of values for functions
        obj2.name=name
        obj2.age=age
    def myfunc(obj2):
        print("Hello my name is :"+obj2.name)
        print("His age is :",obj2.age)
p1 = Person("Shreyansh",17)

p1.myfunc()
        
