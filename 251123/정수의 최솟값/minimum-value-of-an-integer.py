a, b, c = map(int, input().split())

def min_number(a,b,c):
    min_n = a
    if min_n > b:
        min_n = b

    if min_n > c:
        min_n = c

    return min_n   

print(min_number(a,b,c))