a, b = map(int, input().split())

def include369(n):
    mok = n
    namage = 0
    while mok !=0 :
        namage = n%10
        mok = mok // 10
        if namage%3 ==0:
            return True

    return False    
      

def count369(a,b):
    count = 0
    for i in range(a,b+1):
        if i%3 == 0 or include369(i):
            count += 1

    return count

print(count369(a,b))            