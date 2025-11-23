n = int(input())

def number_position_sum(n):
    a = n//10
    b = n%10
    if (a+b)%5 == 0:
        return True
    else:
       return False

def is_yes(n):
    if n%2 == 0 and number_position_sum(n):
        print("Yes")
    else:
        print("No")    

is_yes(n)        
