from decorator import type_2


class A:
    a = 5


@type_2
def type_1(obj):
    return f"Type of {obj} is {type(obj)}"


value = int
b = 2
prueba = A()
obj = type('X', (object,), dict(a="Hello", b="World"))
print("Test for type(obj)==<class 'type'>:")
print(type_1(A))
print("Test for type(obj)!=<class 'type'>:")
print(type_1(b))
print("Test for type(obj) as an object:")
# For creating a new type object, obj is the name of the type object,  a must be a base and b must be a dictionary
print(type_1(obj))
