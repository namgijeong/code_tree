N = int(input())

def suyal(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2

    return suyal(n//3) + suyal(n-1)   


print(suyal(N))