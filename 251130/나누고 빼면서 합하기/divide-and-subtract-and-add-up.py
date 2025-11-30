n, m = map(int, input().split())
A = list(map(int, input().split()))

def find_number():
    global m
    global n
    global A
    sum_number = 0
    while m >= 1:
        #print(m)
        sum_number += A[m-1]
        if m%2 == 0:
            m = m // 2
        else:
            m -= 1

    return sum_number


print(find_number())
                

