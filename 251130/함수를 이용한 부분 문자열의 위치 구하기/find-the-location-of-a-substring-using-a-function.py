text = input()
pattern = input()

def is_same(text_n, pattern_n, text_start_index):
    count = 0
    for i in range(pattern_n):
        if text[text_start_index + i] == pattern[i]:
            count += 1

    if count == pattern_n:
        return True
    else:
        return False                


def is_part():
    text_n = len(text)
    pattern_n = len(pattern)
    
    for i in range(text_n): 
        if text[i] == pattern[0]:
            if is_same(text_n, pattern_n,i):
                print(i)
                return

    print(-1)
    return         


is_part()