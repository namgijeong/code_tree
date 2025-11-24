a, b = map(int, input().split())

def isSosu(a,b):
    sum_n = 0

    for i in range(a, b+1):
        sosu_flag = True
        for j in range(2,i):
            if i%j == 0:
                sosu_flag = False
        if sosu_flag == True:
            sum_n += i        

    return sum_n

isSosu(a,b)                