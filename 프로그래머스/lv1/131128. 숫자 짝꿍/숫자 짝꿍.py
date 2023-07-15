from collections import Counter

def solution(X, Y):
    answer = ""
    X, Y = Counter(X), Counter(Y)
    
    if set(X) & set(Y) == {"0"}:
        answer = "0"
    elif set(X) & set(Y) == set():
        answer = "-1"
    else:
        for idx in range(9, -1, -1):
            idx = str(idx)
            answer += idx * min(X[idx], Y[idx])
    
    return answer
    
