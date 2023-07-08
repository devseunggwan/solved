def solution(k, scores):
    answer = []
    m = []
    
    for score in scores:
        m.append(score)
        m.sort()
        
        if len(m) == k+1:
            m = m[1:]    
        
        answer.append(m[0])
    
    return answer