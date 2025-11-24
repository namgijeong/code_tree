n1, n2 = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

b_start_index = 0
a_start_index = 0

def find_start_index(n1,n2,a,b):
    #바깥변수를 인식하려면 어쩔수 없이 global
    global b_start_index
    global a_start_index

    for i in range(n1):
        for j in range(n2):
            if a[i] == b[j]:
                # print(a[i], ' ',b[j])
                # print(i, ' ',j)
                b_start_index = j
                a_start_index = i
                # print(a_start_index)
                # print(b_start_index)
                return


find_start_index(n1,n2,a,b)


is_true = True
for i in range(n2):
    if a[a_start_index] != b[b_start_index]:
        is_true = False
        break
    else:
        a_start_index += 1    
        b_start_index += 1

   

if is_true == True:
    print('Yes')
else:
    print('No')    


