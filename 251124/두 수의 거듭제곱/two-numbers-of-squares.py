a, b = map(int, input().split())

def multiply(a,b):
    mul = 1
    for i in range(1,b+1):
        mul *= a

    return mul    

print(multiply(a,b))    