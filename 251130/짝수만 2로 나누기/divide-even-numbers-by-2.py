n = int(input())
arr = list(map(int, input().split()))

def print_number(n, arr):
    for i in range(n):
        if arr[i] % 2 == 0:
            print(arr[i]//2 , end=" ")
        else:
            print(arr[i], end = " ")    


print_number(n, arr)