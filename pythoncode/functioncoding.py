def func1():
    print("sample function 1")


func1()


def func2(a,b):
     c =  a + b
     return c

result = func2(10,20)
print(result)


def func3(*args):
    print(args)
    l1 = list(args)
    count = len(l1)
    print(l1)
    for i in l1:
        if i.isdigit():
            print(f"{i} is a number")
        else:
            print(f"{i} is a string")

        
func3("hello", "world", "123", "python", "456")

