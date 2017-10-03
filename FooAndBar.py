import sys

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
for i in range (0, 100001):
    sys.stdout.write(str(i) + ": ")
    if i == squNum:
        print("Bar")
        squNum += squAdd
        squAdd += 2
    elif primeTest(i):
        print("Foo")
    else:
        print("FooBar")