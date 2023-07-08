import re

def solution(DR):
    answer = 0
    
    p = re.findall(r"([0-9]+)([SDT])([\#\*]?)", DR)
    sdt = {
        "S": 1,
        "D": 2,
        "T": 3,
    }
    
    star = [1, 1, 1]
    for idx in [2, 1, 0]:
        star[idx] *= 2 if p[idx][2] == "*" else 1
        star[idx-1] *= 2 if p[idx][2] == "*" else 1
        acha = -1 if p[idx][2] == "#" else 1
        try:
            point = (int(p[idx][0]) ** sdt[p[idx][1]]) * star[idx] * acha    
        except:
            pass
        answer += point
        
    return answer