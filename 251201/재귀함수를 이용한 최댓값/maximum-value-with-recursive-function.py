n = int(input())
arr = list(map(int, input().split()))

def max_array(index):
    if index == 0:
        return arr[index]

    max = max_array(index-1)
    
    #만약 기존 max보다 현재 인덱스가 크면 갱신
    if (max < arr[index]):
        max = arr[index]

    return max


print(max_array(n-1))   
   