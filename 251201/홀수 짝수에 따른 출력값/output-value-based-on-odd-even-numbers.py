N = int(input())

def print_sum(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2


    if n % 2 == 0:
        return n + print_sum(n-2)

    else:
        return n + print_sum(n-2)    


print(print_sum(N))      