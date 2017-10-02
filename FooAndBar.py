def primeTest(x):
    if(x % 2 == 0):
        return False
    for i in range(3, x//2, 2):
        if x % i == 0:
            return False
    return True

print("Prime/Square number checker")
print()
squNum = 100
squAdd = 21
i = 100
while i <= 100000:
    print(i, ": ", end="")
    if i == squNum:
        print("Bar")
        squNum += squAdd
        squAdd += 2
    elif primeTest(i):
        print("Foo")
    else:
        print("FooBar")
    i += 1