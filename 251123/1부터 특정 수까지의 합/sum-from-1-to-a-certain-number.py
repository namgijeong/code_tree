n = int(input())

def divide10(n):
    number_sum = 0
    for i in range(n+1):
        number_sum += i

    return number_sum//10

print(divide10(n))        

   