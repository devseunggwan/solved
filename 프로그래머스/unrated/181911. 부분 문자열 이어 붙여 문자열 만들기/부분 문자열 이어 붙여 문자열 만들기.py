def solution(my_strings, parts):
    return "".join([s[part[0]:part[1]+1] for s, part in zip(my_strings, parts)])