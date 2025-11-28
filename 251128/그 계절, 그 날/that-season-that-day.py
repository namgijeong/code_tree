Y, M, D = map(int, input().split())

def is_yunyear(Y):
    if Y % 4 != 0:
        return False
    elif Y % 400 == 0:
        return True
    elif Y % 100 == 0:
        return False
    else:
        return True


def if_yunyear_is_date_valid(M,D):
    if M == 2:
        if D >= 1 and D <= 29:
            return True
        else:
            return False 

    elif M == 1 or M == 3 or M == 5 or M == 7 or M == 8 or M == 10 or M == 12:
        if D >= 1 and D <= 31:
            return True
        else:
            return False  

    elif M == 4 or M == 6 or M == 9 or M == 11:
        if D >= 1 and D <= 30:
            return True
        else:
            return False  

    else:
        return False  


def if_not_yunyear(M,D):
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

    elif M == 4 or M == 6 or M == 9 or M == 11:
        if D >= 1 and D <= 30:
            return True
        else:
            return False  

    else:
        return False  


def what_season(M):
    if M < 3:
        print("Winter")
    elif M < 6:
        print("Spring")
    elif M < 9:
        print("Summer")
    elif M < 12:
        print("Fall")
    else:
        print("Winter")  

              
def is_date_valid(Y,M,D):
    if is_yunyear(Y):
        if if_yunyear_is_date_valid(M,D):
            #계절찍기
            what_season(M)
        else:
            print(-1)

    else:
        if if_not_yunyear(M,D):
            #계절찍기
            what_season(M)
        else:
            print(-1)    


is_date_valid(Y,M,D)            

