def solution(str_list):
    for idx, s in enumerate(str_list):
        if s == "l":
            return str_list[:idx]
        elif s == "r":
            return str_list[idx+1:]
            
    return []