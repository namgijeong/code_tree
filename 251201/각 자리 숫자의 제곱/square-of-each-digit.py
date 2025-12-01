N = int(input())

def multiple_sum(n):
    if n < 10 :
        return (n % 10)*(n % 10)

    return (n % 10)*(n % 10) + multiple_sum(n // 10)


print(multiple_sum(N))    