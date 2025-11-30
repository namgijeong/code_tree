A = input()

def is_palindrome(A):
    if len(A) == 1:
        print('Yes')
        return 

    else:
        if A[0] == A[-1]:
            return is_palindrome(A[1:-1])
        else:
            print("No")
            return     

# if is_palindrome(A):
#     print("Yes")
# else:
#     print("No")    

is_palindrome(A)