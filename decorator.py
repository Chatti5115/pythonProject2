def decoarg(arg):
    print(f"decoarg: {arg}")
    def decofunc(func):
        def wrapper(*args, **kwargs):
            print(f"wragpper: {arg}")
            decovalue = func(*args, **kwargs)
            print(decovalue * 5)
        return wrapper
    return decofunc

@decoarg("deco arg")
def demo(arg1):
    return arg1

print(demo(3))