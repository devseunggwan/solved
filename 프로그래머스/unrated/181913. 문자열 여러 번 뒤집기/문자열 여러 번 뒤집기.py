def solution(my_string, queries):
    my_string = list(my_string)
    
    for s, e in queries:
        my_string[s:e+1] = reversed(my_string[s:e+1])
        
    return ''.join(my_string)