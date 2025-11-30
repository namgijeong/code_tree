text = input()
pattern = input()

def is_same(text_n, pattern_n, text_start_index,pattern_start_index):
    count = 0
    for i in range(text_start_index, text_n):
        for j in range(pattern_start_index, pattern_n):
            if text[i] == pattern[j]:
                count += 1

    if count == pattern_n:
        return True
    else:
        return False                


def is_part():
    text_n = len(text)
    pattern_n = len(pattern)
    
    for i in range(text_n):
        for j in range(pattern_n):
            if text[i] == pattern[j]:
                if is_same(text_n, pattern_n,i,j):
                    print(i)
                    return

    print(-1)
    return         


is_part()