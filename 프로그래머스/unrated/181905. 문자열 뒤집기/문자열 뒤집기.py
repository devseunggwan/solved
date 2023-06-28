def solution(my_string, s, e):
    my_string = list(my_string)
    my_string[s:e+1] = reversed(my_string[s:e+1])
    
    return "".join(my_string)