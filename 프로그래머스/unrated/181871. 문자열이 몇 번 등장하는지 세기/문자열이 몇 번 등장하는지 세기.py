def solution(myString, pat):
    answer = 0
    
    for idx in range(len(myString)-len(pat)+1):
        if myString[idx:idx+len(pat)] == pat:
            answer += 1
    
    return answer