def solution(code):
    mode = 0
    answer = ''
    
    for idx, s in enumerate(code):
        if s == "1":
            mode = 0 if mode else 1
        elif idx % 2 == mode:
            answer += s
            
    return answer if answer else "EMPTY"