n = int(input())
arr = list(map(int, input().split()))

def zualde(n, arr):
    for i in range(n):
        arr[i] = abs(arr[i])


zualde(n,arr)   

for i in range(n):
    print(arr[i], end=" ")