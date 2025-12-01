n = int(input())

def suyal(n):
    if n == 1:
        return 0

    if n%2 == 0:
        n = n/2
    else:
        n = n*3 + 1

    return 1 + suyal(n)        


print(suyal(n))    