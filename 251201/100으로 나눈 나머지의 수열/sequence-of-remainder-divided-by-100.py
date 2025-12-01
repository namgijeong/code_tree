N = int(input())

def suyal(n):
    if n == 1:
        return 2
    elif n == 2:
        return 4

    return (suyal(n-1)*suyal(n-2))%100


print(suyal(N))        
