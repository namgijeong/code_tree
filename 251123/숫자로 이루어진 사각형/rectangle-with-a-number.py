n = int(input())

# Please write your code here.
def print_n_square(n):
    sum = 1
    for i in range(n):
        for j in range(n):
            print(sum, end=" ")
            sum += 1

            if sum > 9:
                sum = 1

        print()
        
print_n_square(n)                