y = int(input())

def isYunyear(y):
    if y%100 == 0 and y%400 !=0:
        return False
    if y%4 == 0:
        return True

    else:
        return False


if isYunyear(y):
    print("true")
else :
    print("false")                    