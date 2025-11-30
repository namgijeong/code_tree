A = input()

def is_palindrome(A):
    if len(A) == 1:
        return True

    else:
        if A[0] == A[-1]:
            return is_palindrome(A[1:-1])
        else:
            return False    

if is_palindrome(A):
    print("Yes")
else:
    print("No")            