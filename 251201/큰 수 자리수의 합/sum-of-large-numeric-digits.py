a, b, c = map(int, input().split())

def multiple(a,b,c):
    return a*b*c


def recursive_sum(n):
    if n < 10:
        return n

    return n%10 + recursive_sum(n //10)


def digit_sum(a,b,c):
    total_number = multiple(a,b,c)

    return recursive_sum(total_number)


print(digit_sum(a,b,c))   