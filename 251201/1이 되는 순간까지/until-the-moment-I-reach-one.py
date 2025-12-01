N = int(input())

def reply_count(n):
    if n == 1:
        return 0

    if n % 2 == 0:
        n = n / 2
    else:
        n = n // 3    

    # count = 0
    # count += 1
    return 1 + reply_count(n)    


print(reply_count(N))
