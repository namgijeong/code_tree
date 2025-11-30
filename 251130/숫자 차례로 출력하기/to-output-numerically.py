n = int(input())

def print_n(n):
    if n == 0:
        return
    print_n(n-1)
    print(n, end=" ")


def print_n_reverse(n):
    if n == 0:
        return
    print(n, end=" ")
    print_n_reverse(n-1)


print_n(n)
print()
print_n_reverse(n)        