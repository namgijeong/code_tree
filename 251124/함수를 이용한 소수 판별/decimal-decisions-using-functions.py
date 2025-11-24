a, b = map(int, input().split())

def isSosu(a,b):
    sum_n = 0

    for i in range(a, b+1):
        for j in range(2,i):
            if i%j == 0:
                sum_n = i

    return sum_n

isSosu(a,b)                