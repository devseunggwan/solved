def solution(my_string, overwrite_string, s):
    my_string, overwrite_string = list(my_string), list(overwrite_string)
    
    my_string[s:s+len(overwrite_string)] = overwrite_string
    return "".join(my_string)
    