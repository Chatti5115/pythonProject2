def sumAllPointer(*list):
    return sum(list)

example = [1,2,3,4,5]
print(sumAllPointer(*example))

print(sumAllPointer(1,2,3,4,5))

def dicPointer1(**dic):
    for key, value in dic.items():
        print(f"{key} : {value}")

dic1 = {'a':1, 'b':2, 'c':3}
print(dicPointer1(**dic1))

def dicPointer2(**dic):
    for key, value in dic :
        print(f"{key} : {value}")
dicPointer2(a1=10)
print(dicPointer2(b1 = 10, b2=20, b3=49))