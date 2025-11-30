a, b = map(int, input().split())

def print_number(a,b):
    if a > b:
        b = b+10
        a = a*2
    else:
        b = b*2
        a = a+10
        
    return a,b

a,b = print_number(a,b)
print(a,b)         
