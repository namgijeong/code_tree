M, D = map(int, input().split())


def is_date_valid(M,D):
    if M == 2:
        if D >= 1 and D <= 28:
            return True
        else:
            return False 
    elif M == 1 or M == 3 or M == 5 or M == 7 or M == 8 or M == 10 or M == 12:
        if D >= 1 and D <= 31:
            return True
        else:
            return False  

    else:
        if D >= 1 and D <= 30:
            return True
        else:
            return False  


if is_date_valid(M,D):
    print("Yes")
else:
    print("No")    