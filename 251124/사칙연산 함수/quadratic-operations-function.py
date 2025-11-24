a, o, c = input().split()
a = int(a)
c = int(c)

def calc(a,o,c):
    match o:
        case'+':
            print(f"{a} + {c }= {a+c}")
            
        case'-':
            print(f"{a} - {c} = {a-c}")
            
        case'*':
            print(f"{a} * {c} = {a*c}")
            
        case'/':
            print(f"{a} / {c} = {a/c}")
            
        case '_':
            print('False')     


calc(a,o,c)                   