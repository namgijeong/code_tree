n, m = map(int, input().split())

# Please write your code here.
def max_yaksu(n,m):
    if n>m:
        result = n%m
    else:
        result = m%n    

    if result == 0:
        result = m
    print(result)

max_yaksu(n,m)    