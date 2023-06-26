def solution(n_str):
    answer = ""
    is_first = True
    
    for n in n_str:
        if is_first and n == "0":
            continue
        else:
            is_first = False
            answer += n
    
    return answer