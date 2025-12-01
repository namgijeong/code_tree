N = int(input())

def return_sum(n):
    if n == 0:
        return

    if n == 1:
        return 1

    next_sum = return_sum(n-1)
    return n + next_sum


print(return_sum(N))

