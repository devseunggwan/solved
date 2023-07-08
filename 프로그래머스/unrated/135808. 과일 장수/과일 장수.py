def solution(k, m, score):
    result = 0
    greedy = sorted(score, reverse=True)
    for idx in range(0, len(greedy), m):
        if len(greedy) - idx < m:
            break
        
        result += min(greedy[idx:idx+m]) * m
    
    return result