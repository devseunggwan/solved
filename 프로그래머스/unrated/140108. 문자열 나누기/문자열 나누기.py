def solution(s):
    answer = 0
    
    is_start = 0
    x = ""
    cnt_x = 0
    cnt_not_x = 0 
    
    for c in s:
        if not is_start:
            is_start += 1
            x = c
            cnt_x = 1
        else:
            if c == x:
                cnt_x += 1
            else:
                cnt_not_x += 1
        
        if cnt_x == cnt_not_x:
            answer += 1
            is_start = 0
            x = ""
            cnt_x = 0
            cnt_not_x = 0
    
    answer += is_start
    
    return answer