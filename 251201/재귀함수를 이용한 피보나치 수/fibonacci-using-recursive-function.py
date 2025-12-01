N = int(input())

def fibo(n):
    if n == 1:
        return 1
    elif n == 2 :
        return 1    

    n = fibo(n-1) + fibo(n-2)
    return n 


print(fibo(N))    