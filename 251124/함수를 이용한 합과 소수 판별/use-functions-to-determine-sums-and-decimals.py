a, b = map(int, input().split())

def isSosu(n):
    for i in range(2,n):
        if n%i == 0:
            return False

    return True


def isDigitSumEven(n):
    mok =  n
    
    sum_n = 0
    while mok > 0:
        namage = mok%10
        mok = mok // 10      
        sum_n += namage  

    if sum_n % 2 == 0:
        return True
    else:
        return False


count = 0
for i in range(a, b+1):
    if isSosu(i) and isDigitSumEven(i):
    
        count += 1


print(count)