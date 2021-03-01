def type_2(function):
    def wrapper(obj):
        if isinstance(obj, type):
            print(f"{obj} is a {type(obj)}")
            print(f"As variables it has {vars(obj)}")
        elif not isinstance(obj, type):
            return function(obj)
        elif isinstance(obj, object):
            print(f"{obj} is a type object")
            print(f"{obj} is a {type(obj)}")
            print(f"As variables it has {vars(obj)}")

    return wrapper
