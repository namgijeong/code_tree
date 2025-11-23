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

# def max_yaksu(n,m):
#     gcd = 1
#     try = min(n,m) + 1
#     for i in range(1, try):
#         if n%i == 0 and m%i == 0:
#             gcd = i

#     print(gcd)

# max_yaksu(n,m)    

# 변수 선언 및 입력:
n, m = tuple(map(int, input().split()))


# n과 m의 최대공약수를 반환합니다.
def find_gcd(n, m):
    gcd = 0
    for i in range(1, min(n, m) + 1):
        if n % i == 0 and m % i == 0:
            gcd = i

    print(gcd)


find_gcd(n, m)
