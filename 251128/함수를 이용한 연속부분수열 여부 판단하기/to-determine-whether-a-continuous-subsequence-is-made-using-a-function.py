n1, n2 = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a_start_index = 0

def find_start_index(n1,n2,a,b):
    #바깥변수를 인식하려면 어쩔수 없이 global
    global a_start_index

    for i in range(n1):
        if a[i] == b[0]:
            b_start_index = 0
            a_start_index = i
            #print('b_start_index: ',b_start_index)
            #print('a_start_index: ',a_start_index)

            #123124  , 124 가 있을때 두번째 검사시에 수열임
            if is_suyal(n2,a,b):
                return True

    return False                



def is_suyal(n2,a,b):
    
    global b_start_index
    global a_start_index

    count = 0
    for i in range(n2):
        if (a_start_index + i) < n1 and (i) < n2 and a[a_start_index + i] != b[i]:
            return False
        count += 1    

    #인덱스를 벗어나서 b 길이만큼 검사못했을 수도 있다 
    if count == n2:
        return True  
    else:
        return False         
       

if find_start_index(n1,n2,a,b):
    print('Yes')
else :
    print('No')    

  


