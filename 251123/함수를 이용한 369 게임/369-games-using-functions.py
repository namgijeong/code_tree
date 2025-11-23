a, b = map(int, input().split())

def include369(n):
    digit_10 = n//10
    digit_1 = n%10
    if digit_10%3 == 0 || digit_1%3 ==0:
        return True
    else:
        return False    

def count369(a,b):
    count = 0
    for i in range(a,b+1):
        if i%3 == 0 || include369(i):
            count += 1

    return count

print(count369(a,b))            