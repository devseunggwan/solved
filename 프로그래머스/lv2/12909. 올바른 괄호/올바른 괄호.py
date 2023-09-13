def solution(s):
    answer = True
    stack = 0
    
    for i in s:
        if i == "(":
            stack += 1
        else:
            stack -= 1
        
        if stack < 0:
            answer = False
            break
    
    if stack != 0:
        answer = False
    
    return answer