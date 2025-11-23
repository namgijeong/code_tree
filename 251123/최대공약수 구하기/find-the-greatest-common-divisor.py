n, m = map(int, input().split())

# Please write your code here.
# def max_yaksu(n,m):
#     if n>m:
#         result = n%m
#     else:
#         result = m%n    

#     if result == 0:
#         result = m
#     print(result)

def max_yaksu(n,m):
    gcd = 1
    count_try = min(n,m) + 1
    for i in range(1, count_try):
        if n%i == 0 and m%i == 0:
            gcd = i

    print(gcd)

max_yaksu(n,m)    


