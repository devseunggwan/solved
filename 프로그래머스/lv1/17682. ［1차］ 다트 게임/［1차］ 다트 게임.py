import re

def solution(DR):
    answer = 0
    
    p = re.findall(r"([0-9]+)([SDT])([\#\*]?)", DR)
    sdt = {
        "S": lambda x: x,
        "D": lambda x: x**2,
        "T": lambda x: x**3,
    }
    
    star = [1, 1, 1]
    for idx in [2, 1, 0]:
        star[idx] *= 2 if p[idx][2] == "*" else 1
        star[idx-1] *= 2 if p[idx][2] == "*" else 1
        acha = -1 if p[idx][2] == "#" else 1
        try:
            point = sdt[p[idx][1]](int(p[idx][0])) * star[idx] * acha    
        except:
            pass
        answer += point
        
    return answer