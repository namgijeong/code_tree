n, m = map(int, input().split())

# Please write your code here.
try_range = min(n,m) + 1

max_yaksu = 0
for i in range(1,try_range):
    if n%i == 0 and m%i==0:
        max_yaksu = i

min_baesu = n*m/max_yaksu

print(int(min_baesu))