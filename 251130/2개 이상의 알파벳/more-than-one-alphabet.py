A = input()

def count_alphabet(A):
    count = 1
    for i in range(len(A)-1):
        if A[i] != A[i+1]:
            count += 1

    if count >= 2:
        print('Yes')
    else:
        print('No')    


count_alphabet(A)