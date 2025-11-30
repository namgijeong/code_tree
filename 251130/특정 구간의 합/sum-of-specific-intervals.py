n, m = map(int, input().split())
arr = list(map(int, input().split()))
queries = [tuple(map(int, input().split())) for _ in range(m)]

def sub_sum(part):
    sub_sum_number = 0;
    for i in range(part[0]-1, part[1]):
        sub_sum_number += arr[i]

    print(sub_sum_number)
    return    


def total_sum():
    big_sum_number = 0
    for i in range (m):
        sub_sum(queries[i])

    return


total_sum()