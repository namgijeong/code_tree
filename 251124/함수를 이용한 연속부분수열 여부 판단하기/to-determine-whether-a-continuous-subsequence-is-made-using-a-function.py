n1, n2 = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

b_start_index = 0
a_start_index = 0

for i in range(n1):
    for j in range(n2):
        if a[i] == b[j]:
            b_start_index = j
            a_start_index = i
            break


is_true = true
for i in range(n2):
    if a[a_start_index] != b[b_start_index]:
        is_true = False
        break
else:
    is_true = True    


if is_true == True:
    print('Yes')
else:
    print('No')    


