a, o, c = input().split()
a = int(a)
c = int(c)

def calc(a,o,c):
    switch(o):
        case '+':
            print(a+c)
        case '-':
            print(a-c)    
        case '*':
            print(a*c)
        case '/':
            print(a//c)
        default:
            print('False')     
            

calc(a,o,c)                   